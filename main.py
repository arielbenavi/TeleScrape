import argparse
from telegram_scraper import TelegramScraper

def main():
    parser = argparse.ArgumentParser(description='Telegram Channel Scraper')
    parser.add_argument('channel_name', help='Name of the Telegram channel to scrape')
    parser.add_argument('--link-types', nargs='*', help='Specific link types to extract (e.g., twitter.com facebook.com)')
    parser.add_argument('--time-filter', type=int, help='Number of days to filter messages')
    parser.add_argument('--output', default='output.csv', help='Output file name')
    parser.add_argument('--limit', type=int, default=500, help='Maximum number of messages to scrape')

    args = parser.parse_args()

    scraper = TelegramScraper()
    df = scraper.scrape_channel(args.channel_name, args.link_types, args.time_filter, args.limit)

    if not df.empty:
        df.to_csv(args.output, index=False)
        print(f"Data saved to {args.output}")
        print(f"Total messages scraped: {len(df)}")
        if args.link_types:
            for link_type in args.link_types:
                count = df['links'].apply(lambda x: any(link_type in link for link in x)).sum()
                print(f"Messages containing {link_type} links: {count}")
    else:
        print("No data found or all data filtered out.")

if __name__ == "__main__":
    main()