n, m = map(int, input().split())
m = list(map(int, input().split()))
path = 1
count = 0
 
for step in m:
    count += (step - path + n) % n
    path = step
 
print(count)
