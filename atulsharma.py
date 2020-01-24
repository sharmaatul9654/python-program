a='hello atul'
for i in a:
    if i not in a:
        print(a.count(i),":",i)
        a+=i
