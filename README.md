Easy
1. Create a list of numbers from 1 to 20
2. Create a list of all even numbers from 1 to 50
3. Create a list of squares of numbers from 1 to 10
expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
4. Convert a list of strings to uppercase
pythonwords = ["hello", "world", "python"]
expected: ["HELLO", "WORLD", "PYTHON"]
5. Extract all vowels from a string
pythonsentence = "hello world"
expected: ["e", "o", "o"]

Easy-Medium
6. Filter out negative numbers from a list
pythonnums = [3, -1, 4, -1, 5, -9, 2, -6]
expected: [3, 4, 5, 2]
7. Create a list of lengths of each word in a sentence
pythonsentence = "the quick brown fox"
expected: [3, 5, 5, 3]
8. Replace all odd numbers with 0 in a list
pythonnums = [1, 2, 3, 4, 5, 6]
expected: [0, 2, 0, 4, 0, 6]
9. Create a list of tuples pairing each number with its square
pythonexpected: [(1,1), (2,4), (3,9), (4,16), (5,25)]
10. Remove all duplicates from a list while keeping order
pythonnums = [1, 2, 2, 3, 4, 4, 5]
expected: [1, 2, 3, 4, 5]

Medium
11. Flatten a 2D list into a single list
pythonmatrix = [[1,2,3],[4,5,6],[7,8,9]]
expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
12. Create a list of all numbers from 1 to 100 divisible by both 3 and 5
expected: [15, 30, 45, 60, 75, 90]
13. Extract only the numbers from a mixed list
pythonmixed = [1, "hello", 2.5, True, "world", 42]
expected: [1, 2.5, 42]
14. Create a multiplication table for a given number as a list
pythonn = 5
expected: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
15. Given a list of words, keep only words that are palindromes
pythonwords = ["radar", "hello", "level", "world", "madam"]
expected: ["radar", "level", "madam"]

Medium-Hard
16. Create a list of all prime numbers up to 50
17. Transpose a matrix using list comprehension
pythonmatrix = [[1,2,3],[4,5,6],[7,8,9]]
expected: [[1,4,7],[2,5,8],[3,6,9]]
18. Given two lists, create a list of all pairs where the sum equals a target
pythona = [1, 2, 3, 4]
b = [5, 6, 7, 8]
target = 9
expected: [(1,8), (2,7), (3,6), (4,5)]

Hard
19. Create a dictionary from two lists using dictionary comprehension where keys are words and values are their frequency count
pythonwords = ["apple", "banana", "apple", "cherry", "banana", "apple"]
expected: {"apple": 3, "banana": 2, "cherry": 1}
20. Given a list of sentences, create a list of lists where each inner list contains words longer than 3 characters, sorted alphabetically, with duplicates removed
pythonsentences = ["the quick brown fox", "the lazy brown dog"]
expected: [["brown", "quick"], ["brown", "lazy"]]
