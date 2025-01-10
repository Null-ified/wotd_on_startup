from bs4 import BeautifulSoup
import main
import requests
import re 
import time


def webster_WOTD(r_obj:requests.Response):
    ''' Soup to decode -> Reg Expression + Soup to find attributes with WOTD
        -> Jump to proper page to extract rest of the info.'''    
    oxford_Soup = BeautifulSoup(r_obj.text, "html5lib")

    wotd = oxford_Soup.find(class_="word-header-txt").text

   
    #DEBUG: Find some available examples.
    # Need solution for multiple example 
    print("Finding some examples starting with // via text")
    def wotd_example()-> str:
        for soup in oxford_Soup.find_all("p"):
            if soup.text and re.match(r'^\s*//', soup.text):
                spliced = soup.text[3:]    
        return spliced

    #def wotd_offical_entry_request(): 
        #time.sleep(1)
        #main.request_connection_Execptions(f"https://www.merriam-webster.com/dictionary/{wotd}") 
    
    main.wotd_display(name = wotd,
                 word_type = oxford_Soup.find(class_=re.compile('(main-attr)')).text,
                 syllabes = oxford_Soup.find(class_=re.compile('(word-syllables)')).text,
                 definition = oxford_Soup.find("div", class_=re.compile('(wod-definition-container)')).contents[3].text,
                 examples = wotd_example(),
                 link = f"https://www.merriam-webster.com/dictionary/{wotd}")