def LookAndSay(number):
    sequence=[1]
    for seq in range(number-1):
        digits=str(sequence[seq])
        temp=[digits[0]]
        tn=0
        for digit in range(1, len(str(sequence[seq]))):
            if temp[tn][0]==digits[digit]:
                temp[tn]+=digits[digit]
            else:
                temp.append(digits[digit])
                tn+=1
        nextSequence=""
        for i,j in enumerate(temp):
            nextSequence+=str(len(j))+temp[i][0]
        sequence.append(int(nextSequence))
    print(sequence)
LookAndSay(10)