
import re

thaana_regex = re.compile(r'[\u0780-\u07BF]')

def is_dhivehi(text):
    return bool(thaana_regex.search(text))
