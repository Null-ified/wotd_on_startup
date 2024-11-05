from bs4 import BeautifulSoup
import requests
import re 
import main


def webster_WOTD(r_obj:requests.Response):
    ''' Soup to decode -> Reg Expression + Soup to find attributes with WOTD
        -> Jump to proper page to extract rest of the info.'''    
    web_Soup = BeautifulSoup(r_obj.text, "html5lib")

    print("[DEBUG]: searching for better def and making list of examples")
    def wotd_def():
        for soup in web_Soup.find_all("div", class_=re.compile('(wod-definition-container)')):
            print(type(soup.p.text))
            return soup.p.text

    #DEBUG: Find all available examples.
    # Need solution for multiple example 
    print("Finding all examples starting with // via text")
    def wotd_examples()-> list:
        for soup in web_Soup.find_all("p"):
            if soup.text and re.match(r'^\s*//', soup.text):
                spliced = soup.text[3:]
                The_examples: list[str] = []   
                The_examples.append(spliced) 
        return The_examples
    

# Rewrite find alls, Fix problem with multiple  examples output 
    main.wotd_info(name = web_Soup.find_all("h2", class_=re.compile('(word)'))[0].string,
                 word_type = web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[1].string,
                 syllabes = web_Soup.find_all("span", class_=re.compile('(word)'))[0].string,
                 definition = wotd_def(),
                 examples = wotd_examples())