# Dota 2 Patch Scraper
This Python script fetches and parses patch notes from the official Dota 2 website. The extracted information includes the patch number, release timestamp, general notes, item changes, and hero changes (including new additions).

## Features
1. Fetches patch notes from multiple versions.
2. Handles different HTML structures for various patch note pages.
3. Extracts the following data from each patch note:

    - Patch number
    - Release timestamp (in epoch format)
    - General notes
    - Item changes
    - Hero changes (including new heroes)

## Dependencies
The script depends on the following Python libraries:

- requests: For sending HTTP requests.
- bs4 (BeautifulSoup): For parsing HTML.
- datetime: For converting date strings to epoch timestamps.
- json: For handling JSON data.

You can install these dependencies using pip:

```bash
pip install requests bs4 datetime json
```
## How to Use
First, define a list of patch versions you want to scrape. For example:

```python
patch_versions = ["6.00","6.01","6..."]
```

Then, run the script:

```bash
python patch_scraper.py
```

The script will fetch and parse the patch notes for each version, then save the data to a JSON file named patch_notes.json.

## Output
The output is a JSON file named patch_notes.json, which contains an array of patch note data. Each element in the array is a dictionary with the following structure:

```json
{
    "patch_number": "<version number>",
    "patch_timestamp": "<release timestamp>",
    "general": ["<general note 1>", "<general note 2>", ...],
    "items": {
        "<item name>": ["<change 1>", "<change 2>", ...],
        ...
    },
    "heroes": {
        "Added": ["<new hero 1>", "<new hero 2>", ...],
        "<hero name>": ["<change 1>", "<change 2>", ...],
        ...
    }
}
```

## Caveats and Limitations

- The script might not work correctly if the structure of the Dota 2 website changes.
- The script might not fetch or parse data correctly if there are inconsistencies in the structure or content of the patch notes.
- The script doesn't handle errors or exceptions beyond basic error logging. It's recommended to monitor the script's output for any error messages.