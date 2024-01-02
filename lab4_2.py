#write a programme that asks for a character to be entered by the user
#then the programme checks whether the given character is vowel or consonant:
vowels=("a","e","i","o","u")
char=input("enter a letter")
if char in vowels:
    print("your letter is vowel")
if char not in vowels:
    print("your letter is consonant")
