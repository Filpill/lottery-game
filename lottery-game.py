import random as r

def error_message(num,player_list):
    if num < 1 or num > 50:
        print('\nInvalid Input - Integer Must Be Between 1-50\n')
    elif num in player_list:
        print('\nInvalid Input - Cannot Have 2 Identical Picks\n')

def selecting_first_numbers():

    player_list = []
    num_position = {
        1:"First",
        2:"Second",
        3:"Third",
        4:"Fourth",
        5:"Fifth",
        6:"Sixth"
        }
    num = 0 #Initialising variable outside of Integer Range For While Loop

    for i in range(1,7):
        while num < 1 or num > 50 or num in player_list or type(num) != int:
            num = int(input(f"Enter Your {num_position.get(i)} Lottery Number: "))
            error_message(num,player_list)
        player_list.append(num)
        num = 0 # Reset Variable

    return player_list

# def reroll(player_list,correct_values,incorrect_values):
#     for i,val in enumerate(incorrect_values):


def main():

    player_list = selecting_first_numbers()
    print(f"Here are your Lottery Numbers: {player_list}")

    # Creating the Lottery Draw
    lottery_draw = r.sample(range(1,50),6)

    # Seperating Values into Correct/Incorrect Lists
    correct_values = []
    incorrect_values = []
    for val in player_list:
        if val in lottery_draw:
            correct_values.append(val)
        elif val not in lottery_draw:
            incorrect_values.append(val)

    # Checking numbers for win condition
    if len(correct_values) < 6:
        print(f"\nUnlucky... You only got {len(correct_values)}/6 correct\n")
        print(f"But you will have a chance to re-roll in the Bonus Round!")
        # reroll()
    elif len(correct_values) == 6:
        print(f"The Winning Lottery Draw: {lottery_draw}")
        print("\nCongrats! You are the Winner!\n")

if __name__ == "__main__":
    main()