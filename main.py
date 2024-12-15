'''We will make the baord using dictionary
in which keys will be the location(i. : top-left,mid-right,etc.)
and initiallity it's values will be empty space and then after every
move
    we will change the valkue accoring toto player's choice of move.'''

theboard = {'7' : '', '8': '' , '9': '',
            '4': '', '5': '', '6': '',
            '1': '', '2': '' , '3': '',}
board_keys =[]

for key in theBoard:
    board_keys.append(key)

'''We will have to print the updated after every move in the game
and
   thus we will make a function in which we'll define the printBaod
   function so that we can easily print the board everytime by calling this
   function.'''

def printBoard(board):
   print(board['7'] +'|' +  board['8'] + '|' + board['9'])
   print('-+-+-')
   print(board['4'] +'|' +  board['5'] + '|' + board['6'])
   print('-+-+-')
   print(board['1'] +'|' +  board['2'] + '|' + board['3'])
   print('-+-+-')

def game():
       
       turn = 'x'
       count = 0

for i in range(10):
     printBoard(theBoard)
     print("it's your turn," + turn + turn + "Move to which pleace?")

     if theBoard[move] == ' ':
          theBoard[move] = turn
          count += 1

     else:
          print("that place is already filled.\nMove to which place?")
          continue
     