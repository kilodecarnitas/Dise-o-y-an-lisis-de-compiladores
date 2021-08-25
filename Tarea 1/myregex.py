# Aldo Fernando Ortiz Mejía - A01654735

import re

def email(str):
    if re.search("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", str):
        return True
    else:
        return False

def phone_number(str):
    if re.search("(\+[0-9]{1-3}[\s]*\([0-9]{1,3}\)[\s]*)*[\s]*[0-9]{2,3}[\s]*[0-9]{4}[\s]*[0-9]{4}",str):
        return True
    else:
        return False

def hexadecimal(str):
    if re.search("^(0x(?=0*[1-9a-fA-F]0*)[0-9a-fA-F]{8}$)",str):
        return True
    else:
        return False