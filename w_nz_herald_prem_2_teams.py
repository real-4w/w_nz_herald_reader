import w_nz_herald_prem_scrape as w_scrape, pymsteams
#============================================================================================================================
debug, yaml_data = w_scrape.ProcessYAML('config.yaml')                           # yaml settings are global variables
if __name__ == "__main__" :                                                      # execute only if run as a script
    URLS = yaml_data['URLS']                                                     # List of Articles stored in yaml file
    web_hook = yaml_data['web_hook']                                             # MS Teams webhook URL
    myTeamsMessage = pymsteams.connectorcard(web_hook)
    
    for target in URLS :
        myTeamsMessage.title (f"Article: {target}")
        if debug == True : print(f"{len(URLS)} URLS:{URLS}")
        nzh_soup = w_scrape.GetMySoup(target)
        article= w_scrape.ScrapeMySoup(nzh_soup)
        if debug == True : print(article)
        myTeamsMessage.text(article)
        if debug == True :  
            myTeamsMessage.printme()
        else :
            myTeamsMessage.send()
   