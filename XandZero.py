print("X and 0 game created by Mohammed Ali Zia")

Player1_name = input("Player 1, what is your name?")
Player2_name = input("Player 2, what is your name?")

# Position Dictionary

pos = dict([
    ("A1", "n"),
    ("A2", "n"),
    ("A3", "n"),
    ("B1", "n"),
    ("B2", "n"),
    ("B3", "n"),
    ("C1", "n"),
    ("C2", "n"),
    ("C3", "n"),
])

# Grid Identifier for display

sampleRow1 = ["A1", "A2", "A3"]
sampleRow2 = ["B1", "B2", "B3"]
sampleRow3 = ["C1", "C2", "C3"]

possible_positions = sampleRow1
possible_positions.extend(sampleRow2)
possible_positions.extend(sampleRow3)

print("The following is the format of this game:-")
print(possible_positions[0:3])
print(possible_positions[3:6])
print(possible_positions[6:9])

print(Player1_name + " is X")
print(Player2_name + " is 0")

# Player Movement Definitions

def user1_move():
    user1_continue = 0
    while (user1_continue == 0):
        user1_input = input(Player1_name + ", where on the grid do you want to move")
        if (user1_input in possible_positions) and (pos[user1_input] != "0") and (pos[user1_input] != "X"):
            user1_continue = 1
            pos[user1_input] = "X"
        else:
            if (user1_input in possible_positions) == False:
                print("Sorry, " + Player1_name + " " + user1_input + " doesn't exist")
            elif pos[user1_input] == "X" or pos[user1_input] == "0":
                print("Sorry, " + Player1_name + " " + user1_input + " is taken")


def user2_move():
    user2_continue = 0
    while (user2_continue == 0):
        user2_input = input(Player2_name + ", where on the grid do you want to move")
        if (user2_input in possible_positions) and (pos[user2_input] != "0") and (pos[user2_input] != "X"):
            user2_continue = 1
            pos[user2_input] = "0"
        else:
            if (user2_input in possible_positions) == False:
                print("Sorry, " + Player2_name + " " + user2_input + " doesn't exist")
            elif pos[user2_input] == "X" or pos[user2_input] == "0":
                print("Sorry, " + Player2_name + " " + user2_input + " is taken")

# Winning situations

Win1 = ["X", "X", "X"]
Win2 = ["0", "0", "0"]

# Main Game

win = 0
while win == 0:
    Row1_p1 = [pos["A1"], pos["A2"], pos["A3"]]
    Row2_p1 = [pos["B1"], pos["B2"], pos["B3"]]
    Row3_p1 = [pos["C1"], pos["C2"], pos["C3"]]

    # Grid display to help play the game (Position Indicators)
    print("The following is the format of this game:-")
    print(possible_positions[0:3])
    print(possible_positions[3:6])
    print(possible_positions[6:9])

    # Current Grid Display
    print("The current grid is:-")
    print(Row1_p1)
    print(Row2_p1)
    print(Row3_p1)

    user1_move()

    Row1_p1 = [pos["A1"], pos["A2"], pos["A3"]]
    Row2_p1 = [pos["B1"], pos["B2"], pos["B3"]]
    Row3_p1 = [pos["C1"], pos["C2"], pos["C3"]]

    current_positions = Row1_p1
    current_positions.extend(Row2_p1)
    current_positions.extend(Row3_p1)

    if (Row1_p1 == Win1) or (Row2_p1 == Win1) or (Row3_p1 == Win1) or ((Row1_p1[0] == "X") and (Row2_p1[0] == "X") and (Row3_p1[0] == "X")) or ((Row1_p1[1] == "X") and (Row2_p1[1] == "X") and (Row3_p1[1] == "X")) or ((Row1_p1[2] == "X") and (Row2_p1[2] == "X") and (Row3_p1[2] == "X")) or ((Row1_p1[0] == "X") and (Row2_p1[1] == "X") and (Row3_p1[2] == "X")) or ((Row1_p1[2] == "X") and (Row2_p1[1] == "X") and (Row3_p1[0] == "X")):
        win = 1
        print(Player1_name + " won the game")
        break

    elif ("n" in current_positions) == False:
        win = 1
        print("Nobody won the game")
        break
    else:
        Row1_p2 = [pos["A1"], pos["A2"], pos["A3"]]
        Row2_p2 = [pos["B1"], pos["B2"], pos["B3"]]
        Row3_p2 = [pos["C1"], pos["C2"], pos["C3"]]

        # Grid display to help play the game (Position Indicators)
        print("The following is the format of this game:-")
        print(possible_positions[0:3])
        print(possible_positions[3:6])
        print(possible_positions[6:9])

        # Current Grid display
        print("The current grid is:-")
        print(Row1_p2)
        print(Row2_p2)
        print(Row3_p2)

        user2_move()

        Row1_p2 = [pos["A1"], pos["A2"], pos["A3"]]
        Row2_p2 = [pos["B1"], pos["B2"], pos["B3"]]
        Row3_p2 = [pos["C1"], pos["C2"], pos["C3"]]

        current_positions = Row1_p2
        current_positions.extend(Row2_p2)
        current_positions.extend(Row3_p2)

        if (Row1_p2 == Win2) or (Row2_p2 == Win2) or (Row3_p2 == Win2) or ((Row1_p2[0] == "0") and (Row2_p2[0] == "0") and (Row3_p2[0] == "0")) or ((Row1_p2[1] == "0") and (Row2_p2[1] == "0") and (Row3_p2[1] == "0")) or ((Row1_p2[2] == "0") and (Row2_p2[2] == "0") and (Row3_p2[2] == "0")) or ((Row1_p2[0] == "0") and (Row2_p2[1] == "0") and (Row3_p2[2] == "0")) or ((Row1_p2[2] == "0") and (Row2_p2[1] == "0") and (Row3_p2[0] == "0")):
            win = 1
            print(Player2_name + " won the game")
            break
        elif ("n" in current_positions) == False:
            win = 1
            print("Nobody won the game")
            break
        else:
            continue

Final_exit = input("Press 'Enter' to exit the game")






