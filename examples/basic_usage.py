from telegram_scraper import TelegramScraper

def main():
    scraper = TelegramScraper()
    channel_name = 'example_channel'
    
    df = scraper.scrape_channel(channel_name)
    
    print(f"Scraped {len(df)} messages from {channel_name}")
    print(df.head())

if __name__ == "__main__":
    main()