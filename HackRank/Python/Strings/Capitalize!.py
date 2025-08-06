#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s3 = s.split(" ")
        # s1 = s3[0]
        # s2 = s3[1]
        # #print(s1)
        # #print(s2)
        # s11 = s1[0].capitalize()
        # s22 = s2[0].capitalize()
        # s11 += s1[1:len(s1)]
        # s22 += s2[1:len(s2)]
        # result = s11 + " " + s22
    cap_words = []
        
    for word in s3:
        if word and word[0].isalpha():
            word = word[0].upper() + word[1:]
        cap_words.append(word)
    
    result = " ".join(cap_words)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
