
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from dhivehi_detector import is_dhivehi
from word_processor import WordProcessor
from robots_checker import can_crawl

class DhivehiCrawler:
    def __init__(self, start_url, storage_location):
        self.visited = set()
        self.to_visit = [start_url]
        self.word_processor = WordProcessor(storage_location)
    
    def start(self):
        while self.to_visit:
            url = self.to_visit.pop()
            if url in self.visited:
                continue
            self.visited.add(url)

            try:
                if not can_crawl(url):
                    continue
                print(f"Crawling: {url}")
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                text = soup.get_text(separator=" ")
                self.word_processor.process_text(text)

                for link in soup.find_all('a', href=True):
                    absolute = urljoin(url, link['href'])
                    if self.is_valid_url(absolute):
                        self.to_visit.append(absolute)
            except Exception as e:
                print(f"Failed to crawl {url}: {e}")

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https']
