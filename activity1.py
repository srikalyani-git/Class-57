sum = 0
num = input("Enter your number:")
inum = int(num)
length = int(len(num))
for i in range(len(num)):
    sum += int(num[i])**(length)

if inum == sum:
    print(f"{inum} is an Armstrong number")
else:
    print(f"{inum} is not an Armstrong number")