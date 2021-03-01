import requests
from bs4 import BeautifulSoup
import pandas as pd
debug = True
#==============================================================================
# List of Articles
#==============================================================================
URLS = {"https://www.nzherald.co.nz/business/online-ghosts-facebooks-millennial-reach-is-thousands-above-nz-population/PR6ZSNI6EZIVRWKDB65WMCC4Y4/"
    }
#==============================================================================
# step 1: load URL into BeautifulSoup
#==============================================================================
def GetMySoup (URL):
    """This function takes a URL and returns a parsed soup."""
    if debug == True : print("+-" * 30, "\nStep 1: Scraping URL: ", URL)
    s1 = requests.Session()
    header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page1 = requests.get(URL, headers=header1)
    if debug == True :
        print("Page: ", page1)
        input("Enter to continue...")
    my_soup = BeautifulSoup(page1.content, 'lxml')
    if debug == True :
        print(my_soup)
        input("Enter to continue...")
    return my_soup


if __name__ == "__main__" :                                     # execute only if run as a script
    for target in URLS :
        if debug == True :
            print(f"{URLS}")
        nzh_soup = GetMySoup(target)