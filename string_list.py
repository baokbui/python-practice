word = input("Enter a word: ")

wordReverse = word[::-1]

if wordReverse == word:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")