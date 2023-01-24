file = open("digits.txt", "r")
digits = file.read()

binary = ""
for digit in digits:
    binary += bin(int(digit))[2:]

def patternSet(index):
    cur = ""
    for i in range(16):
        cur += (binary[index + i])
    return cur

def printPattern(pattern):
    for i in range(4):
        for j in range(4):
            if (pattern[(i*4)+j] == "0"):
                print(" ", end="")
            if (pattern[(i*4)+j] == "1"):
                print("#", end="")
        print()

pattern = "1111100110011111" # "1111100110011111" # "0111110011110101" # Amogus pattern

for i in range(len(digits)-15):
    if (pattern == binary[i:i+16]):
        print("Pattern matched at", i)
        printPattern(pattern)
        