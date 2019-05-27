"""
UwU CIT is so fun! 
OwO CIT instructors are the best!
"""
import funct

UwU = 'UwU means unhappy without you.'
OwO = 'Not UwU.'
XD = 'old face lmao'

player = {
    "fname": '',
    "lname": '',
    "age": '',
    "gender": '',
    "personality": '',
    "term1grades": {
        "acit1420": '',
        "acit1515": '',
        "acit1620": '',
        "acit1630": '',
        "comm1116": '',
        "math1310": '',
        "orgb1100": '',
    }
}

player['fname'] = funct.getfname()
player['lname'] = funct.getlname()
player['age'] = funct.getage()
player['gender'] = funct.getgender()
player['personality'] = funct.getpersonality()

print(player)