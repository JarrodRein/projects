def merge_the_tools(string, k):
    # your code goes here
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        # For each chunk, create a set to track seen characters
        # and a result list to store unique characters
        substring = string[i:i+k]
        # empty set to track seen characters
        # result list to store unique characters
        seen = set()
        result = []
        # Iterate through the characters in the substring
        # If the character has not been seen, add it to the result        
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        # Join the result list into a string and print it
        # Print the unique characters for the current chunk
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)