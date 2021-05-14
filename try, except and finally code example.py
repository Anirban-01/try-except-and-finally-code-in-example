def my_function():
    my_list = [0, 1, 2, 3, 4, 5]

    list_length = len(my_list)

    if list_length > 0:
        print('list length is greater')
    else:
        print('list length is lesser')

    # try block check whether the statement is executable
    try:
        list_length1 = len(my_list1)
        print(list_length1)
    # except block handles the error occurs in statement
    except:
        print('There is no list in code')
    # finally block print the statement whether the statement is true or false
    finally:
        print('Finally printing list: ', my_list)

    print(list_length)


my_function()