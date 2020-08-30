#displays the information for the user
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

#User's choice for which row and column they want to edit
def user_choice():

    choice = 'Wrong'
    input_value = 'Wrong'
    acceptable_row = [1,2,3]
    acceptable_column = [0,1,2] 
    i = 0
    #for i in range(0,9): 
    while choice.isdigit() == False and input_value.isdigit() == False:
        choice = input('Please enter the row you want to select (1-3): ')
        input_value = input('Please enter the column (0-2): ')

        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        if choice in acceptable_row:
            print("Sorry, the value must be 1,2,3 ")

        if input_value.isdigit() == False:
            print("Sorry that is not a digit")

        if input_value in acceptable_column:
            print("Sorry, the value must be 0,1,2 ")

    if choice == '1':
        if input_value == '0':
            row1[0] = 'X'

        elif input_value == '1':
            row1[1] = 'X'

        elif input_value == '2':
            row1[2] = 'X'

    if choice == '2':
        if input_value == '0':
            row2[0] = 'X'

        elif input_value == '1':
            row2[1] = 'X'

        elif input_value == '2':
            row2[2] = 'X'

    if choice == '3':
        if input_value == '0':
            row3[0] = 'X'

        elif input_value == '1':
            row3[1] = 'X'

        elif input_value == '2':
            row3[2] = 'X'

    display(row1,row2,row3)

display(row1,row2,row3)
user_choice()



