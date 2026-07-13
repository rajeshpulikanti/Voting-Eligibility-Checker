print ("==" * 45)
print("VOTING ELIGIBILITY CHECKER ")
print("=="*45)
name = input("Enter your name ")
try :
    age = int(input("Enter your age "))
except ValueError :
    print("Invalid age input ")
    exit()
if age < 0 :
    print("invalid information ")
    exit()
print(f"Hello {name}")
print(f"Age : {age}")
if age < 18 :
    years_left = 18 - age
    print ("Status :  not eligible ")
    print (f"Sorry  {name}, you are not eligible to vote ")
    print(f"you can vote after {years_left}")
elif age >= 18 :
    print("Status : eligible ")
    print (f"Congratulations {name }, you are eligible for voting ")
