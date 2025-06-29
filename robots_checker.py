
from urllib.parse import urlparse
import urllib.robotparser

robot_parsers = {}

def can_crawl(url):
    parsed = urlparse(url)
    domain = f"{parsed.scheme}://{parsed.netloc}"

    if domain not in robot_parsers:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(f"{domain}/robots.txt")
        try:
            rp.read()
        except:
            return False
        robot_parsers[domain] = rp

    return robot_parsers[domain].can_fetch("*", url)
