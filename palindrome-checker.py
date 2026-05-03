#palindrome checker
class isPalindrome:

    def __init__(self , word):

        self.word = word

    def palindrome(self):

        w = self.word
        w = w.lower()
        reverse = w[::-1]

        if reverse == w:
            return "Palindrome"

        else:
            return "Not Palindrome"


word = input("enter a word: ")

query = isPalindrome(word).palindrome()

print(query)

