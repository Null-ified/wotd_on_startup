from bs4 import BeautifulSoup
import re
import requests

#All of this will get refactored eventually I swear


#Printing out choices and error checking
def Choices():
    print("Please select one of the following sites to know the word of the day of:")
    print("[] Webster Dictionary | A ")
    print("[] Oxford Dictionary | B ")
    print("[] Dictionary.com | C ")
    
    valid_choices = {'A', 'B', 'C'}

    while True:
        choice = input("Enter letter corresponding to site: ").strip().upper()
        
        if choice in valid_choices:
            print(f"You selected option {choice}.")
            return choice  # Or call a function based on the choice
        else:
            print("Invalid input. Please enter either A, B, or C.")

       
def siteResponseObjGenerator(choice:chr):
    match choice:
        case 'A': 
            print("[x] Webster Dictionary | A ")
            r_webster = requests.get("https://www.merriam-webster.com/word-of-the-day")
            return r_webster, "Webster"
        case 'B': 
            print("[x] Oxford Dictionary")
            r_Oxford = requests.get("https://www.oed.com/")
            return r_Oxford, "Oxford"
        case 'C':
            print("[x] Dictionary.com | C ")
            r_Dictionary = requests.get("https://www.dictionary.com/e/word-of-the-day/")
            return r_Dictionary, "Dictionary"
        

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
    
    #Nonetype not subscriptable, need fix
    wotd_info = {
        'name': web_Soup.find_all("div", class_=re.compile('(word)'))[0].contents,
        'word type': web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[0].string,
        'syllabes': web_Soup.find_all("div", class_=re.compile('(word)'))[2].contents[1].string,
        'definition': web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)'))[0].p.string,
        'example': web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)') )[1].p.string,
}
    print(f"Name of WOTD: {wotd_info['name']}")

''' #Word type 
print(f"Word: {web_Soup.find_all("div", class_=re.compile('(word)'))[2].content[0].string}\n")

#prints def
print(f"Definition: {web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)'))[0].p.string}\n")

#prints examples
print(f"Example of {web_Soup.find_all("div", class_=re.compile('(wotd|word of the day|definition)') )[1].p.string}")

'''

#Refactor type checks eventually
def Request_Debug(requestobj:requests.Response):    
    print("==========================")
    print(f"REQUEST CONTENT DEBUG: {requestobj.content}")
    print("==========================")

def StatusCheck(requestobj:requests.Response):
    if (requestobj.status_code != 200): 
        print(f"Webster status code: {requestobj.status_code}")
    else:
        print(f"Webster status code: {requestobj.status_code}")

#rObj_ChosenSite[1](Tuple) for crawling on specific site 
#main
rObj_ChosenSite = siteResponseObjGenerator(Choices())


match(rObj_ChosenSite[1]):
    case "Webster":
        print("Run Webster Function")
        webster_WOTD(rObj_ChosenSite[0])
    case "Oxford":
        print("Run Oxford Function")
    case "Dictionary.com":
        print("Run Dictionary.com Function")
    case _: 
        raise Exception("[Err] Default case was reached.")

