from bs4 import BeautifulSoup
import re
import requests
import Webster


''' 
To-Do

Solve
    Circular import
    Printing out choices and error checking

Feature
    Allowing someone to check the word of the days for any day of any year
        Using their word of the day Calender 
    OR
    Make a random function where you hit random word and it will fetch a random word for you.
    
    Click on a word and hyperlinks to webster dictionary

'''

def Choices():
    print("Please select one of the following sites to know the word of the day of:")
    print("[] Webster Dictionary | A ")
    print("[] Oxford Dictionary | B ")
    print("[] Dictionary.com | C ")
    print("DEBUG: Testing failed requests | F")
    
    valid_choices = {'A', 'B', 'C', 'F'}

    while True:
        choice = input("Enter letter corresponding to site: ").strip().upper()
        
        if choice in valid_choices:
            print(f"You selected option {choice}.")
            return choice  
        else:
            print("Invalid input. Please enter either A, B, C, F")


def request_connection_Execptions(x:str):
    '''Simple try catch when making connections. Might show more execeptions later'''
    try:
        ok_requestObj = requests.get(x, timeout=5)
        return ok_requestObj
    except requests.exceptions.RequestException as e:
        raise Exception(e) 
    

def siteResponseObjGenerator(choice:chr):
        match choice:
            case 'A': 
                print("[x] Webster Dictionary | A\n")
                print("Creating Webster Object...")
                r_webster = request_connection_Execptions("https://www.merriam-webster.com/word-of-the-day")
                return r_webster, "Webster"
            case 'B': 
                print("[x] Oxford Dictionary")
                print("Creating Oxford Object...")
                r_Oxford = request_connection_Execptions("https://www.oed.com/")
                return r_Oxford, "Oxford"
            case 'C':
                print("[x] Dictionary.com | C ")
                print("Creating Dictionary  Object...")
                r_Dictionary = request_connection_Execptions("https://www.dictionary.com/e/word-of-the-day/")
                return r_Dictionary, "Dictionary"
            case 'F':
                print("[DEBUG] Testing connection exceptions...")
                r_Debug_F = request_connection_Execptions("lol")
                return r_Debug_F, "This should output an error"

#This is completely unneeded because the .text method
'''
def cull_tags(soup_string: str):
    # Extracting text w/o tags
    clean_text = soup_string.get_text(separator=' ',strip=True)
    clean_text = re.sub(r'//', '', clean_text)
    return clean_text.strip()     
'''


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
          Example: {(wotd_info['example'])}
          """
          )



#main
def main(): 
    #rObj_ChosenSite[1](Tuple) for specific site 
    rObj_ChosenSite = siteResponseObjGenerator(Choices())
    

    match(rObj_ChosenSite[1]):
        case "Webster":
            print("Running Webster Function")
            Webster.webster_WOTD(rObj_ChosenSite[0])
        case "Oxford":
            print("Run Oxford Function")
        case "Dictionary.com":
            print("Run Dictionary.com Function")
        case _: 
            print("[Main - Default case] Error with sitegenerator return  \n")
            


if __name__ == '__main__':
    main()