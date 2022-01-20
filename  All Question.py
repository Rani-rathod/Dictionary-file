
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1 :
#     if i in d2 :
#         d2[i]=(d1[i]+d2[i])
#     else :
#         d2[i]=d1[i]
# print(d2)



# d={}
# n=5
# for i in range(1,n+1):
#     key=i
#     value=i*i
#     z={key:value}
#     d.update(z)
# print(d)


# d={0:10, 1:20}
# d[2]=30
# print(d)


# d1={'a': 100, 'b': 200}
# d2={'x': 300, 'y': 200}
# dic={}
# for x in (d1,d2):
#     dic.update(x)
# print(dic)


# dic= {'data1':100,'data2':-54,'data3':247}
# a=1
# for k in dic:    
#     a=a*dic[k]
# print(a)


# dict={'a':1,'b':2,'c':3,'d':4}
# if 'a' in dict: 
#     del dict['a']
# print(dict)


# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in dic:
#     for j in dic:
#         if dic[i]>dic[j]:
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)


# dict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in dict:
#     print(dict[i])


# dict_num={4:10,7:20,1:30,5:40,2:50,8:60}
# count=0
# for i in dict_num:
#     count=count+1
#     print(i,dict_num[i],count)



# dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dic.popitem()
# print(dic)
