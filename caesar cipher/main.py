ask = input("do you want to encode or decode?: ").lower()
if ask == "encode":

    word = input("ENTER YOUR word: ").upper()
    shift = int(input("enter your own shift:"))
    result = " "
    
    for i in word:
        if i ==" ":
            result += i
            continue
        convert = ord(i)
        

        sum = shift + convert
        if sum>90:
            
            character1=(chr(shift + 64))
            result += character1
        elif sum<90:
            character2=(chr(sum))
            result += character2
       

    print(result)

elif ask=="decode":
    word = input("ENTER YOUR word: ").upper()
    shift = int(input("enter your own shift:"))
    result = " "
    for i in word:
        if i ==" ":
            result += i
            continue
        convert = ord(i)

        s = convert - shift
        if s<64:
            sum = s + 90
            character1=(chr(sum - 64))
            result += character1
        elif s>64:
            character2=(chr(s))
            result += character2
       

    print(result)


    