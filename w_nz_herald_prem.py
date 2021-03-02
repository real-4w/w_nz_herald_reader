import requests
from bs4 import BeautifulSoup
from tkinter.constants import LEFT
import yaml
import tkinter as tk
import textwrap
debug = False
window = True
#==============================================================================
# List of Articles
#==============================================================================
URLS = {"https://www.nzherald.co.nz/business/what-business-leaders-really-want-from-government/KPDBNBBK2NRPADUR7ADSZ64NKA/"
    }
#==============================================================================
# step 1: load URL into BeautifulSoup
#==============================================================================
def GetMySoup (URL):
    """This function takes a URL and returns a parsed soup."""
    if debug == True : print("+-" * 30, "\nStep 1: Getting URL: ", URL)
    #s1 = requests.Session()
    header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page1 = requests.get(URL, headers=header1)
    if debug == True :
        print("Page: ", page1)
        input("Enter to continue...")
    my_soup = BeautifulSoup(page1.content, 'lxml')
    return(my_soup)
#==============================================================================
# step S: Scrape the soup & wrap text
#==============================================================================
def ScrapeMySoup(soup):
    """This function scrapes my soup object and returns a wrapped string."""
    if debug == True : print("+-" * 30, "\nStep 2: Scraping the Soup.")
    s_content = soup.find_all("title")
    if debug == True : print(s_content)
    s_text = soup.find_all(text=True)
    #if debug == True : print(s_text)
    if debug == True : print(set([t.parent.name for t in s_text]))
    r_output = ''
    blacklist = ['[document]','script','header','html','meta','head','input','script',
        #'p',                                # WvdS
        'head','button','div','a','h1','h2','h3','h4','time','small',
        #'span',                            # WvdS
        #'title',                           # WvdS
        'figcaption']
        # there may be more elements you don't want, such as "style", etc.   
    for t in s_text:
        if t.parent.name not in blacklist:
            r_output += '{}\n '.format(t)
    wrapper = textwrap.TextWrapper(width=200) 
    output = wrapper.fill(text=r_output)
    return(output)

class ShowArticle():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("NZ Herald Article.")
        self.win.minsize(1280, 960)
        self.ctr = 1
        self.article_var = tk.StringVar()
        article_txt = f"NZ Herald premium Article:\n"
        self.article_var.set(article_txt)
        w_lab=tk.Label(self.win, textvariable=self.article_var, justify=tk.LEFT)
        w_lab.place(x=20, y=0)
        self.updater()
        self.win.mainloop()
    def updater(self):
        self.ctr -= 1
        update_label = f"Next refresh in {str(self.ctr)} seconds."
        self.win.title(update_label)
        if self.ctr > 0:
            self.win.after(1000, self.updater)
        else:
            article_txt = article
            self.article_var.set(article_txt)
            self.ctr = 60
            self.win.after(1000, self.updater)
#============================================================================================================================
if __name__ == "__main__" :                                     # execute only if run as a script
    for target in URLS :
        if debug == True :
            print(f"{URLS}")
        nzh_soup = GetMySoup(target)
        article= ScrapeMySoup(nzh_soup)
        if debug == True : print(article)
    if window == True : SA=ShowArticle()
