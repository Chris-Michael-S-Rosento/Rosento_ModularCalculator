Number_1 = int(input("Enter Number_1: "))
Number_2 = int(input("Enter Number_2: "))

print("Choose operation: 1-Addition 2-Subtraction 3-Multiplication 4-Division")

Operation = int(input("Enter the operation: "))

if Operation == 1:
 Add_num = (Number_1 + Number_2)
 print(Add_num)

if Operation == 2:
 Subtract_num = (Number_1 - Number_2)
 print(Subtract_num)
if Operation == 3:
 Multiply_num = (Number_1 * Number_2)
 print(Multiply_num)
if Operation == 4:
 Divide_num = (Number_1/Number_2)
 print(Divide_num)
