"""
Milton V. Banos
Compare two software version strings
"""


def string_compare(str1, str2):

    str1_list = str1.split('.')  # list w/str vals
    str2_list = str2.split('.')

    # Convert str element to int, put into new list using comprehension
    str1_list = [int(i) for i in str1_list]
    str2_list = [int(i) for i in str2_list]

    # Convert list to tuple for comparison
    str1_tuple = tuple(str1_list)
    str2_tuple = tuple(str2_list)

    if str1_tuple < str2_tuple:
        print(str1 + ' is smaller than ' + str2)
    elif str1_tuple > str2_tuple:
        print(str1 + ' bigger than ' + str2)
    else:
        print(str1 + ' == ' + str2)


string_compare('1.2.3', '1.2.13')
string_compare('1.2.23', '1.2.13')
string_compare('2.2.23', '1.2.13')
string_compare('2.2.23', '1.2.13')
string_compare('1.2.23', '1.2.23')
string_compare('1.0', '1.2.23.44.55')
