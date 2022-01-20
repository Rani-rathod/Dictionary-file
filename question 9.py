

my_dict="MISSISSIPPI"
count=0
dict={}
for i in my_dict:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)


