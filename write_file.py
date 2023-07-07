"""
Milton V. Banos
Write phrase to file with line # 1x1
"""

try:
    myfile = open('myfile.txt', 'wt') 
    phrase = 'Copy this to file'
    for i in range(len(phrase)):
        myfile.write("line #" + str(i+1) + ' ' + phrase[i] +"\n")
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))
