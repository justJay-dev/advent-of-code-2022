def main():
    fully_contains = []
    overlaps = []
    with open("day-4/input.txt") as f:
        data = f.read().split("\n")
        for pairs in data:
            # split each pair into sections
            sections = pairs.split(",")
            # treat each section as a range of numbers 2-4 = 2,3,3 etc.
            the_range = [
                range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in sections
            ]
            # find if one range fully contains the other
            left = set(the_range[0])
            right = set(the_range[1])
            if left.issubset(right) or right.issubset(left):
                fully_contains.append(pairs)
            # find if the ranges overlap
            if any(x in right for x in left):
                overlaps.append(pairs)

    print("Part 1 solution: ", len(fully_contains))
    print("Part 2 solution: ", len(overlaps))


main()
