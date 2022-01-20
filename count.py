


a='w3resource'
count={}
for i in a:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print(count)
