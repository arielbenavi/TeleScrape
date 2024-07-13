# Telegram Channel Scraper

This project is a Python-based scraper for public Telegram channels. It allows users to extract messages and links from specified channels, with options for filtering by time and link types.

## Features

- Scrape messages from public Telegram channels
- Extract specific types of links (e.g., Twitter, Facebook)
- Apply time filters to retrieve recent messages
- Output results to CSV file
- Customizable user agent rotation

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/telegram-channel-scraper.git
   cd telegram-channel-scraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Basic usage:

```
python telegram_scraper.py channel_name
```

Advanced usage:

```
python telegram_scraper.py channel_name --link-types twitter.com facebook.com --time-filter 7 --output results.csv
```

This command scrapes the specified channel, extracts Twitter and Facebook links from messages posted in the last 7 days, and saves the results to `results.csv`.

## Arguments

- `channel_name`: Name of the Telegram channel to scrape (required)
- `--link-types`: Specific link types to extract (optional)
- `--time-filter`: Number of days to filter messages (optional)
- `--output`: Output file name (default: output.csv)

## Examples

Check the `examples/` directory for more usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.