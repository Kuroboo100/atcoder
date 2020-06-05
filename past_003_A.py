s=input()
t=input()

if s==t:
    print("same")
else:
    if s.lower()==t.lower():
        print("case-insensitive")
    else:
        print("different")
