# it's like that peg game in cracker barrel...kinda!
from collections import deque


# turn a string "like move 6 from 4 to 3" into a list of ints to be used in our move function :D
def parse_move(move):
    return [int(x) for x in move.split() if x.isdigit()]


def pop_left_n_times(times, crate):
    things_moved = []
    for _ in range(times):
        things_moved.append(crate.popleft() if crate else None)
    return things_moved


def enqueue_things_moved(things_moved, crate):
    for thing in things_moved:
        crate.appendleft(thing)


def main():
    # read the moves from the file
    with open("day-5/input.txt") as f:
        moves = [parse_move(line) for line in f]

    # create the crates
    crates = (
        deque(["F", "T", "N", "Z", "M", "G", "H", "J"]),
        deque(["J", "W", "V"]),
        deque(["H", "T", "B", "J", "L", "V", "G"]),
        deque(["L", "V", "D", "C", "N", "P", "B"]),
        deque(["G", "R", "P", "M", "S", "W", "F"]),
        deque(["M", "V", "N", "B", "F", "C", "H", "G"]),
        deque(["R", "M", "G", "H", "D"]),
        deque(["D", "Z", "V", "M", "N", "H"]),
        deque(["H", "F", "N", "G"]),
    )
    # sample_crates = (deque(["N", "Z"]), deque(["D", "C", "M"]), deque(["P"]))
    for move in moves:
        # move the crate
        # dequeue move[0] creates from move[1] to move[2]
        things_moved = pop_left_n_times(move[0], crates[move[1] - 1])
        enqueue_things_moved(things_moved, crates[move[2] - 1])

    # print the position 0 of each crate
    print("".join([crate[0] for crate in crates]))



main()
