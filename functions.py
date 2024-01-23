from datetime import datetime
import random, string, barnum


def createNameAsString(type: int):  # 1 for first name, 2 for last name, 3 for full name
    if type == 1:
        name = ""
        name += barnum.create_name()[0]
        return name
    elif type == 2:
        name = ""
        name += barnum.create_name()[1]
        return name
    elif type == 3:
        name = ""
        name += barnum.create_name()[0] + " "
        name += barnum.create_name()[1]
        return name
