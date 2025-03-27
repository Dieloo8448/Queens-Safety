def hamming_distance(a_data, b_data):
    """
    Determine the Hamming distance between two lists of ints.

    pre: a_data is not None, b_data is not None, len(a_data) == len(b_data)
    post: return the Hamming Distance between the two lists of ints.
    Neither the parameter a_data nor b_data are altered as a result of this
    function.
    """
    # START WORKING HERE:
    index_count = 0
    hammings_distance = 0
    for data in a_data:
        if data != b_data[index_count]:
            hammings_distance += 1
        index_count +=1
    return hammings_distance

def is_permutation(a_data, b_data): 
    """
    Determine whether integer lists a_data and b_data are permutations of each
    other.

    pre: a_data is not None, b_data is not None, and both lists only contain 
    integers
    post: return True if a_data is a permutation of b_data, False otherwise.
    Neither a_data nor b_data are altered as a result of this function.
    """
    # START WORKING HERE:
    a_frequency_0 = 0
    a_frequency_1 = 0
    a_frequency_2 = 0
    a_frequency_3 = 0
    a_frequency_4 = 0
    a_frequency_5 = 0
    a_frequency_6 = 0
    a_frequency_7 = 0
    a_frequency_8 = 0
    a_frequency_9 = 0

    b_frequency_0 = 0
    b_frequency_1 = 0
    b_frequency_2 = 0
    b_frequency_3 = 0
    b_frequency_4 = 0
    b_frequency_5 = 0
    b_frequency_6 = 0
    b_frequency_7 = 0
    b_frequency_8 = 0
    b_frequency_9 = 0

    for num in a_data:
        if num == 0:
            a_frequency_0 += 1
        elif num == 1:
            a_frequency_1 += 1
        elif num == 2:
            a_frequency_2 += 1
        elif num == 3:
            a_frequency_3 += 1
        elif num == 4:
            a_frequency_4 += 1
        elif num == 5:
            a_frequency_5 += 1
        elif num == 6:
            a_frequency_6 += 1
        elif num == 7:
            a_frequency_7 += 1
        elif num == 8:
            a_frequency_8 += 1
        elif num == 9:
            a_frequency_9 += 1

    for num in b_data:
        if num == 0:
            b_frequency_0 += 1
        elif num == 1:
            b_frequency_1 += 1
        elif num == 2:
            b_frequency_2 += 1
        elif num == 3:
            b_frequency_3 += 1
        elif num == 4:
            b_frequency_4 += 1
        elif num == 5:
            b_frequency_5 += 1
        elif num == 6:
            b_frequency_6 += 1
        elif num == 7:
            b_frequency_7 += 1
        elif num == 8:
            b_frequency_8 += 1
        elif num == 9:
            b_frequency_9 += 1
    a_frequencies_1 = [a_frequency_0, a_frequency_1, a_frequency_2, a_frequency_3, a_frequency_4]
    a_frequencies_2 = [a_frequency_5, a_frequency_6, a_frequency_7, a_frequency_8, a_frequency_9]
    b_frequencies_1 = [b_frequency_0, b_frequency_1, b_frequency_2, b_frequency_3, b_frequency_4]
    b_frequencies_2 = [b_frequency_5, b_frequency_6, b_frequency_7, b_frequency_8, b_frequency_9]

    if a_frequencies_1 == b_frequencies_1 and a_frequencies_2 == b_frequencies_2:
        return True
    return False

def most_vowels(list_of_strings):
    """
    Determine the index of the string that has the largest number of vowels.
    Vowels are defined as 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', and 'u'.

    pre: list_of_strings is not None, len(list_of_strings) > 0, and there is at
    least 1 element in list_of_strings that is not None.
    post: return the index of the element in list_of_strings that has
    the largest number of vowel characters and is not None.
    If there is a tie, return whichever of the tied indices is closest to zero.
    The empty string, "", has zero vowels. It is possible for the maximum
    number of vowels to be 0.
    The parameter list_of_strings is not altered as a result of this function.
    """
    # START WORKING HERE:
    most_vowel = -1
    most_vowels_index = -1
    vowel_count = 0
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for string in list_of_strings:
        if string is not None:
            for character in string:
                if character in vowels:
                    vowel_count += 1

            if vowel_count > most_vowel:
                most_vowel = vowel_count
                most_vowels_index = list_of_strings.index(string)

            elif vowel_count == most_vowel:
                if most_vowels_index > list_of_strings.index(string):
                    most_vowels_index = list_of_strings.index(string)             
        vowel_count = 0
    return most_vowels_index

def queens_are_safe(board):
    """
    Determine if the queens on the given board are safe.

    pre: board is not None, len(board) > 0 and len(board) < 9, and board is a 
    square matrix (in other words, all rows in board have len(board) columns.) 
    All elements of board are 'q' or '.', where 'q's represent queens, '.'s 
    represent open spaces.
    post: return True if the configuration of the board is safe, meaning no
    queen can attack any other queen on the board.
    Return False otherwise. The parameter board is not altered as a result of
    this function.
    """
    # START WORKING HERE:

    n = len(board)
    queens = []

    # Collect all queen positions
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'q' or board[row][col] == 'Q':
                queens.append((row, col))

    row_queen_seen = []
    col_queen_seen = []
    diag1_queen_seen = []
    diag2_queen_seen = []

    for row, col in queens:
        if row in row_queen_seen:
            return False
        row_queen_seen.append(row)
        if col in col_queen_seen:
            return False
        col_queen_seen.append(col)
        diag1 = row - col
        if diag1 in diag1_queen_seen:
            return False
        diag1_queen_seen.append(diag1)
        diag2 = row + col
        if diag2 in diag2_queen_seen:
            return False
        diag2_queen_seen.append(diag2)

    return True
