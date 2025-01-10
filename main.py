from bs4 import BeautifulSoup
import re
import requests
import Webster
import Dictionary


#Choices rn is for debug. On startup,
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

def request_connection_Execptions(x_no_delay:str):
    try:
        requestObj = requests.get(x_no_delay, timeout=5)
        requestObj.raise_for_status()
        print("Successfully requested for content and")
        return requestObj
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failure requesting content from webpage {e}")
    
def siteResponseObjGenerator(choice:chr):
        match choice:
            case 'A': 
                print("[x] Webster Dictionary | A\n")
                print("Creating Webster Object...")
                r_webster = request_connection_Execptions("https://www.merriam-webster.com/word-of-the-day")
                return r_webster, "Webster"
            case 'B': 
                print("[x] Oxford Dictionary | B ")
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


#Where this is outputted on screen needs to have a link to the full entry on webster with pronuncation and shit.
def wotd_display(name:str, word_type:str, syllabes:str, definition:str,
              examples:list[str], link:str):
    wotd_info = {
        'name': name,
        'word type': word_type,
        'syllabes': syllabes,
        'definition': definition,
        'examples': examples,
        'link': link
}
    print(f"""
          Name of WOTD: {wotd_info['name']}
          Word type: {wotd_info['word type']}
          Syllabes: {wotd_info['syllabes']} 
          Definition: {wotd_info['definition']}
          Examples: {(wotd_info['examples'])}
          Link: {(wotd_info['link'])}
          """
          )


def main(): 
    #rObj_ChosenSite[1](Tuple) for specific site 
    rObj_ChosenSite = siteResponseObjGenerator(Choices())
    

    match(rObj_ChosenSite[1]):
        case "Webster":
            print("Running Webster Function")
            Webster.webster_WOTD(rObj_ChosenSite[0])
        case "Oxford":
            print("Run Oxford Function")
        case "Dictionary":
            print("Running Dictionary.com Function")
            Dictionary.dictionary_WOTD(rObj_ChosenSite[0])
        case _: 
            print("[Main - Default case] Error with sitegenerator return  \n")
            


if __name__ == '__main__':
    main()