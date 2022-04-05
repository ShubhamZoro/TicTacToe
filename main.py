#tic tac toe
tic_tac=["_","_","_",
         "_","_","_",
         "_","_","_"]

cross='X'
zero='0'
gameover=True
i=0
def print_tac():
    print(tic_tac[0]+ " | " + tic_tac[1]+ " | " + tic_tac[2])
    print("________")
    print(tic_tac[3] + " | " + tic_tac[4] + " | " + tic_tac[5])
    print("________")
    print(tic_tac[6] + " | " + tic_tac[7] + " | " + tic_tac[8])

print_tac()

def player_input(i):
    pos = int(input("Enter the number 0-8: "))
    if pos>=0 and pos<9 and i%2==0 and tic_tac[pos] == "_" :
        tic_tac[pos] = cross
    elif  pos>=0 and pos<9 and i%2!=0 and tic_tac[pos]=="_" :
        tic_tac[pos] = zero
    else:
        if pos>=0 and pos<9:
            print("Position is already filled")
        else:
            print("Postion out of bound")
        player_input(i)


def win_lose(i):
    if tic_tac[0]==tic_tac[1]==tic_tac[2] and tic_tac[0]!="_":

        if tic_tac[0]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[3]==tic_tac[4]==tic_tac[5] and tic_tac[3]!="_":

        if tic_tac[3]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[6]==tic_tac[7]==tic_tac[8] and tic_tac[6]!="_":

        if tic_tac[6]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[0]==tic_tac[3]==tic_tac[6] and tic_tac[0]!="_":

        if tic_tac[0]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[1]==tic_tac[4]==tic_tac[7] and tic_tac[1]!="_":

        if tic_tac[1]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[2]==tic_tac[5]==tic_tac[8] and tic_tac[2]!="_":

        if tic_tac[2]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[0]==tic_tac[4]==tic_tac[8] and tic_tac[0]!="_":

        if tic_tac[0]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False

    elif tic_tac[2]==tic_tac[4]==tic_tac[6] and tic_tac[2]!="_":

        if tic_tac[2]==cross:
            print("Player1 win")
        else:
            print("Player2 win")
        return False
    else:
        if i==8:
            print("No one win")
            return False
        return True
while gameover:
    player_input(i)
    gameover=win_lose(i)
    print_tac()
    i = i + 1









