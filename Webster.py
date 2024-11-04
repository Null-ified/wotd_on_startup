from bs4 import BeautifulSoup
import requests
import re 
import main

'''
Goal for fetching
    Grab WOTD via big font
    Def is found right before example, so have soup find //'s tag first then have it look up child coming before it
    Pattern for example is that inside of wod def container, the words after the // is the example.     
    have soup find tags that have // as element and parse that tags contents

'''

def webster_WOTD(r_obj:requests.Response):
    ''' Soup to decode -> Reg Expression + Soup to find attributes with WOTD
        -> Jump to proper page to extract rest of the info.'''    
    web_Soup = BeautifulSoup(r_obj.text, "html5lib")

    print("[DEBUG]: searching for better def and making list of examples")
    def wotd_def():
        for soup in web_Soup.find_all("div", class_=re.compile('(wod-definition-container)')):
            return soup.p.text


    
    #Debug finding potential container with wotd info   
    ''' print("[DEBUG]: Printing out matched tags for word name + other details")
    for soup in web_Soup.find_all("div", class_=re.compile('(word)') ):
        print(soup['class'])  '''

    '''print("[DEBUG]: MORE DEBUGGING")
    for soup in web_Soup.find_all("div", class_=re.compile('(wotd|wod|word of the day|definition)') ):
        print(soup.p)
    '''

    #Find all available examples
    print("Finding all examples starting with // via text")

    # hey = web_Soup.find_all(string=re.compile(r'^//(.*)', re.DOTALL))
    ''' for soup in hey:
        print(soup)'''
    def wotd_examples():
        #Need to only return the examples man
        for soup in web_Soup.find_all("p"):
            if soup.text and re.match(r'^\s*//', soup.text):
                print(soup.text)
        return soup.text
    

# Rewrite with find 
    main.wotd_info(name = web_Soup.find_all("h2", class_=re.compile('(word)'))[0].string,
                 word_type = web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[1].string,
                 syllabes = web_Soup.find_all("span", class_=re.compile('(word)'))[0].string,
                 definition = wotd_def(),
                 example = wotd_examples())
    


''' #valid
  main.wotd_info(name = web_Soup.find_all("h2", class_=re.compile('(word)'))[0].string,
                 word_type = web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[1].string,
                 syllabes = web_Soup.find_all("span", class_=re.compile('(word)'))[0].string,
                 definition = main.cull_tags(web_Soup.find("div", class_=re.compile('(wotd|word of the day|definition)')).p),
                 example = web_Soup.find("p", text=re.compile(r'^\s*//') ))

'''