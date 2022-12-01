
def main():
    with open('day-1/input.txt') as f:
        data = f.read()

        # Split the data into a list of lists on new line as an elf.
        data = data.split('\n\n')
        # sum each split and return the sum and index of the split.
        snackiest_elf = {"index": 0, "calories": 0}
        # [{index: 0, calories: 0}]
        elf_inventories = []
        for i, calories in enumerate(data):
            # Split the data into a list of lists on new line as an elf.
            calories = calories.split('\n')
            # sum each split and return the sum and index of the split.
            total_calories = sum([int(c) for c in calories])
            # part 1
            # knowing what we know about part 2 now, we could just refactor to use the same solution as part 2 with :1
            # 🤷
            if total_calories > snackiest_elf["calories"]:
                snackiest_elf["calories"] = total_calories
                snackiest_elf["index"] = i

            # part 2
            elf_inventories.append({"index": i, "calories": total_calories})

    # part 1!
    print(snackiest_elf)
    # part 2!
    # print the top three elves with the most calories.
    sorted_elf_inventories = sorted(
        elf_inventories, key=lambda k: k['calories'], reverse=True)
    # sum the top three elves with the most calories.
    print(sum([x["calories"] for x in sorted_elf_inventories[:3]]))


main()
