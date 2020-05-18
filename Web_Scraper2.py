import requests
import io
import sys
import easygui as eg
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def getWebPage():
    #ua = UserAgent()
    #proxies = {'http' : 'http://10.10.0.0:0000', 'https': 'http://120.10.0.0:0000'}    
    text_file = open("Text_Output.txt", 'w');
    eg.msg = "Enter the URL"
    url = eg.enterbox(default = 'http://', 
                      msg = 'Enter the url of website you wanna scrape', title = 'Web Scraper', strip = 1)
    if url is None:
        sys.exit(0)
    page = requests.get(url, timeout = 150); #, proxies = proxies
    soup = BeautifulSoup(page.text, 'html.parser');
    result = soup.get_text()
    print('Scraping Successful')
    with io.open("Text_Output.txt", "w", encoding="utf-8") as f:
        f.write(result)
    text_file.close();
    print('Output successful')

def main():
    getWebPage();
     
    
main()
