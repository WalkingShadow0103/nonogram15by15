while 1:
    sum = 0
    count = 0
    a_list = []
    while 1:
        tmp = input("type : ")
        if  tmp == 'r':
            break
        else:
            a_list.append(int(tmp))
            sum += int(tmp)
            count += 1

    print(sum+count-1)
    print(a_list)

    line = []
    clsf = 15-(sum+count-1) #classifier
    if clsf == 0:
        cc = 0 # countchecker
        for j in a_list:
            k = 0 # iteration for O
            while k != j:
               print("O",end='')
               k += 1

            if cc != len(a_list)-1:
               print("X",end='')
            cc += 1  # iteration for X

    elif clsf > 0:
        cc = 0
        for j in a_list: #1,2,3,4
            if j - clsf <= 0:
                k = 0
                while k != j:
                    print("X", end='')
                    k += 1

            else: # j - clsf = 1
                k = 0
                while k != clsf:
                    print("X", end='')
                    k += 1
                k = 0
                while k != j - clsf:
                    print("O", end='')
                    k += 1

            if cc != len(a_list)-1:
                print("X",end='')
            cc += 1

        k = 0
        while k != clsf:
            print("X", end='')
            k += 1
    print("")