rnum = input("Enter your roman numeral:")
sum = 0
characters = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
for i in range(0,len(rnum)-1):
    if characters[rnum[i]] < characters[rnum[i+1]]:
            sum -= characters[rnum[i]]
    else:
          sum+= characters[rnum[i]]
print(sum+characters[rnum[-1]])