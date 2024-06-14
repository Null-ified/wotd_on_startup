from bs4 import BeautifulSoup
import requests
import re 
import main

def webster_WOTD(r_obj:requests.Response):
    ''' Soup to decode -> Reg Expression + Soup to find attributes with WOTD
        -> Jump to proper paper to extract rest of the info.'''    
    web_Soup = BeautifulSoup(r_obj.text, "html5lib")

    # Filter for div tag with class attribute that has wotd and look at its children's element
    print("[DEBUG]: Printing out matched tags for word def")
    for soup in web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)') ):
        print(soup['class'])    
    
    #wotd   
    print("[DEBUG]: Printing out matched tags for word name + other details")
    for soup in web_Soup.find_all("div", class_=re.compile('(word)') ):
        print(soup['class'])  

    print("[DEBUG]: MORE DEBUGGING")
    for soup in web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)') ):
        print(soup.p)


    main.wotd_info(name = web_Soup.find_all("h2", class_=re.compile('(word)'))[0].string,
                 word_type = web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[1].string,
                 syllabes = web_Soup.find_all("span", class_=re.compile('(word)'))[0].string,
                 definition = web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)'))[0].p.string,
                 example = web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)') )[0].p.find_next("p"),
)
