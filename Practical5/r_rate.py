# define the n and r
# repeat refine n for 5 times 
# n=n*r+n
# print the final n 



r=float(input("the average number of individuals infected by each individual with virus"))
n=84
for i in range(0,5):
        n=n*r+n
print(n)

