import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def return_Value_From_Dictionarie(dict_Key):

    dict_Key.lower()

    if dict_Key in data:
        return data[dict_Key]
    elif dict_Key.title() in data:
        return data[dict_Key.title()]
    elif dict_Key.upper() in data:
        return data[dict_Key.upper()]
    elif len(get_close_matches(dict_Key, data.keys(), cutoff = 0.8)) > 0:

        temp_Word = get_close_matches(dict_Key, data.keys(), cutoff = 0.8)[0]
        print ("Did you mean %s instead? " % temp_Word)
        temp_Input = input("Type 'y' for yes or 'n' for no... ").lower()

        if temp_Input == "y":
            return return_Value_From_Dictionarie(temp_Word)
        else:
            return "Restarting Program"

    else:
        return "Sorry that word is not on the dictionary, please check the spelling of the desired word "


while True:

    user_Input = input("Type a word to get its definition or type '/end' to end the program... \n").lower()
    
    if user_Input != "/end":
        output = return_Value_From_Dictionarie(user_Input)
        
        if type(output) == list:
            for definition in output:
                print(definition)
        else:
            print(definition)
    
        continue
    else:
        break