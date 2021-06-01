list_1= [1,2,3]
new_list = [item+1 for item in list_1]
print(new_list)
name = "Angela"
new_name = [i for i in name]
print(new_name)
new =[i*2 for i in range(1,5)]
print(new)
even = [i for i in range(101) if i % 2 == 0 and i % 3 == 0]
print(even)

names = ["alex", 'ealanor','beth',"dave", "Akshith"]
caps_list = [idx.upper() for idx in names if len(idx)>5]
print(caps_list)


