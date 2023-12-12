import argparse

digitNames = {"one": "1", "two": "2", "three": "3",
                "four": "4", "five": "5", "six": "6",
                "seven": "7", "eight": "8", "nine": "9"}

def getDigit(line: str, from_front: bool, count_word=False) -> str:
    
    if from_front:
        starting_index = 0
        inc_value = 1
        word_index = len(line)
        word = ""
        if count_word:
            for digit in digitNames.keys():
                found_index = line.find(digit)
                if found_index >= 0 and found_index < word_index:
                    word_index = found_index
                    word = digitNames[digit]

    else:
        starting_index = len(line) - 1
        inc_value = -1
        word_index = -1
        word = ""
        if count_word:
            for digit in digitNames.keys():
                found_index = line.rfind(digit)
                if found_index > word_index:
                    word_index = found_index
                    word = digitNames[digit]

    for index in range(starting_index, word_index, inc_value):
        if line[index].isdigit():
            return line[index]

    return word

    
    


def main():
    # Create CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", help="Treat words as digits", action="store_true")
    parser.add_argument("file_path", help="Path to file to process")
    args = parser.parse_args()

    # Get file name from user input 
    file_name = args.file_path

    # Open the file to start processing
    with open(file_name, "r") as f:
        # Iterate through all the lines
        sum = 0
        for line in f:

            # Find first digit
            first_digit = getDigit(line, True, args.w)

            # Find last digit
            last_digit = getDigit(line, False, args.w)

            # Combine the digits and add to the running sum
            sum += int(first_digit + last_digit)

    print(f"Sum of numbers is {sum}")


if __name__ == "__main__":
    getDigit

    main()