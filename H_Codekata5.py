def decode(iptn):
    if len(iptn) == 0:
        return 1
    elif len(iptn) == 1:
        return 1 if int(iptn[0]) != 0 else 0

    else:
        if int(iptn[0]) == 0 or (int(iptn[0]) == 0 and int(iptn[1]) == 0):
            return 0
        elif int(iptn[0:2]) <= 26:
            return decode(iptn[1:]) + decode(iptn[2:])
        else:
            return decode(iptn[1:])
        
iptn = input("Enter the number:")
print(decode(iptn))
