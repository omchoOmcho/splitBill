import random

a = int(input("Enter the number of friends joining (including you): \n"))
print()
d = {}

if a > 0:
    print("Enter the name of every friend (including you), each on a new line: ")
    
    for i in range(a):
        keys = input()
        d[keys] = 0
        #print(d)

    print()
    b = int(input("Enter the total bill value: \n"))
    c = float(b/a)
    e = round(c, 2)
    #print(e)
    
    r = dict.fromkeys(d, e)
    #print(r)
    print()

    game = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if game == "Yes":
        v = list(r.keys())
        izbor = random.choice(v)
        print()
        print(izbor,"is the lucky one!")
        print()
        r1 = {izbor:0}
        r.pop(izbor)
        n = b/len(r.keys())
        k = dict.fromkeys(r, n)
        k.update(r1)
        
        print(k)
        
    else:
        print()
        print("No one is going to be lucky")
        print()
        print(r)
else:
    
    print("No one is joining for the party")







