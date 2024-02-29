# Basic Python Script to generate random username based on user's firstname and lastname  

import random 

firstname_limit = 10
lastname_limit = 10
username_limit = 10 # Max Limit: 16, Min Limit: 10 ;
username_end_type = "chars" # "digits", "chars", "mix" 

def get_random_name(firstname, lastname):
    
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

    short_firstname = firstname[:4]
    short_lastname = lastname[:4]
    extra_chars = username_limit - len(short_firstname + short_lastname)

    if username_limit <= 16 and username_limit >= 10:
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
        
        # Paste you code here if you want to make it automatic to the database :)) #

        print(f"Username: {username}") # Remove this if you have connected to a database
    else:
        print("Username limit is not valid")


if __name__ == "__main__":
   firstname = input("Enter your firstname: ")
   lastname = input("Enter your lastname: ")
   get_random_name(firstname=firstname, lastname=lastname)

    
    
