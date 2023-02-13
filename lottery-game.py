import random as r

def main():

    # Generate your lottery numbers
    player_list = []
    num_position = ["First","Second","Third","Fourth","Fifth","Sixth"]
    num = 0 #Initialisng variable to prevent while loop breaking

    for pos in num_position:
        while num < 1 or num > 50 or num in player_list or type(num) != int:
            num = int(input(f"Enter Your {pos} Lottery Number: "))
            if num < 1 or num > 50:
                print('\nInvalid Input - Integer Must Be Between 1-50\n')
            elif num in player_list:
                print('\nInvalid Input - Cannot Have 2 Identical Picks\n')
            elif type(num) != int:
                print('\nInvalid Input - Must Be Integer Type\n')
        player_list.append(num)
        num = 0 # Resetting to while loop condition

    print(f"Here are your Lottery Numbers: {player_list}")

    # Creating the Lottery Draw
    lottery_draw = r.sample(range(1,50),6)

    print(f"Winning Lottery Draw: {lottery_draw}")

    # Checking numbers for win condition
    match_list = []
    incorrect_values = []
    for val in player_list:
        if val in lottery_draw:
            match_list.append(val)
        elif val not in lottery_draw:
            incorrect_values.append(val)

    if len(match_list) == 6:
        print("Congrats! You are the Winner!")
    else:
        print(f"Unlucky... You only got {len(match_list)}/6 correct")

if __name__ == "__main__":
    main()