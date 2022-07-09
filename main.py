def sum(a, b, c ):
    return a + b + c

def printBoard( xMove, zMove ):
    zero= 'X' if xMove[0] else ('O' if zMove[0] else 0)
    one = 'X' if xMove[1] else ('O' if zMove[1] else 1)
    two = 'X' if xMove[2] else ('O' if zMove[2] else 2)
    three = 'X' if xMove[3] else ('O' if zMove[3] else 3)
    four = 'X' if xMove[4] else ('O' if zMove[4] else 4)
    five = 'X' if xMove[5] else ('O' if zMove[5] else 5)
    six = 'X' if xMove[6] else ('O' if zMove[6] else 6)
    seven = 'X' if xMove[7] else ('O' if zMove[7] else 7)
    eight = 'X' if xMove[8] else ('O' if zMove[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xMove, zMove):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xMove[win[0]], xMove[win[1]], xMove[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zMove[win[0]], zMove[win[1]], zMove[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    xMove = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zMove = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Myturn = 1 # 1 for X and 0 for O
    print("Start Tic_Tac_Toe")
    print(' ')
    while(True):
        printBoard(xMove, zMove)
        if(Myturn == 1):
            print(' ')
            value = int(input("X's Chance: "))
            print(' ')
            xMove[value] = 1
        else:
            print(' ')
            value = int(input("O's Chance: "))
            print(' ')
            zMove[value] = 1
        cwin = checkWin(xMove, zMove)
        Myturn = 1 - Myturn
        if(cwin != -1):
            print("Match over") 
           
            break
          
        
       