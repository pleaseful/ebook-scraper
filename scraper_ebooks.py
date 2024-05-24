import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# Use a directory within the user's home folder
SAVE_DIR = os.path.expanduser("~/books")

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def get_soup(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    return BeautifulSoup(response.content, 'html.parser')

def is_valid_pdf_url(url):
    return url.endswith('.pdf')

def find_pdfs_on_page(url):
    soup = get_soup(url)
    if not soup:
        return []

    pdf_urls = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if is_valid_pdf_url(href):
            pdf_urls.append(urljoin(url, href))
        elif 'pdf' in href.lower():
            full_url = urljoin(url, href)
            pdf_urls.extend(find_pdfs_on_page(full_url))
    return pdf_urls

def search_for_ebooks(query):
    ebook_urls = []
    for page in range(1, 4):
        search_url = f"https://www.google.com/search?q={query}&start={(page - 1) * 10}"
        soup = get_soup(search_url)

        if not soup:
            continue

        for result_block in soup.find_all('a'):
            href = result_block.get('href')
            if href and 'url?q=' in href:
                end_pos = href.find("&sa=")
                url = href[href.find('url?q=')+len('url?q='):end_pos]
                if 'pdf' in url.lower():
                    ebook_urls.append(url)
                else:
                    ebook_urls.extend(find_pdfs_on_page(url))
        time.sleep(2)

    return list(set(ebook_urls))

def download_pdf(url, save_dir):
    local_filename = os.path.join(save_dir, os.path.basename(url))
    try:
        with requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded {url} to {save_dir}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def main():
    query = "free Assembly programming e-books filetype:pdf"
    ebook_urls = search_for_ebooks(query)

    for url in ebook_urls:
        print(f"Downloading {url}")
        download_pdf(url, SAVE_DIR)

if __name__ == '__main__':
    main()