def romantoint(romaninput):
    roman ={'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    resultint = 0
    for i in range(0, len(romaninput) - 1):
       if roman[romaninput[i]] < roman[romaninput[i+1]]:
           resultint -= roman[romaninput[i]]
       else:
           resultint += roman[romaninput[i]]
    return resultint + roman[romaninput[-1]]

roman = input("input roman number")

print("integer equivalent:",romantoint(roman))