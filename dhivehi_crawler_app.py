
from crawler import DhivehiCrawler

if __name__ == "__main__":
    start_url = "https://www.example.com"  # Replace with target start site
    storage_location = r"C:\Users\W-book\Documents\crawler"

    crawler = DhivehiCrawler(start_url, storage_location)
    crawler.start()
