# 13. Alphabet is Vowel or Consonant
char = input("Enter an alphabet: ").lower()
if char in "aeiou":
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Invalid Input")