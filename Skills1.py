# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    #create new list
    new_list = []
    # loop through each item in some_list
    for i in some_list:
        # find the odd numbers
        if i % 2 != 0:
            # append to the new list
            new_list.append(i)
            # verify the new list
            print new_list

    # return the list with the odd numbers
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    #create new list
    new_list = []
    # loop through each item in some_list
    for i in some_list:
        # find the even numbers
        if i % 2 == 0:
            # append to the new list
            new_list.append(i)
            # verify the new list
            print new_list

    # return the list with the odd numbers
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    #create new list
    new_list = []
    # loop through the list
    for i in word_list:
        # find the even numbers
        if len(i) >= 4:
            # append to the new list
            new_list.append(i)
            # verify the new list
            print new_list

    # return the list with the odd numbers
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    rnew_list = sorted(word_list)
    print new_list[0]
    return new_list[0]

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):

    largest_number = some_list[0]    

    for i in some_list:
        if i >= largest_number:
            largest_number = i
            print largest_number
    return largest_number

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    # create an empty list
    new_list = []    

    # loop through each element in the list
    # divide each element by 2
    # add it to the new list
    # return the list
    for i in some_list:
        divided_by_two = float(i/2.0)
        new_list.append(divided_by_two)
    #print new_list    
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    # create an empty list
    new_list = []    

    # loop through each word in the list
    # get the length of each word
    # add it to the new list
    # return the list
    for i in word_list:
        length_of_word = len(i)
        new_list.append(length_of_word)
    #print new_list    
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    # variable to hold number summing     
    sum_of_numbers = 0

    # loop through each number in the list
    # add the number to sum_of_numbers
    # return sum_of_number

    for i in numbers:
        sum_of_numbers += i
        print sum_of_numbers
        
    # print sum_of_numbers
    print sum_of_numbers
    return sum_of_numbers

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    # variable to hold number multiplying     
    multiply_numbers = numbers[0]

    # loop through each number in the list
    # multiply and then assign it to the var
    # return multiply_numbers

    for i in numbers:
        multiply_numbers *= i
        # print multiply_numbers

    # print sum_of_numbers
    # print multiply_numbers
    return multiply_numbers

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    # variable to hold the new string     
    new_string = " "

    # loop through each string in the list
    # add each string to the new string
    # return new_string

    for i in string_list:
        new_string += i + ' '
        
    # print new_string
    print new_string
    return new_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    # variable to hold the average     
    sum_of_numbers = 0
    # average_of_numbers = 0
    # loop through each number in the list
    # average each number
    # return average_of_numbers

    for i in numbers:
        sum_of_numbers += i
        # print sum_of_numbers
        
    # print sum_of_numbers
    average_of_numbers = sum_of_numbers/len(numbers)
    # print average_of_numbers
    # print average_of_numbers
    return average_of_numbers