bin = input("Enter your binary number:")
sum = 0
n = len(bin)-1
while n > 0:
    for i in range(len(bin)):
        sum += int(bin[i])*(2**n)
        n -= 1

print(sum)