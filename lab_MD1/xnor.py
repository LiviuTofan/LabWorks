a=input()
b=input()
if(a or b) not in (a and b):
    print(bool(0))
else:
    print(bool(1))