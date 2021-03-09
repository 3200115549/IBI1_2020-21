#first list the number: 1 1 2 3 5 8 13 21 34 55 89 144 233
#first time a=0, b=1
#second time let a=b=1 b=a+b=1
#so this can repeat for 13 times and print each value of a  

a,b=0,1
for i in range(0,13):
    a,b=b,a+b
    print(a)
