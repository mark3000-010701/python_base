import turtle as t
'''vẽ hình vuông quay tròn'''
'''
def draw_square(a):
    for i in  range(3):
        t.forward(100)
        t.right(90)
    t.forward(100)
    t.right(90+a)
step=36
a=360/step
for i in range(step):
    draw_square(a)
t.mainloop()
'''

##   Ứng dụng quản lý chi tiêu cá nhân'''
'''
expenses=[]
def add_item(myTempList, item):
    myTempList.append(item)
def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result
def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")
print("Your expenses:", expenses)
print("What do you want to do? -\n"\
        "1. Add\n" \
        "2. Remove")
option = int(input("Select option 1 or 2: "))
name_input = input("Item name: ")
if option == 1:
    cost_input = int(input("Item cost: "))
    date_input = input("Date: ")
    item = {'name': name_input, 'cost':cost_input, 'date':date_input}
    add_item(expenses, item)
    print("Your expenses: ", expenses)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses: ", expenses)
else:
    print("Invalid input")
'''

### Đếm số ký tự trong chuỗi sử dụng hàm ###
'''
def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result
input_str = input('Your string: ')
print('Length: ', count_chars(input_str))
'''

### Sắp xếp các số nguyên ###
'''
def sort_numbers(num1,num2,num3):
    temp=0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return (num1,num2,num3)
x,y,z=map(int,input().split())
a,b,c=sort_numbers(x,y,z)
print("Original numbers: ", x, y, z)
print("Sorted numbers: ", a, b, c)
'''

###  Tìm giá trị nhỏ nhất trong danh sách ###
'''
def get_min_numbers(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result
numbers=[1,2,4,-9,4]
min_number = get_min_numbers(numbers)
print("Min number: ", min_number)
'''
