import random

def instructions():
    print("""
************
INSTRUCTIONS
************

You will be asked for a 4-digit number,
and then told how many cows and how many bulls you have.

A cow is a correct number in the wrong place.

A bull is a correct number in the right place,

""")

def numberGenerator():#generates a random 4-digit number with no recurring numbers
    global number
    numbers=['0','1','2','3','4','5','6','7','8','9']
    newNumber=[]
    loop=0
    while loop!=4:
        availableNum=len(numbers)-1
        generator=random.randint(0,availableNum)
        newDigit=numbers[(generator)]
        newNumber.append(newDigit)
        numbers.remove(newDigit)
        loop=loop+1
    number=newNumber[0]+newNumber[1]+newNumber[2]+newNumber[3]

def lengthCheck(guess):#checks guess is length 4
    global correct
    length=len(guess)
    if length!=4:
        print('Guess needs to be 4 numbers long')
    else:
        correct=True
    
def numberCheck(guess):#checks guess consists of only digits
    global correct
    check=guess.isdigit()
    if check==False:
        print('Guess needs to consist of only numbers')
    else:
        correct=True

def repeatCheck(guess):#checks guess has no recurring digits
    global correct
    guessList=[]
    for i in guess:
        guessList.append(i)
    x=True
    loop1=-1#these variables keep the for loops from checking a number against 
    loop2=-1#itself and using incorrect information
    for i in guessList:
        loop1=loop1+1
        loop2=-1
        ipos=guessList.index(i)
        for n in guessList:
            loop2=loop2+1
            npos=guessList.index(n)
            if ipos==npos and loop1!=loop2:
                x=False
    if x==False:
        print('Guess cant have any repeated digits')
    else:
        correct=True

def validGuess(guess):#function runs all 3 checks through if statements
    global correct
    global valid
    correct=False
    lengthCheck(guess)
    if correct==True:
        correct=False
        numberCheck(guess)
        if correct==True:
            correct=False
            repeatCheck(guess)
            if correct==True:
                valid=True#if all checks are succesful, valid is used to leave check loop
    

def comparison(guess,number):#compares number and guess, returns cows and bulls and success
    #creates lists of characters in guess and number to be compared
    guessList=[]
    for i in guess:
        guessList.append(i)
    numberList=[]
    for n in number:
        numberList.append(n)

    bulls=0
    cows=0
    for i in guessList:#loops for each character in guess
        ipos=guessList.index(i)#variable for position for bulls
        for n in numberList:#nested loop to compare each character in number
                            #against each character in guess
            npos=numberList.index(n)
            if i==n:#checks for match (definitely at least a cow)
                if ipos==npos:#bull if both characters match and have same position
                    bulls+=1
                else:#cow if they match but not with position
                    cows+=1
                    

   #prints cows and bulls
    print('Cows: '+str(cows)+', ''Bulls: '+str(bulls)+'.')

    if bulls==4:
        print('You guessed the number!')
        global success
        success=True

def restart():
    print("To play again, press \'Y\' or to exit, press \'N\'")
    valid=False
    
    while valid==False:
        answer=input('Enter Y/N: ')
        if (answer.lower()=='y') or (answer.lower()=='n'):
            valid=True
        else:
            print('Please enter Y or N')
            
    if answer.lower()=='y':
        retry=True
    else:
        retry=False

    return retry

#main program
print('''
**************
*COWS & BULLS*
**************
''')#title

game=True
while game==True:
    instructions()
    numberGenerator()#generates a random 4-digit number
    counter=0#turn counter
    success=False#used for when user guesses correctly
    leaving=False#used for if the user enters 'exit'
    while success==False and leaving==False:#while not guessed number
        valid=False#resets check
        while valid==False:#repeats checks until guess is acceptable
            guess=input('Enter a 4-digit number, or enter \'exit\' to end game: ')
            if guess.lower()=='exit':
                valid=True
                leaving=True
            else:
                validGuess(guess)#runs 3 checks
        if leaving==True:
            break
        counter=counter+1#counter
        comparison(guess,number)#comparison for bulls, cows and winning the game
    if success==True:#separates users who entered exit and users who won
        print('You took '+str(counter)+' turns.')
    game=restart()
input('Press any key to end')#catcher
