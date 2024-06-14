from bs4 import BeautifulSoup
import re
import requests
import Webster
#All of this will get refactored eventually I swear
#need to solve circular import

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

def cull_tags(soup_string: str):
    # Extracting text w/o tags
    clean_text = soup_string.get_text(separator=' ',strip=True)
    clean_text = re.sub(r'//', '', clean_text)
    return clean_text        

def wotd_info(name:BeautifulSoup, word_type:BeautifulSoup, syllabes:BeautifulSoup, definition:BeautifulSoup,
              example:BeautifulSoup):
    wotd_info = {
        'name': name,
        'word type': word_type,
        'syllabes': syllabes,
        'definition': definition,
        'example': example,
}
    print(f"""
          Name of WOTD: {wotd_info['name']}
          Word type: {wotd_info['word type']}
          Syllabes: {wotd_info['syllabes']} 
          Definition: {wotd_info['definition']}
          Example: {cull_tags(wotd_info['example'])}
          """
          )



#main
def main(): 
    #rObj_ChosenSite[1](Tuple) for specific site 
    rObj_ChosenSite = siteResponseObjGenerator(Choices())

    match(rObj_ChosenSite[1]):
        case "Webster":
            print("Run Webster Function")
            Webster.webster_WOTD(rObj_ChosenSite[0])
        case "Oxford":
            print("Run Oxford Function")
        case "Dictionary.com":
            print("Run Dictionary.com Function")
        case _: 
            raise Exception("[Err] Default case was reached.")

if __name__ == '__main__':
    main()