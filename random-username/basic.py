# Basic Python Script to generate random username based on user's firstname and lastname  

import random 
import json

firstname_limit = json.load(open("config.json"))["firstname_limit"] 
lastname_limit = json.load(open("config.json"))["lastname_limit"] 
username_limit = json.load(open("config.json"))["username_limit"] 
username_end_type = json.load(open("config.json"))["username_fill_with"]   # diigits, chars, mix

def get_random_username(firstname, lastname):
    
    if len(firstname) >= firstname_limit:
        firstname = firstname[:firstname_limit].lower()
    else:
        firstname = firstname.lower()

    if len(lastname) >= lastname_limit:
        lastname = lastname[:lastname_limit].lower()
    else:
        lastname = lastname.lower() 
    
    digits = "1234567890"
    chars= "abcdefghijklmnopqrstuvwxyz"
    mix = chars + digits

    ch1  = json.load(open("config.json"))["chars_should_remain_firtname"] 
    ch2  = json.load(open("config.json"))["chars_should_remain_lastname"]

    short_firstname = firstname[:ch1]
    short_lastname = lastname[:ch2]
    extra_chars = username_limit - len(short_firstname + short_lastname)

    if username_limit <= 32 and username_limit >= 6 and username_end_type in ["digits", "chars", "mix"]:
        generated_random = []
        for i in range(extra_chars):
            if username_end_type == "digits":
                adding = random.choice(digits)
                generated_random.append(adding)
            elif username_end_type == "chars":
                adding = random.choice(chars)
                generated_random.append(adding)
            elif username_end_type == "mix":
                adding = random.choice(mix)
                generated_random.append(adding)
            else:
                print("Having some ghost error, ops!")     
        username = short_firstname + short_lastname + "".join(generated_random)
    else:
        username = "Error"
    return username 
