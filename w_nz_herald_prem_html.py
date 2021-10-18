import w_nz_herald_prem_scrape as w_scrape
import time
#============================================================================================================================
debug, yaml_data = w_scrape.ProcessYAML('config.yaml')                           # yaml settings are global variables
if __name__ == "__main__" :                                                      # execute only if run as a script
    window = yaml_data['window']
    URLS = yaml_data['URLS']                                                     # List of Articles stored in yaml file
    news_list = []
    doc_name = time.strftime("%Y%m%d-%H%M%S") + '_NZ_Herald_Premium.html'
    w_html = open(doc_name,"w", encoding="utf-8")
    w_html.write("<html>\n<head>\n<title> \nOutput Data in an HTML file\n \
           </title>\n</head> <body> <h1>Welcome to \
           <font color = #00b300>NZ Herald Premium Reader</font></h1>\n \
           <h2>Premium news the cheap way.</h2>\n</body></html>")

    for target in URLS :
        w_html.write(f'<h2>{target}.</h2><p style="font-family:Arial">')
        if debug == True : print(f"{len(URLS)} URLS:{URLS}")
        nzh_soup = w_scrape.GetMySoup(target)
        article= w_scrape.ScrapeMySoup(nzh_soup)
        if debug == True : print(article)
        news_list.append(article)    
        w_html.write(article)
        w_html.write(f"</p>")
        if debug == True :print(f"Length news_list is now {len(news_list)}")
    w_html.close()
    