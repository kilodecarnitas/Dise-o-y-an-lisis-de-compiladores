import re

def email(str):
    if re.search("\b[0-9A-F]+\b", str):
        print("True")
    else:
        print("False")

# ^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$
email("hexadecimal")