import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

class PlayAgain(IntEnum):
    No = 0
    Yes = 1

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    victories = {
        Action.Scissors: [Action.Lizard, Action.Paper],
        Action.Paper: [Action.Spock, Action.Rock],
        Action.Rock: [Action.Lizard, Action.Scissors],
        Action.Lizard: [Action.Spock, Action.Paper],
        Action.Spock: [Action.Scissors, Action.Rock]
}

    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

def get_answer():
    answers = [f"{answer.name}[{answer.value}]" for answer in PlayAgain]
    answers_str = ", ".join(answers)
    selection = int(input(f"Enter a choice ({answers_str}): "))
    answer = PlayAgain(selection)
    return answer

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    try:
        play_again = get_answer()
    except ValueError as e:
        range_str2 = f"[0, {len(PlayAgain) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str2}")
        

    if play_again == 0:
        break
