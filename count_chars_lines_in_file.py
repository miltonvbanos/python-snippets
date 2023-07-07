try:
    countlines = countchars = 0
    file = open('somefile', 'r')
    lines = file.readlines()
    # readlines() method reads all the lines of the file and joins them in a list sequence
    for line in lines:
        print(line, end='')
        countlines += 1
        for char in line:
            countchars += 1
    file.close()
    print("\nCharacters in file:", countchars)
    print("Lines in file:", countlines)
except IOError as error:
    print("I/O error occurred:", str(error))
