# Top secret elven tick tack toe decryption library
scores = {
    "win": 6,
    "draw": 3,
    "loss": 0
}

play = {
    "A": 'rock',
    "B": 'paper',
    "C": 'scissors'
}

response = {
    "X": 'rock',
    "Y": 'paper',
    "Z": 'scissors'
}

point_values = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

expected_outcome = {
    "X": 'loss',
    "Y": 'draw',
    "Z": 'win'
}

total_score: int = 0


def get_score(opponent, player):
    if play[opponent] == response[player]:
        return point_values[response[player]] + scores['draw']
    elif play[opponent] == 'rock' and response[player] == 'scissors':
        return point_values[response[player]] + scores['loss']
    elif play[opponent] == 'paper' and response[player] == 'rock':
        return point_values[response[player]] + scores['loss']
    elif play[opponent] == 'scissors' and response[player] == 'paper':
        return point_values[response[player]] + scores['loss']
    else:
        return point_values[response[player]] + scores['win']


def select_appriopriate_response(opponent, expected_outcome):
    if expected_outcome == 'win':
        if play[opponent] == 'rock':
            return 'Y'
        elif play[opponent] == 'paper':
            return 'Z'
        elif play[opponent] == 'scissors':
            return 'X'
    elif expected_outcome == 'draw':
        if play[opponent] == 'rock':
            return 'X'
        elif play[opponent] == 'paper':
            return 'Y'
        elif play[opponent] == 'scissors':
            return 'Z'
    elif expected_outcome == 'loss':
        if play[opponent] == 'rock':
            return 'Z'
        elif play[opponent] == 'paper':
            return 'X'
        elif play[opponent] == 'scissors':
            return 'Y'


# load our inputs and similate our games
with open('day-2/input.txt', 'r') as f:
    for line in f:
        opponent, player = line.strip().split(' ')
        # part 2 stuff.
        outcome = select_appriopriate_response(
            opponent, expected_outcome[player])

        total_score += get_score(opponent, outcome)


print(f"Total score: {total_score}")
