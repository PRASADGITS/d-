import copy

'''
SHALLOW COPY METHOD
'''
old_list = [[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)

print ("old_list",old_list)
print ("new_list",new_list,"\n")

old_list.append([999])

print ("old_list",old_list)
print ("new_list",new_list,"\n")

old_list[1][0]="x"            # both changes Because the refernce is same for nested objects in shallow copy,
                              # poinsta to the same object in memory
print ("old_list",old_list)
print ("new_list",new_list,"\n")

'''
Deep copy method
'''
print ("Deep copy starts \n")

old_list_1 = [[1,2,3],[4,5,6],[7,8,9]]
new_list_1=copy.deepcopy(old_list_1)

print ("old_list_1",old_list_1)
print ("new_list_1",new_list_1,"\n")

old_list_1.append([999])

print ("old_list_1",old_list_1)
print ("new_list_1",new_list_1, "\n")

old_list_1[1][0]="x"            # Because the old list was recursively copied
print ("old_list_1",old_list_1)
print ("new_list_1",new_list_1)
