"""Projeto nº1 do HackerSchool (Slot Machine)
O projeto é uma classe player com métodos para jogar uma slot machine.

Miguel Fernandes _ nº estudante: 103573 _ Data da última alteração: 21/10/2022
email: miguel.e.fernandes@tecnico.ulisboa.pt

"""

from random import randint

class Player:
    """ Initializes the player with his starting credits """
    def __init__(self, totalCredits):
        self.totalCredits = totalCredits
        self.ReactionStringList = [""]*16
        
    """ Asks for bet amount until a valid amount is given """
    def getBet(self):
        while self.totalCredits < (bet := int(input("How many cwedits do you w-want t-to bet?!?1 "))):
            print(f'You don\'t that many cwedits. Twy something w-wower than {self.totalCredits}')
        self.totalCredits -= bet
        self.bet = bet
    
    """ Selects a random symbol, chosen with probability """
    def spinSymbol(self):
        num = randint(0, 155)
        if num in range(0, 50):         # 50/156
            return 'Δ'
        elif num in range(50, 90):      # 40/156
            return '$'
        elif num in range(90, 120):     # 30/156
            return '%'
        elif num in range(120, 140):    # 20/156
            return '&'
        elif num in range(140,150):     # 10/156
            return '@'
        elif num in range(150, 155):    # 5/156
            return '£'
        else:
            return '€'                  # 1/156
    
    
    def setLosingReactionString(self):
        self.ReactionStringList[0] = " "*5 + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠐⠒⠶⠶⠒⢂⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[1] = " "*5 + "⠀⠀⠀⠀⠀⢀⣠⡶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁⠶⣄⠀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[2] = " "*5 + "⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀\n"
        self.ReactionStringList[3] = " "*5 + "⠀⠀⣰⠟⠁⠀⠀⣀⠤⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⢗⠢⢀⠀⠀⠈⢹⣄⠀⠀\n"
        self.ReactionStringList[4] = " "*5 + "⠀⣰⠏⠀⠀⠀⢀⣀⣬⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⣀⠀⠀⠀⢻⣆⠀\n"
        self.ReactionStringList[5] = " "*5 + "⢠⡿⠀⢀⣤⠞⠉⠀⠈⠙⣿⣿⣦⠀⠀⠀⠀⡴⠚⠉⠀⠈⠻⣿⣷⣄⠀⠀⣿⡀\n"
        self.ReactionStringList[6] = " "*5 + "⣼⡇⢀⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣧⢃⢠⣿⡃⠀⠀⠀⠀⢀⣿⣿⣿⡇⠄⢨⡷\n"
        self.ReactionStringList[7] = " "*5 + "⣿⡇⢠⢸⣷⣄⣀⣀⣤⣾⣿⣿⣿⣿⢘⠀⢿⣧⣄⣀⣀⣴⣿⢿⣿⣿⡇⢰⢈⡟\n"
        self.ReactionStringList[8] = " "*5 + "⢻⡇⠘⡈⢿⣿⣿⣿⣿⣧⣠⣿⡿⠃⡜⢰⠘⢿⣿⣿⣿⣿⣧⣠⣿⡿⠁⡎⣸⡇\n"
        self.ReactionStringList[9] = " "*5 + "⠈⣷⡀⠐⠀⠙⠻⠿⠿⠿⠿⠋⢁⠔⠁⠀⠑⣈⠙⠻⠿⠿⠿⠿⠋⢀⠜⢀⡿⠀\n"
        self.ReactionStringList[10] = " "*5+ "⠀⠙⣇⡀⠀⠁⠒⠠⠤⠤⠔⠚⠁⣀⣀⣀⣀⠀⠑⠒⠤⠤⠤⠐⠊⠁⢀⣾⠁⠀\n"
        self.ReactionStringList[11] = " "*5+ "⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀\n"
        self.ReactionStringList[12] = " "*5+ "⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠀⠀⠀⠀\n"
        self.ReactionStringList[13] = " "*5+ "⠀⠀⠀⠀⠀⠀⠈⠓⠶⣆⣠⡀⣀⣀⡀⢀⣀⣀⣀⣤⡴⠶⠛⠁⠀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[14] = " "*5+ "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠋⠙⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[15] = "Oh nyo?!?! You didn't *sweats* win anything :("
    
    
    def setWinningReactionString(self, valueWon):
        self.ReactionStringList[0] = " "*5 + "\n"
        self.ReactionStringList[1] = " "*5 + "\n"
        self.ReactionStringList[2] = " "*5 + "⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠶⠶⠒⠲⠦⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[3] = " "*5 + "⠀⠀⠀⠀⢀⡠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠲⠤⣄⡀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[4] = " "*5 + "⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡿⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[5] = " "*5 + "⠀⢾⣅⡀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢀⡦⠤⠄⠀⠀⢻⡀⠀⠀⠀⠀⠀\n"
        self.ReactionStringList[6] = " "*5 + "⠀⠈⢹⡏⠀⠀⠐⠋⠉⠁⠀⠻⢿⠟⠁⠀⠀⢤⠀⠀⠠⠤⢷⣤⣤⢤⡄⠀\n"
        self.ReactionStringList[7] = " "*5 + "⠀⠀⣼⡤⠤⠀⠀⠘⣆⡀⠀⣀⡼⠦⣄⣀⡤⠊⠀⠀⠀⠤⣼⠟⠀⠀⢹⡂\n"
        self.ReactionStringList[8] = " "*5 + "⠀⠊⣿⡠⠆⠀⠀⠀⠈⠉⠉⠙⠤⠤⠋⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⡼⠁\n"
        self.ReactionStringList[9] = " "*5 + "⠀⢀⡾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠁⠀⠀⠀⣸⠁⠀\n"
        self.ReactionStringList[10] = " "*5 + "⠀⠀⠀⡼⠙⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀\n"
        self.ReactionStringList[11] = " "*5 + "⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀\n"
        self.ReactionStringList[12] = " "*5 + "⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀\n"
        self.ReactionStringList[13] = " "*5 + "⣾⠁⠀⢀⣠⡴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀\n"
        self.ReactionStringList[14] = " "*5 + "⠈⠛⠻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀\n"
        self.ReactionStringList[15] = "You won " + str(valueWon) + " cwedits!! :O"
    

    def printSlotMachine(self, symbols):
        print("\n"+  
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿" + self.ReactionStringList[0] +
            "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿" + self.ReactionStringList[1] +
            "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿" + self.ReactionStringList[2] +
            "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿" + self.ReactionStringList[3] +
            "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿" + self.ReactionStringList[4] +
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[5] +
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[6] +
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[7] +
            "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿" + self.ReactionStringList[8] +
            "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿" + self.ReactionStringList[9] +
            "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿" + self.ReactionStringList[10] +
            "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿" + self.ReactionStringList[11] +
            "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿" + self.ReactionStringList[12] +
            "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿" + self.ReactionStringList[13] +
            "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿" + self.ReactionStringList[14] +
            self.ReactionStringList[15]
            )
        
        
    """ Selects the won amount and adds it to the total credits """
    def getWinnings(self, symbols):
        if (symbols == symbols[0]*3):
            if symbols[0] == 'Δ':
                valueWon = self.bet * 5
            elif symbols[0] == '$':
                valueWon = self.bet * 10
            elif symbols[0] == '%':
                valueWon = self.bet * 20
            elif symbols[0] == '&':
                valueWon = self.bet * 70
            elif symbols[0] == '@':
                valueWon = self.bet * 200
            elif symbols[0] == '£':
                valueWon = self.bet * 1000
            else:
                valueWon = self.bet * 1000000
            self.totalCredits += valueWon
            self.setWinningReactionString(valueWon)
            #print(f'You won {valueWon} cwedits!! :O')
        else:
            self.setLosingReactionString()
            #print("Oh nyo?!?! You didn't *sweats* win anything :(")
    
    """ Plays a whole round of the Slot Machine"""
    def playRound(self):
        self.getBet()
        symbols = ""
        for i in range(0,3):
            symbols += self.spinSymbol()
        self.getWinnings(symbols)
        self.printSlotMachine(symbols)
"""      print(  "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿" + self.ReactionStringList[0] +
                "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿" + self.ReactionStringList[1] +
                "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿" + self.ReactionStringList[2] +
                "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿" + self.ReactionStringList[3] +
                "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿" + self.ReactionStringList[4] +
                "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[5] +
                "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[6] +
                "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{a}{a}⢸⡇{b}{b}⢸⡇{c}{c}⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿".format(a = symbols[0], b = symbols[1], c = symbols[2]) + self.ReactionStringList[7] +
                "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿" + self.ReactionStringList[8] +
                "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿" + self.ReactionStringList[9] +
                "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿" + self.ReactionStringList[10] +
                "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿" + self.ReactionStringList[11] +
                "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿" + self.ReactionStringList[12] +
                "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿" + self.ReactionStringList[13] +
                "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿" + self.ReactionStringList[14])
"""
        

""" Prints the Arcade's logo """
print("\n $$\\   $$\\               $$\\   $$\\        $$$$$$\\                                     $$\\           \n \
$$ |  $$ |              $$ |  $$ |      $$  __$$\\                                    $$ |          \n \
$$ |  $$ |$$\\  $$\\  $$\\ $$ |  $$ |      $$ /  $$ | $$$$$$\\   $$$$$$$\\ $$$$$$\\   $$$$$$$ | $$$$$$\\  \n \
$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |      $$$$$$$$ |$$  __$$\ $$  _____|\\____$$\\ $$  __$$ |$$  __$$\\ \n \
$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |      $$  __$$ |$$ |  \\__|$$ /      $$$$$$$ |$$ /  $$ |$$$$$$$$ |\n \
$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |      $$ |  $$ |$$ |      $$ |     $$  __$$ |$$ |  $$ |$$   ____|\n \
\$$$$$$  |\\$$$$$\\$$$$  |\$$$$$$  |      $$ |  $$ |$$ |      \\$$$$$$$\\\\$$$$$$$ |\\$$$$$$$ |\\$$$$$$$\\ \n \
 \\______/  \\_____\\____/  \\______/       \\__|  \\__|\\__|       \\_______|\\_______| \\_______| \\_______|)\n \
                                                                                                   \n \
                                                                                                   \n")

""" Creates the player """
player = Player(int(input("How many cwedits do you w-want t-to deposit?!?1 ")))
""" Main loop """
while True:
    if("Yes" != input("Do you w-want t-to pway!?!11 UwU (Yes/Nyo)  ")):
        break
    player.playRound()
    

