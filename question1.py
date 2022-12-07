def num_check(n,c=0):
    for i in str(n):
        if i.isnumeric():
            c+=1
    if c==10 or 11:
        print("valid")
    else:
        print("invalid")

num_check(2124567890)
num_check(212-456-7890)
num_check('(212)456-7890')
num_check('(212)-456-7890')
num_check('212.456.7890')
num_check(+12124567890)




