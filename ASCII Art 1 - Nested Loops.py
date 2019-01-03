breakBetweenExamples = '--------------- break between examples ---------------'

# ASCII art examples

def someRectangle():
    for j in range(6):
        # The above line makes a loop that counts from 0 to 5 and then ends.
        # Using this to draw 6 rows.
        for i in range(10):
            # The above line makes a loop that counts from 0 to 9 and then ends.
            # I'm using this to draw 10 symbols in each row. AKA columns.
            print('#', end='')
        print()  # Start a new line.


someRectangle()
print(breakBetweenExamples)


# ---------------------------------------
# ---------------------------------------


def customRectangle():
    ''' Asks user for rows, columns, and character and then displays custom rectangle. '''
    rows = int(input('How many rows?'))  # saving row as integer
    columns = int(input('How many columns?'))  # saving column as integer
    character = input('Which character?')  # getting a character to use as the pixel
    character = character[0]  # saving only the first character provided, in case more are typed
    for j in range(rows):  # repeat the following  row  times
        for i in range(columns):  # repeat the following  column  times
            print(character, end='')  # display the pixel character
        print()  # at the end of the row start a new line


customRectangle()
print(breakBetweenExamples)


# ---------------------------------------
# ---------------------------------------




def someTriangle():
    # Triangle with 5 rows:
    for j in range(1, 6):
        # The line above specifically counts like this: 1, 2, 3, 4, 5
        # j is the width of the triangle on that row.
        for i in range(j):
            # The above line loops j times.
            # Equivalent to saying that the width of row j is j.
            print('#', end='')
        print()  # End of row linebreak.


someTriangle()
print(breakBetweenExamples)


# ---------------------------------------
# ---------------------------------------


def customTriangle():
    ''' Asks user for width and character and then displays custom triangle. '''
    maxWidth = int(input('How wide will the triangle be?'))  # saving maxWidth as integer
    character = input('Which character do you want it to be made with?')  # getting a character to use as the pixel
    character = character[0]  # saving only the first character provided, in case more are typed
    for j in range(maxWidth):  # repeat the following  maxWidth  times
        # so j will take on values 0 to maxWidth-1
        for i in range(j + 1):
            # j value:      i values:
            #     0             0          <--- 1 iteration to print character
            #     1             0, 1       <--- 2 iterations to print character
            #     2             0, 1, 2    <--- 3 iterations to print character
            print(character, end='')  # display the pixel character
        print()  # at the end of the row start a new line
    for j in range(maxWidth - 1, 0, -1):  # count down from maxWidth-1 to 1 (stopping just before 0)
        # so j will take on values maxWidth-1 to 1
        for i in range(j):
            # j value:      i values:
            #     2             0, 1       <--- 2 iterations to print character
            #     1             0          <--- 1 iteration to print character
            #     0                        <--- j will not be 0
            print(character, end='')  # display the pixel character
        print()  # at the end of the row start a new line


customTriangle()

# ---------------------------------------
# ---------------------------------------
