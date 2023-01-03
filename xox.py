import os,time,sys,random
class XOX:
    def __init__(self) -> None:
        self.table = [ ["","",""] , ["","",""] , ["","",""] ]
        self.status = True
        self.move = 0

    def xoxTable(self):
        for c in self.table:
            for r in c:
                print("_" +r + "_" + " " * (5 - len(r)),end="")
            print("\n")

    def playerX(self):
        print('Player X ')
        try:
            row = int(input('Row Number : '))
            while row < 0 or row > 3 :
                print('Please select a value from 1 to 3!')
                row = int(input('Row Number : '))
            column = int(input('Column Number : '))
            while column < 0 or column > 3:
                print("Please select a value from 1 to 3")
                column = int(input('Column Number'))  
            if self.isItFull(row,column):
                self.table[row][column] = 'X'
                self.gameConfigration()
            else:
                print('Bu Alan Dolu')
                self.move -= 1

        except ValueError:
            print('Cannot contain textual expressions and spaces !')
            self.program()
            sys.exit()

    def playerO(self):
        print('Player O ')
        time.sleep(1)
        row = random.randint(0,2)
        column = random.randint(0,2)

        if self.isItFull(row,column):
            self.table[row][column] = 'O'
            self.gameConfigration()
        else:
            row = random.randint(0,2)
            column = random.randint(0,2)
            self.move -= 1

    def isItFull(self,row,column):
        if self.table[row][column] != "": #is Full
            return False
        
        return True # is empty

    def gameConfigration(self):
        self.clearTerminal()
        self.xoxTable()

    def clearTerminal(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        else:
            pass
    def program(self):        
        for i in range(3,1,-1):
            print('\rProgram Closing %s'%(i),end = "")
            time.sleep(1)
        self.clearTerminal()

    def listControl(self):
        # region Yatay
        if [self.table[0][0],self.table[0][1],self.table[0][2]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][0],self.table[0][1],self.table[0][2]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        elif [self.table[1][0],self.table[1][1],self.table[1][2]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[1][0],self.table[1][1],self.table[1][2]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        elif [self.table[2][0],self.table[2][1],self.table[2][2]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[2][0],self.table[2][1],self.table[2][2]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        #endregion
        
        # region Dikey 
        elif [self.table[0][0],self.table[1][0],self.table[2][0]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][0],self.table[1][0],self.table[2][0]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        elif [self.table[0][1],self.table[1][1],self.table[2][1]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][1],self.table[1][1],self.table[2][1]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False

        elif [self.table[0][2],self.table[1][2],self.table[2][2]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][2],self.table[1][2],self.table[2][2]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        #endregion
        
        # region Çapraz
        elif [self.table[0][2],self.table[1][1],self.table[2][0]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][2],self.table[1][1],self.table[2][0]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        elif [self.table[0][0],self.table[1][1],self.table[2][2]] == ["X","X","X"]:
            print('Winning Player : PlayerX')
            return False
        elif [self.table[0][0],self.table[1][1],self.table[2][2]] == ["O","O","O"]:
            print('Winning Player : PlayerO')
            return False
        #endregion
        else:
            return True
        
    def play(self):
        if self.move % 2 == 0:
            self.playerX()
        else:
            self.playerO()
        self.status = self.listControl()
        self.move += 1 
    
if __name__ == '__main__':
    game = XOX()
    game.xoxTable()
    while game.status:
        game.play()
