def display():
    f = open('data.txt',encoding="utf8")

    exit

print("1. New Staff")
print("2. Delete Staff")
print("3. View Summary Data")
print("4. Save & Exit")
s = print(input("Input Choice:"))
print(s)
def inputz():
    if s <= 1:
        print("New Staff")
    elif s == 2:
        print("Delete Staff")
    elif s == 3:
        print("Summary Data")
    else:
        exit()
