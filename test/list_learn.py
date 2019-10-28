a_list = [1, 2, 3]
a_list[0]
a_t = (1,2,3)
# {key:value}  key是唯一
a_dict = {"a":"xxx","b":"111"}
a_dict['a']
a_dict.get("a")
for a in a_list:
	print(a)

print(len(a_list))
# for i in range(3)
# 循环list
for i in range(len(a_list)):
	print(a_list[i])

for i in range(10):
	print(i)
#	循环元组
print("-------------")
for a in a_t:
	print(a)

print('---------')
# 循环字典
for key,value in a_dict.items():
	print(key,value)

# list 的添加元素
a = list() # a = []
a.append(1)
print(a)
a.remove(1)
# dict
aa = dict() # aa = {}
aa["a"] ='123'
aa['a'] = '1234'
print(aa) # {"a":"1234"}
aa.update({"a":"12345","b":"1221"})
print(aa)
