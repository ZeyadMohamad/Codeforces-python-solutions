word = list(input().lower())
orgin = "hello"
index = 0
new = ""
for i in word:
    if i == orgin[index]:
        new += i
        index += 1
    else:
        pass
    if index == len(orgin):
        break
    
if new == orgin:
    print("YES")
else:
    print("NO")