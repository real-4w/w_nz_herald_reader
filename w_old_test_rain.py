import requests
from bs4 import BeautifulSoup
import pandas as pd
debug = False
#==============================================================================
# List of weather stations
#==============================================================================
URLS = {"http://waitakeres.co.nz/", "http://www.pjb.co.nz/",
        "http://www.janter.co.nz/weather/index.htm","https://opotikiweather.nz/",
        "http://www.nzpws.net/bishopdale/index.htm","http://nzpws.net/frasertown/index.htm"
    }
#==============================================================================
# step 1: load URL into BeautifulSoup
#==============================================================================
def GetMySoup (URL):
    """This function takes a URL and returns a parsed soup."""
    #print("+-" * 30, "\nStep 1: Scraping URL: ", URL)
    s1 = requests.Session()
    header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    page1 = requests.get(URL, headers=header1)
    if debug == True :
        print("Page: ", page1)
        input("Enter to continue...")
    my_soup = BeautifulSoup(page1.content, 'lxml')
    #if debug == True :
    #    print(my_soup)
    #    input("Enter to continue...")
    return my_soup
#==============================================================================
# step S: Scrape the #2 table: get the TDs
#==============================================================================
def ScrapeMySoup(soup):
    """This function scrapes my soup object and returns a list of strings."""
    #print(f"Step 2 using {soup.title.text} second table on page & onwards")
    weather_table = soup.find_all("table")
    #print(weather_table[0])            #First table can be ignored, not interest in that data
    #print(weather_table[1])
    rainfall_table_tr = weather_table[1].find_all("tr", attrs={"class":"td_rainfall_data"})
    #print("Step 3 Scrape Table Rows (TR) found (is a list with TDs)")
    #print(type(rainfall_table_tr))
    #print(rainfall_table_tr)
    #print ("3 Going into for loop. =========================================")
    w_list = []
    w_list.append(soup.title.text)
    for trs in rainfall_table_tr:
        w1_string = ''
        w2_string = ''
        #print (trs)
        tds = trs.find_all('td')
        #print ("4a printing tds ===========================================")
        #print(tds)
        #print ("4b print len tds ==========================================")
        #print(len(tds))
        #for i in range (0,len(tds)):                                   # variable pairs
        #    w_string = w_string.strip() + ' ' +  tds[i].text           # needs code below
        w1_string = tds[0].text.strip()                                 # data comes in pairs
        w1_string = w1_string + ' ' + tds[1].text.strip()               # attribute - value
        w2_string = tds[2].text.strip()
        w2_string = w2_string.strip() + ' ' + tds[3].text
            #print ("4c print ====================================================")
            #print (i, tds[i].text)
            #print (i, tds[i].get_text())
        #Add into a dataframe with location, attribute and value
        #print(w1_string, w2_string)
        w_list.append(w1_string)
        w_list.append(w2_string)
    #print(len(w_list))
    #print(w_list)
    return(w_list)
    #w_df = pd.DataFrame(w_list, columns=['Scraped'])
    #print (w_df['Scraped'])

if __name__ == "__main__":                    # execute only if run as a script
    station_list=[]                           # one list for all scrapes
    if debug == True : 
        print(f"URLs: {URLS}")
        print(station_list)
    for target in URLS:
        if debug == True : print(target)
        station_list.append(ScrapeMySoup(GetMySoup(target)))
    if debug == True :
        print(f"Loaded #: {len(station_list)}")
        print(station_list)
    w_df = pd.DataFrame(station_list, columns=['Station', 'Today', 'Rate', 'Month', 'Year', 'Last Hour', 'Last Fall'])
    pd.set_option("display.max_colwidth", 32)
    print(w_df[['Station', 'Today', 'Rate', 'Last Fall']])
