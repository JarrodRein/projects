

def split_and_join(line):
    line = line.split(" ")  # Split the string into a list of words
    return "-".join(line)  # Join the list into a string with hyphens


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)