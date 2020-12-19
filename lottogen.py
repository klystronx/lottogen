class LottoGenerator:
    def __init__(self):
        winningNumbers = 0
    def generate_lotto_numbers(self, count, startRange, endRange):
        import random

        winningNumbers = []
        for i in range(count):
            winningNumbers.append(random.SystemRandom().randint(startRange, endRange + 1))
        return winningNumbers

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

gen = LottoGenerator()
myCalc = Calculator()
totalPlays = 0
print()
while True:
    totalPlays += 1
    matchedNumbers = 0
    myNumbers = gen.generate_lotto_numbers(6,1,54)
    lottoNumbers = gen.generate_lotto_numbers(6,1,54)
    for i in range(len(myNumbers)):
        if myNumbers[i] in lottoNumbers:
            matchedNumbers += 1
   
    myCalc.calculatewin(matchedNumbers)

    print('Played: %s | Matched: %s | Winnings: %s | Spent: %s | Balance: %s' % (totalPlays,
                                                                                 matchedNumbers,
                                                                                str(myCalc.totalWinnings),
                                                                                str(myCalc.totalSpent),
                                                                                str(myCalc.balance)),
                                                                                end='\r')
    if matchedNumbers == 6:
        print('\n BOOM! HIT THE LOTTERY!!')
        print(myNumbers)
        print(lottoNumbers)
        break    