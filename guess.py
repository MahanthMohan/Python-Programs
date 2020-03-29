max = 1000
actual = 125
guess = 500

def Guess(guess):
    if guess != actual:
        print(guess)
        if guess > actual:
            isHigh = True
            guess = guess - guess/2
            Guess(int(guess))   
        else:
            isHigh = False
            guess = guess + guess/2
            Guess(int(guess))
        guessAgain(guess,isHigh)
    else:
        return True
    

def guessAgain(guess, isHigh):
    if isHigh:
        ret = guess - (guess/2)
    else:
        ret = guess + (guess/2)
    Guess(ret)

print(Guess(guess))