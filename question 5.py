

list1=["One","Two","Three","Four","Five"]
list2=[1,2,3,4,5]
dict={}
for i in list1:
    for j in list2:
        dict[i]=j
        list2.remove(j)
        break
print(dict)


# list=['a','b','c','d','e','f']
# list1=[1,2,3,4,5]
# dict={}
# for i in list:
#     for j in list1:
#         dict[i]=j
#         list1.remove(j)
#         break
# print(dict)




# a=[1,2,3,4,5,6]
# dic={}
# for i in a:
#     dic[i]=i
#         # c=({i:j})
#     dic.update({dic[i]:i})
# print(dic)

# dic={}
# i=0
# while i<len(a):
#     j=0
#     while j<=i-1:
#         dic.update({a[i]:a[j]})
#         j=j+1
#     i=i+1
# print(dic)
