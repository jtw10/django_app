def getfname():
    x = input('What is your first name?: ')
    return x

def getlname():
    x = input('What is your last name?: ')
    return x

def getage():
    x = int(input('How old are you? (Enter an integer): '))
    if type(x) != int:
        getage()
    else:
        return x

def getgender():
    x = int(input('What do you identify as? Enter 1 for male, 2 for female, or 3 for undecided: '))
    if x == 1:
        gender = 'male'
        return gender
    elif x == 2:
        gender = 'female'
        return gender
    elif x == 3:
        gender = 'undecided'
        return gender
    else:
        print('Enter 1 for male, 2 for female, or 3 for undecided: ')
        getgender()


def getpersonality():
    personality = ''
    print('Choose the answer that best describes how you would feel or act if you were in that situation.')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=')
    print('If my instructor gives me 70 percent on a quiz, I would think...')
    print('A. \'That is good enough\'')
    print('B. \'The instructor is bad\'')
    print('C. \'I need to work harder\'')
    print('D. \'I just want to pass\'')
    q1 = input('Enter A, B, C, OR D: ')
    print('If my instructor is a feminist and my group name is \'Macho Men\'...')
    print('A. Stick with it. Nobody is my boss.')
    print('B. Why should I care, it\'s my group!')
    print('C. Change my group name to something drastically different.')
    print('D. Leave it up to my group to make appropriate changes.')
    q2 = input('Enter A, B, C, OR D: ')
    print('If my classmates are cheating and talking during midterms...')
    print('A. I would tell everyone that it is okay to talk loudly during midterms. The world has to right to know the truth.')
    print('B. I would instruct the instructor to watch the cheater.')
    print('C. I would write a program to cheat for me.')
    print('D. I would cheat the same way because instructors clearly don\'t care.')
    q3 = input('Enter A, B, C, OR D: ')
    print('If someone in my group did nothing and it is peer review time...')
    print('A. I would give everyone perfect.')
    print('B. I would not put their name on the peer review.')
    print('C. I would mark everyone objectively and fairly.')
    print('D. I would give everyone low marks and complain to my instructor.')
    q4 = input('Enter A, B, C, OR D: ')
    print('If I am not enjoying a class and I feel it is useless...')
    print('A. I would ask why I should learn it, since the class is useless.')
    print('B. I would not do anything and hope my instructor helps me pass.')
    print('C. I would still try my hardest because I need to get perfect marks in everything.')
    print('D. I would only do the bare minimum.')
    q5 = input('Enter A, B, C, OR D: ')
    print('This best describes how I will spend my lunch breaks:')
    print('A. I will do homework.')
    print('B. I will bring my own lunch and play video games.')
    print('C. I will visit the instructor\'s office hours and try to get the best marks.')
    print('D. I will go out with friends and I will usually eat too much.')
    q6 = input('Enter A, B, C, OR D: ')
    print('During exam week:')
    print('A. I show up 5 minutes late because why should I show up on time?')
    print('B. I show up 10 minutes early just in case something unexpected happens.')
    print('C. I study all night and get to school 2 hours early.')
    print('D. I study enough to do decently well, except in classes that I feel are useless.')
    q7 = input('Enter A, B, C, OR D: ')
    print('If someone says or does something I disagree with...')
    print('A. I will ostracize them and never interact with them again.')
    print('B. I would tell everyone how stupid this person is.')
    print('C. I would pretend to like them because I want my classmates to think that I am a nice person who believes in inclusivity.')
    print('D. I try and understand their point of view. Everyone has their own streghts and weaknesses.')
    q8 = input('Enter A, B, C, OR D: ')
    return personality





