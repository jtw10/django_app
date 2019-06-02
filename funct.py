def getfname():
    x = input('What is your first name?: ')
    return x

def getlname():
    x = input('What is your last name?: ')
    return x

def getage():
    while True:
        try:
            x = int(input('How old are you? (Enter an integer): '))
            return x
        except:
            print('Please enter your age as a number: ')
            continue

def getgender():
    while True:
        try:
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
                raise ValueError
        except ValueError:
            print('Enter 1 for male, 2 for female, or 3 for undecided: ')
            continue

def getpersonality():
    score = []
    personality = ''
    print('Choose the answer that best describes how you would feel or act if you were in that situation.')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=')
    def q1():
        ans = ''
        print('If my instructor gives me 70 percent on a quiz, I would think...')
        print('A. \'That is good enough\'')
        print('B. \'The instructor is bad\'')
        print('C. \'I need to work harder\'')
        print('D. \'I just want to pass\'')
        while True: 
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 2
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 0
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 1
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue
    def q2():
        ans = ''
        print('If my instructor is a feminist and my group name is \'Macho Men\'...')
        print('A. Stick with it. Nobody is my boss.')
        print('B. Why should I care, it\'s my group!')
        print('C. Change my group name to something drastically different and promote inclusivity.')
        print('D. Leave it up to my group to make appropriate changes.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 0
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 0
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 3
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue 
    def q3():
        ans = ''
        print('If my classmates are cheating and talking during midterms...')
        print('A. I would tell everyone that it is okay to talk loudly during midterms. Everyone should know the truth.')
        print('B. I would instruct the instructor to watch the cheater.')
        print('C. I would write a program to cheat for me.')
        print('D. I would cheat the same way because instructors clearly don\'t care.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 2
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 3
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 0
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue
    def q4():
        ans = '' 
        print('If someone in my group did nothing and it is peer review time...')
        print('A. I would give everyone perfect.')
        print('B. I would not put their name on the peer review.')
        print('C. I would mark everyone objectively and fairly.')
        print('D. I would give everyone low marks and complain to my instructor.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 2
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 3
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 1
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue 
    def q5():
        ans = ''
        print('If I am not enjoying a class and I feel it is useless...')
        print('A. I would ask why I should learn it, since the class is useless.')
        print('B. I would not do anything and hope my instructor helps me pass.')
        print('C. I would still try my hardest because I need to get perfect marks in everything.')
        print('D. I would only do the bare minimum.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 2
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 1
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 2
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue
    def q6():
        ans = '' 
        print('This best describes how I will spend my lunch breaks:')
        print('A. I will do homework.')
        print('B. I will bring my own lunch and play video games.')
        print('C. I will visit the instructor\'s office hours and try to get the best marks.')
        print('D. I will go out with friends and I will usually eat too much.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 3
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 1
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 0
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue 
    def q7():
        ans = ''
        print('During exam week:')
        print('A. I show up 5-30 minutes late because why should I show up on time?')
        print('B. I show up 10 minutes early just in case something unexpected happens.')
        print('C. I study all night and get to school 2 hours early.')
        print('D. I study enough to do decently well, except in classes that I feel are useless.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 0
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 2
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 1
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue 
    def q8():
        ans = ''
        print('If someone says or does something I disagree with...')
        print('A. I will ostracize them and never interact with them again.')
        print('B. I would tell everyone how stupid this person is.')
        print('C. I would pretend to like them because I want my classmates to think that I am a nice person who believes in inclusivity.')
        print('D. I try and understand their point of view. Everyone has their own streghts and weaknesses.')
        while True:
            try:
                ans = str(input('Enter A, B, C, OR D: '))
                if ans.lower() == 'a':
                    ans = 1
                    score.append(ans)
                    break
                elif ans.lower() == 'b':
                    ans = 4
                    score.append(ans)
                    break
                elif ans.lower() == 'c':
                    ans = 1
                    score.append(ans)
                    break
                elif ans.lower() == 'd':
                    ans = 3
                    score.append(ans)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("A, B, C, or D only please.")
                continue
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    total = sum(score)
    if total < 10:
        personality = 'Brilliant'
    if 10 <= total <= 14:
        personality = 'Super Confident'
    if 15 <= total <= 19:
        personality = 'Carefree'
    if 20 <= total <= 24:
        personality = 'Resourceful'
    if 25 <= total <= 27:
        personality = 'Hardworking'
    if 28 <= total <= 30:
        personality = 'Studious'
    if 31 <= total <= 32:
        personality = 'Keener'
    if total > 32:
        personality = 'Mysterious'
    return personality
