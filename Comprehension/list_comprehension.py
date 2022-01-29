ls=[]
# for i in range(100):
#     if i %3 ==0:
#         ls.append(i)
        
# Below is a comprehensive way to do the above 

ls=[i for i in range(100) if i%3 == 0]
print(ls)