for _ in range(int(input())):
    n = int(input())
    l = [10,11,100,101,110,111,1000,1001,1010,1011,1100,1101,1111]
    if str(n).count("1") + str(n).count("0") == len(str(n)):
        print("YES")
    else:
        cnt = 1
        c = 0
        while c < len(l):
            temp = n
            if n % l[c] == 0:
               cnt *= l[c]
               n /= l[c]
               c  = 0 
               if cnt == temp or n == 1:
                    print("YES")
                    break
            else:
                c += 1
            
        else:
            print("NO")