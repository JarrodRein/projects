def merge_the_tools(string, k):
    # your code goes here
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        # For each chunk, create a set to track seen characters
        # and a result list to store unique characters
        substring = string[i:i+k]
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)