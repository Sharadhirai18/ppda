#get user input
num= int(input("enter a number:"))

#print the multiplication table
print("multiplication table of {num}:")
for i in range(1, 11):
#print(num*i)  
#loop from 1 to 10
    print(f"{num} x {i} = {num*i}")
