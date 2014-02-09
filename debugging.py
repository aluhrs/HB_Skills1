# Write a function that finds the smallest element in a list of integers and returns it.
some_list = [1, 2, 3, 4, 5]

def long_words(word_list):
    # tmp = 0
    # # loop through the items in the list
    # for i in some_list:
    #     # if the item's value is less than the item's value in the next position
    #     if i < [i + 1]:
    #         # store the item's value
    #         tmp = i
    #         # print the item's value
    #         print tmp
    #     else:
    #         # store the next position's item value
    #         tmp = [i + 1]
    #     print temp
    # # return the smallest integar
    # return tmp
    new_list = sorted(word_list)
    print new_list[0]
    return new_list[0]

long_words(some_list)


