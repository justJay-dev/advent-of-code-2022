# a tick tack toe solver
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


# load our inputs and similate our games
with open('day-2/input.txt', 'r') as f:
    for line in f:
        opponent, player = line.strip().split(' ')
        print(play[opponent], response[player])
        total_score += get_score(opponent, player)


print(f"Total score: {total_score}")
