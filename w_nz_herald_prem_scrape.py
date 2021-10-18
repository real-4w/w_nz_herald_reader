import requests
from bs4 import BeautifulSoup
import yaml
import textwrap
#==============================================================================
def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object.'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (debug, y_data)   
#==============================================================================
debug, yaml_data = ProcessYAML('config.yaml')                           # yaml settings are global variables
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
# step 2: Scrape the soup & wrap text
#==============================================================================
def ScrapeMySoup(soup):
    """This function scrapes my soup object and returns a wrapped string."""
    if debug == True : print("+-" * 30, "\nStep 2: Scraping the Soup.")
    s_content = soup.find_all("title")
    if debug == True : print(s_content)
    s_text = soup.find_all(text=True)
    if debug == True : print(set([t.parent.name for t in s_text]))
    r_output = ''
    blacklist = ['[document]','script','header','html','meta','head','input','script',
        'head','button','div','a','h1','h2','h3','h4','time','small','figcaption']
        #'span','title','p'# there may be more elements you don't want, such as "style", etc.   
    for t in s_text:
        if t.parent.name not in blacklist:
            r_output += '{}'.format(t) + '\n'
    wrapper = textwrap.TextWrapper(width=200) 
    output = wrapper.fill(text=r_output)
    return(output)