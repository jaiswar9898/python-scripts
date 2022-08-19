# This script helps to count number of words, number of lines and number of characters from a file

def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(r'C:\Users\admin\main\newfolder\revenue.txt','r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

if __name__ == '__main__':
    countWords('revenue.txt')