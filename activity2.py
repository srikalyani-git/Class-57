num = int(input("Enter your number:"))
factors = []
for i in range(1,num+1):
    if num/i == num//i:
        factors.append(i)
print(factors)