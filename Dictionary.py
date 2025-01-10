from bs4 import BeautifulSoup
import main
import requests
import re 
import time

def dictionary_WOTD(r_obj:requests.Response):
    ''' Soup to decode -> Reg Expression + Soup to find attributes with WOTD
        -> Jump to proper page to extract rest of the info.'''    
    dictionary_Soup = BeautifulSoup(r_obj.text, "html5lib")

    curr_date = time.ctime(time.time())
    spliced_curr_date:str = curr_date[4:10]
    print(spliced_curr_date)

    print("Debugging to find stuff")
    def dictionary_main():
        print("list of attributes \n ====")
        print(type(dictionary_Soup.find(attrs={"data-date": {spliced_curr_date}}).attrs))
        Parent_Container = dictionary_Soup.find(attrs={"data-date": {spliced_curr_date}})
        #attrs = dic
        wotd = Parent_Container.attrs['data-title']

        #Access class_="otd-item-wrapper-content" child of Parent_container 1 down
        # Then access child of wrapper, class=_"wotd-item" 2 down 
        # class="otd-item-headword"
        # then access class="otd-item-headword__pos-blocks" for adjective and def 3 down
        # then class="otd-item-headword__pos" 
            # then childs for that for more info
        #finding descendants is recursive
        #Need to match otd-item-headword_pos class thing in 
        #find all works way down the tree
        # Need to strip off whitespace man
        wordtype_and_def_as_list = Parent_Container.find(class_="otd-item-headword__pos").text.split()
        Word_type = wordtype_and_def_as_list[:1]
        wotd_brief_definition = wordtype_and_def_as_list[1:]
        Word_type = ' '.join(Word_type)
        wotd_brief_definition =' '.join(wotd_brief_definition)

        
        return wotd, Word_type, wotd_brief_definition
    
    wotd = dictionary_main()
    
    def dictionary_offical_entry_request():
        time.sleep(1)
        main.request_connection_Execptions(f"https://www.dictionary.com/browse/{wotd}")
    

    main.wotd_display(name = wotd[0],
                 word_type = wotd[1],
                 syllabes = "no",
                 definition = wotd[2],
                 examples = "swag",
                 link = f"yea")    