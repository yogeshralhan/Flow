nums=[3,2,1,4,5,6,3,2,4]

list1 =[]
list2 =[]
nums.sort()
list1=nums
print list1
"""
i=0
v=list1[0]
p=len(list1)
for var in list1:
 if v==list1[i+1]:
 	print "hello"
 else:
 	list2.append(list1[i+1])
 i=p-1	
print list2	
"""

print list1
for i, element in enumerate(nums):
    # print i, element
    if i<=len(list1)-2:
        if list1[i+1] == last_seen:
            print "*",list1[i+1], last_seen
        else:
            print "appending ",element 
            last_seen = list1[i+1]
            res.append(last_seen)