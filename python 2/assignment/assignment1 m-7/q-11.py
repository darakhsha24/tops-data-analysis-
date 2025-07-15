# get input from use
User_letter1 = input("Enter single alphabet letter:")
# validate input
if len(User_letter1)!= 1 or not User_letter1.isalpha():
    print("invalid input! please enter valid input")
else:
    letter1 = User_letter1.lower()
    if letter1 in ["a","e","i","o","u"]:
        print(f"{User_letter1} is a vowel")
    else:
         print(f"{User_letter1} is not a vowel")