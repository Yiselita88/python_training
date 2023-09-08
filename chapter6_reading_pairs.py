# Reading pair of numbers
# read all line objects and indicates which ones are starting in the next line
lines = open('read_pairs1.dat', 'r').readlines()
# print(lines)
pairs = []
for line in lines:
    words = line.split()  # it splits the lines and gives them separated
    # print(words)
    for word in words:
        word = word[1:-1]  # strip off parentheses
        # print(word)
        # as it splits the words, it also assigns values to n1 and n2 variables
        n1, n2 = word.split(',')
        # print(n1, n2)
        n1 = float(n1)
        n2 = float(n2)
        pair = (n1, n2)
        print(pair)  # this prints the columns of all pairs
        # after converting the numbers into words, then it appends them into the list of pairs
        pairs.append(pair)
print(pairs)  # this prints the list of all pairs


# Reading pair of numbers when white spaces between parentheses are present
infile = open('read_pairs2.dat', 'r')
lines2 = infile.readlines()

pairs2 = []
for line2 in lines2:
    line2 = line2.strip()
    # this is the important part, where we're eliminating the blank spaces
    line2 = line2.replace(' ', '')
    # here we're eliminating the ')(' that separates the pair
    words = line2.split(')(')
    # here, for the first ford we're eliminating the leading parenthesis
    words[0] = words[0][1:]
    # here we're eliminating the last parenthesis of the last object in the line
    words[-1] = words[-1][:-1]
    for word in words:
        n1, n2, = word.split(',')
        n1 = float(n1)
        n2 = float(n2)
        pair = (n1, n2)
        pairs2.append(pair)
        print(pair)
print(pairs2)
