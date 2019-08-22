import random
from more_itertools import split_after

print("input your desired size of the list:")
size1 = input("> ")
int_size1 = int(size1)

i=0
lst=[]
while i < int_size1:
    ran = random.randint(0,1)
    lst.append(ran)
    i=i+1        
lst2=list(split_after(lst, lambda x:x < 1))
len_lst2 = len(lst2)

k = 0
a = 0
for j in lst2:
    sum_lst2 = sum(lst2[k])
    if sum_lst2 > 1:
        a=a+1
    k=k+1
    if k == len_lst2:
        print (lst,"=>",a)