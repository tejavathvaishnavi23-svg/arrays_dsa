print("1")

# This is a sample Python script.
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)
    print("3")
    print(f'Hi, {name}')
    # Press F9 to toggle the breakpoint.
    print("vaishu")
    a = 5
    print(a)
    b = 6
    a = b
    print(a,'b')
    print(b)
    b = 7
    print(b)
    result = a*b
    print("Multiplication of 5 and 6 is: 3000",result)

def get_name(name):
    print(name)

def get_my_name(name):
    print(name)

def get_location(location):
    print(location)

def get_email(email):
    print(email)

get_my_name("Ram charan")

# Press the green button in the gutter to run the script.
print("5")
if __name__ == '__main__':
    print("2")
    get_location("Laxmipur")
    get_email("tejavathvaishnavi@gmail.com")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 13:
        print("child")
    elif age < 18:
        print("Teen")
    elif age < 60:
        print("Adult")
    else:
        print("Senior Citizen")

    marks = 80
    attendance = 75

    if marks >= 50 and attendance >= 75:
        print("pass")

    print_hi('vaishu')
    print("***")
    get_name('ravi mama')
    print("4")
print("8")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
