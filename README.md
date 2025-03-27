# Queens-Safety

Description:
- Hamming Distance: Calculates the Hamming distance between two lists of integers.
- Permutation Check: Determines if two lists of integers are permutations of each other.
- Most Vowels: Finds the index of the string with the most vowels in a given list of strings.
- Queens Safety: Checks if the queens placed on a chessboard are in a safe configuration, meaning no queens can attack one another.

The goal of the project is to practice working with lists, strings, and basic algorithms, as well as to implement some fundamental operations in Python.

Example set 1: 

Hamming Distance:
hamming_distance([1, 0, 1], [1, 1, 0])  # Returns: 2

Permutation Check:
is_permutation([1, 2, 3, 4], [4, 3, 2, 1])  # Returns: True

Most Vowels:
most_vowels(['hello', 'world', 'python'])  # Returns: 1 (index of 'hello')

Queens Safety:
queens_are_safe([
    ['q', '.', '.', '.'],
    ['.', 'q', '.', '.'],
    ['.', '.', 'q', '.'],
    ['.', '.', '.', 'q']
])  # Returns: False (queens can attack each other)

Examples Set 2:
Hamming Distance:
Input: [1, 0, 1] and [1, 1, 0]
Output: 2

Permutation Check:
Input: [1, 2, 3, 4] and [4, 3, 2, 1]
Output: True

Most Vowels:
Input: ['hello', 'world', 'python']
Output: 1 (index of 'hello')

Queens Safety:
Input: 
[['q', '.', '.', '.'], 
['.', 'q', '.', '.'], 
['.', '.', 'q', '.'], 
['.', '.', '.', 'q']]
Output: False

Acknowledgments: This challenge was posed to me as an Assignment for UT Austin's CS313E course, shoutout to Professor Zou!

