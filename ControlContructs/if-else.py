age = input()
print('Enter your Age')
def checkAge():
    if(age < 18):
        print('Child')
    elif(age > 18 and age < 65):
        print('Adult')
    else:
        print('Senior Citizen')
checkAge()

