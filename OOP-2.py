x = [x for x in range(1 , 21)]

print(x)

x = [x for x in range(1 , 51) if x % 2 == 0]

print(x)

x = [x**2 for x in range(1 , 11)]

print(x)

words = ["hello" , "my" , "name" , "is" ,  "arko"]

words = [word.upper() for word in words]

print(words)

sentence = "A quick brown fox jumped over the brown fence"

vowels = [ words for words in sentence.lower().replace(" " , "") if words in "aeiou"]

print(vowels)

nums = [3, -1, 4, -1, 5, -9, 2, -6]

nums = [x for x in nums if x > 0]

print(nums)

letters = [len(words) for words in sentence.split()]

print(letters)

nums = [1, 2, 3, 4, 5, 6]

nums = [0 if num % 2 != 0 else num for num in nums]

print(nums)

x = [(x , x**2) for x in range(1 , 6)]

print(x)

nums = [1, 2, 2, 3, 4, 4, 5]

nums = [num for i , num in enumerate(nums) if num not in nums[:i]]

print(nums)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix = [matrix[j][i] for j in range(3)  for i in range(3)]

print(matrix)

x = [x for x in range(1 , 101) if x % 5 == 0 and x % 3 == 0]

print(x)

mixed = [1, "hello", 2.5, True, "world", 42]

numbers = [numbers for numbers in mixed if type(numbers) == int or type(numbers) == float]

print(numbers)

n = 5

mul = [n * i for i in range(1 , 11)]

print(mul)

words = ["radar", "hello", "level", "world", "madam"]

palindromes = [pals for i , pals in enumerate(words) if words[i] == words[i][::-1]]
print(palindromes)

primes = [i for primes in range(1 , 101) for i in range(1 , primes) if primes % i != 0]

print(primes)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]

print(transpose)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
target = 9

merger = [(x , y) for x in a for y in b if x + y == target]

print(merger)

