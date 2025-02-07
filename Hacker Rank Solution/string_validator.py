'''print("Kodnest".isalnum())
print("Kodnest123".isalnum())

print("12345".isalpha())
print("Kodnest12".isalpha())

print("apple".islower())
print("APPLaE".isupper())

print(any[True True ]) '''

s = input()
print(any(i.isalpha() for i in s))
print(any(i.isalnum() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.isupper() for i in s))
print(any(i.islower() for i in s))