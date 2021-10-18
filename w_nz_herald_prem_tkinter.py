import w_nz_herald_prem_scrape as w_scrape
import tkinter as tk
from tkinter.constants import LEFT

class ShowArticle():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("NZ Herald Article.")
        self.win.minsize(1280, 960)
        self.ctr = 1
        self.ai = 0
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
            article_txt = news_list[self.ai]
            if self.ai < len(news_list)-1 : self.ai += 1
            else : self.ai = 0
            self.article_var.set(article_txt)
            self.ctr = 60
            self.win.after(1000, self.updater)
#============================================================================================================================
debug, yaml_data = w_scrape.ProcessYAML('config.yaml')                           # yaml settings are global variables
if __name__ == "__main__" :                                                 # execute only if run as a script
    window = yaml_data['window']
    URLS = yaml_data['URLS']                                                # List of Articles stored in yaml file
    news_list = []
    for target in URLS :
        if debug == True : print(f"{len(URLS)} URLS:{URLS}")
        nzh_soup = w_scrape.GetMySoup(target)
        article= w_scrape.ScrapeMySoup(nzh_soup)
        #if debug == True : print(article)
        news_list.append(article)    
        if debug == True :print(f"Length news_list is now {len(news_list)}")
    if window == True : SA=ShowArticle()