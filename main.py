from bs4 import BeautifulSoup
import re
import requests

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

#rObj_ChosenSite[1] for crawling on specific site 
rObj_ChosenSite = siteResponseObjGenerator(Choices())

match(rObj_ChosenSite[1]):
    case "Webster":
        print("Run Webster Function")
    case "Oxford":
        print("Run Oxford Function")
    case "Dictionary.com":
        print("Run Dictionary.com Function")
    case _: 
        raise Exception("[Err] Default case")



#print out all the choices the user can choose 








#Need a regular expression to only parse the word between > < When > is found and
#matches stop after meet <
#print(str(word_of_the_day_Webster[0]))




#r_webster_WOTD_page = requests.get("https://www.merriam-webster.com/dictionary/" + word_of_the_day_Webster)
#soup_webster_WOTD_decoded = BeautifulSoup(r_webster_WOTD_page.text, "html5lib") 

#
#print(soup_webster_WOTD_decoded.findAll("span", "dtText"))