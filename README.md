# E-Book PDF Downloader

This script searches for and downloads free Assembly programming e-books in PDF format from Google search results. The downloaded PDFs are saved in a directory within the user's home folder.

## Features

- Searches Google for free Assembly programming e-books.
- Parses search results to find direct links to PDF files.
- Downloads and saves PDFs to a directory in the user's home folder.
- Handles network errors and retries when necessary.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/pleaseful/ebook-scraper.git
   cd ebook-scraper
   ```

2. **Install Required Libraries:**
   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

1. **Run the Script:**
   ```sh
   python ebook_scraper.py
   ```

2. **The script will:**
   - Search Google for free Assembly programming e-books in PDF format.
   - Download the PDF files found.
   - Save the PDFs in the `./books` directory.

## Notes

- Ensure you have write permissions for the directory where PDFs will be saved.
- Be mindful of the ethical and legal considerations regarding downloading and distributing e-books.

## Troubleshooting

If you encounter any issues:

1. **Permissions:**
   - Ensure you have the necessary write permissions for the `~/books` directory.

2. **Check Output:**
   - Monitor the script output for any error messages or issues with downloading specific files.

3. **Dependencies:**
   - Verify that the required Python libraries are installed and up to date.

## License

This project is licensed under the MIT License.
