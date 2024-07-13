from telegram_scraper import TelegramScraper

def main():
    scraper = TelegramScraper()
    channel_name = 'example_channel'
    link_types = ['twitter.com', 'facebook.com']
    time_filter = 7
    
    df = scraper.scrape_channel(channel_name, link_types=link_types, time_filter=time_filter)
    
    print(f"Scraped {len(df)} messages from {channel_name} in the last {time_filter} days")
    print("Links found:")
    for _, row in df.iterrows():
        print(f"Message: {row['message_link']}")
        for link_type, links in row['links'].items():
            print(f"  {link_type}: {links}")

if __name__ == "__main__":
    main()