class LottoGenerator:
    def __init__(self):
        winningNumbers = 0
    def generate_lotto_draw(self, count, startRange, endRange):
        import random
        #FIX THIS CRAP-STILL GENERATES REPEATING NUMBERS
        drawNumbers = [None] * count
        for i in range(count):
            drawNumbers[i] = random.SystemRandom().randint(startRange, endRange + 1)
            # if drawNumbers[i] in drawNumbers:
            while drawNumbers[i] not in drawNumbers:
                drawNumbers[i] = random.SystemRandom().randint(startRange, endRange + 1)
        return drawNumbers

class Calculator:
    numberMatched = 0
    payouts = [0,0,0,3,55,2046,40500000]
    balance = 0
    totalWinnings = 0
    totalSpent = 0
    def __init_(self):
        pass
    def calculatewin(self,numbersMatched):
        self.balance -= 1
        self.totalSpent += 1
        self.totalWinnings = self.totalWinnings + self.payouts[numbersMatched]
        self.balance = self.balance + self.payouts[numbersMatched]
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

gen = LottoGenerator()
myCalc = Calculator()
totalPlays = 0
matchedBalls = [0,0,0,0,0,0,0]
print()
while True:
    totalPlays += 1
    matchedNumbers = 0
    myNumbers = gen.generate_lotto_draw(6,1,54)
    lottoNumbers = gen.generate_lotto_draw(6,1,54)

    matchedNumbers = len(set(myNumbers).intersection(lottoNumbers))
   
    myCalc.calculatewin(matchedNumbers)
    matchedBalls[matchedNumbers] += 1
    
    x = input()
    print(myNumbers)
    print(lottoNumbers)
    
    if totalPlays % 10000 == 0:
        os.system('clear')
        print('Played: %s | Years: %s | Winnings: %s | Spent: %s | Balance: %s' % (totalPlays,
                                                                                    int(totalPlays/520),
                                                                                    str(myCalc.totalWinnings),
                                                                                    str(myCalc.totalSpent),
                                                                                    str(myCalc.balance)))

        print(matchedBalls)

    if matchedNumbers == 6:
        print('\n BOOM! HIT THE LOTTERY!!')
        print(myNumbers)
        print(lottoNumbers)
        break