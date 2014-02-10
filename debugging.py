#numbers = [1, 2, 3, 4, 5]
string_list = ["ashley", "shaun", "jane", "russ"]

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

join_strings(string_list)    

# Write a function that joins all the strings in a list 
# together (without using the join method) and returns a single string.