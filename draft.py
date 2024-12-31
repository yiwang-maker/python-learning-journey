# Draft Notes
# This file is for temporary notes and drafts. Content here may be changed or deleted at any time.
## 12.29
""" 
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

favorite_number = "301"
message = "我最喜欢的数字是"
print(f"{message}{favorite_number}。") # 注意一下f字符串的用法，有双引号和花括号。
 """
# import this

""" 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-4].title())
message = f"My first bicycle was a {bicycles[2].title()}."
print(message)
 """

""" names = ['jayden', 'john', 'tom']
# print(names[0].title() + "\n" + names[1].title() + "\n" + names[2].title())
# message = f"Hello, {names[0].title()}."
# print(message)

names[0] = 'miller'
print(names)
names.append('taylor')

del names[0]
print(names) """
""" 
names_list = ['jayden', 'john', 'tom']
message = f"{names_list[0].title()},请问我可以邀请你共进晚餐吗？"
print(message)
names_list.append('shen')
unpresent_name = names_list.pop(1)
print(f"不能参加的客人是：{unpresent_name.title()}。")
print(names_list)
names_list.insert(1,'wang')
print(names_list)
 """

""" squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
 """
""" squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares) """

""" for value in range(1,21):
    print(value) """

""" numbers = [value for value in range(1,100_0001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers)) """

numbers = [value**3 for value in range(1,11)]
print(numbers)


