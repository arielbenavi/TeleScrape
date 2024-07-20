# Telegram Channel Scraper

This project is a Python-based scraper for public Telegram channels. It allows users to extract messages and links from specified channels, with options for filtering by time and link types, as well as generating recaps of scraped messages.

## Features

- Scrape messages from public Telegram channels
- Extract specific types of links (e.g., Twitter (X), Facebook)
- Apply time filters to retrieve recent messages
- Output results to CSV file
- Customizable user agent rotation
- Generate AI-powered recaps of scraped messages

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/arielbenavi/TeleScrape.git
   cd TeleScrape
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) If you want to use the recap feature, create an API key file:
   - For RapidAPI: Create a file named `rapid_api_key.txt` with your RapidAPI key.
   - For ChatGPT API: Create a file named `chatgpt_api_key.txt` with your OpenAI API key.

## Usage

Basic usage:

```
python main.py channel_name
```

Advanced usage:

```
python main.py channel_name --link-types twitter.com facebook.com --time-filter 7 --output results.csv --limit 100 --recap --api-type chatgpt
```

This command scrapes the specified channel, extracts Twitter and Facebook links from the last 100 messages posted in the last 7 days, saves the results to `results.csv`, and generates a recap using the ChatGPT API.

## Arguments

- `channel_name`: Name of the Telegram channel to scrape (required)
- `--link-types`: Specific link types to extract (optional)
- `--time-filter`: Number of days to filter messages (optional)
- `--output`: Output file name (default: output.csv)
- `--limit`: Maximum number of messages to scrape (default: 500)
- `--recap`: Generate a recap of scraped messages (optional)
- `--api-type`: API to use for recap, either 'rapid' or 'chatgpt' (default: rapid)

## Examples

Check the `examples/` directory for more usage examples.

## Recap Feature

The recap feature uses AI to generate a summary of the scraped messages. You can choose between two API options:

1. RapidAPI (default): Requires a `rapid_api_key.txt` file with your RapidAPI key. You can get a free test key with 10 requests/day here: https://rapidapi.com/haxednet/api/chatgpt-api8
2. ChatGPT API: Requires a `chatgpt_api_key.txt` file with your OpenAI API key (paid).

To use the recap feature, add the `--recap` flag to your command. You can specify the API type with `--api-type`:

```
python main.py channel_name --limit 100 --recap --api-type chatgpt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.