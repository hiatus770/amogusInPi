file = open("digits.txt", "r")
digits = file.read()

def patternSet(index):
    cur = []
    for i in range(16):
        cur.append(digits[index + i])

binary = ""
for digit in digits:
    binary += bin(int(digit))[2:]

pattern = [0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1]

for i in range(): 
    