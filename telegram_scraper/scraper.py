import re
from datetime import datetime, timedelta
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import random

class TelegramScraper:
    def __init__(self, user_agents_file='user_agents.txt'):
        self.user_agents = self.load_user_agents(user_agents_file)

    @staticmethod
    def load_user_agents(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f]

    def get_random_user_agent(self):
        return {'User-Agent': random.choice(self.user_agents)}

    def request(self, url, headers=None, cookies=None):
        if not headers:
            headers = self.get_random_user_agent()
        time.sleep(0.5)
        return requests.get(url, headers=headers, cookies=cookies)

    def scrape_channel(self, channel_name, link_types=None, time_filter=None, limit=200):
        if link_types:
            return self._scrape_channel_with_link_types(channel_name, link_types, time_filter, limit)
        
        all_results = pd.DataFrame()
        before = None

        while len(all_results) < limit:
            df = self._scrape_channel_page(channel_name, None, time_filter, before)
            if df.empty:
                break

            # Concatenate new results and remove duplicates
            all_results = pd.concat([all_results, df], ignore_index=True)
            all_results.drop_duplicates(subset='message_link', keep='first', inplace=True)

            if time_filter:
                oldest_message_time = all_results['message_time'].min()
                if (datetime.utcnow() - pd.to_datetime(oldest_message_time)).days > time_filter:
                    break

            # Get the 'before' value for the next iteration
            last_message_link = df['message_link'].iloc[-1]
            before = int(last_message_link.split('/')[-1]) - 20

            print(f"[+] Scraped {len(df)} messages. Total unique: {len(all_results)}. Next 'before': {before}")

            if len(all_results) >= limit:
                break

        return all_results.head(limit)

    def _scrape_channel_with_link_types(self, channel_name, link_types, time_filter, limit):
        results = []
        for link_type in link_types:
            df = self._scrape_channel_page(channel_name, link_type, time_filter)
            results.append(df)
        
        combined_df = pd.concat(results, ignore_index=True)
        
        grouped = combined_df.groupby('message_link').agg({
            'message_text': 'first',
            'message_time': 'first',
            'links': lambda x: list(set(link for sublist in x for link in sublist))
        }).reset_index()
        
        return grouped.head(limit)

    def _scrape_channel_page(self, channel_name, link_type, time_filter, before=None):
        url = f'https://t.me/s/{channel_name}'
        if link_type:
            url += f'?q={link_type}'
        if before:
            url += f'{"?" if "?" not in url else "&"}before={before}'
        
        print(f'[*] Scraping data from {url} ...')
        response = self.request(url)
        if not response:
            print(f"Failed to fetch data for channel: {channel_name}")
            return pd.DataFrame()

        soup = BeautifulSoup(response.text, 'lxml')
        messages = soup.find_all('div', class_='tgme_widget_message_bubble')

        data = []
        for msg in messages:
            message_data = self.parse_message(msg, link_type, time_filter)
            if message_data:
                data.append(message_data)

        print(f'[+] Scraped {len(data)} messages from {url}')
        return pd.DataFrame(data)

    def parse_message(self, msg, link_type, time_filter):
        context = msg.text.strip()
        date_link = msg.find('a', class_='tgme_widget_message_date', href=True)
        
        if not date_link:
            return None

        message_link = date_link['href']
        message_time = date_link.find(class_='time')['datetime']
        
        if time_filter and not self.is_within_time_filter(message_time, time_filter):
            return None

        links = self.extract_links(context, link_type)

        return {
            'message_text': context,
            'message_link': message_link,
            'message_time': message_time,
            'links': links
        }

    @staticmethod
    def is_within_time_filter(message_time, time_filter):
        message_date = datetime.strptime(message_time.split('T')[0], '%Y-%m-%d')
        time_difference = datetime.utcnow() - timedelta(days=int(time_filter))
        return message_date >= time_difference

    @staticmethod
    def extract_links(text, link_type):
        if not link_type:
            # Extract all URLs if no specific link type is provided
            url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            return re.findall(url_pattern, text)
        
        pattern = f'({link_type}/.*?)[\)\s\n\r\t<\\@\*\'\"\,]'
        found_links = re.findall(pattern, text + '  ')
        return [link.rstrip('\r\n\t@') for link in found_links]