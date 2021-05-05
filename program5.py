num_list_1 = []
num_list_2 = []
n = int(input("Enter the element value:"))

for i in range (0,n):
    print("Enter the number:", i+1)
    ele=int(input())
    num_list_1.append(ele)

print("The first list is:",num_list_1)

print("Enter values for second list")

for i in range(0,n):
    print("Enter the number:",i+1)
    ele1=int(input())
    num_list_2.append(ele1)

print("The second list is:",num_list_2)

a= set(num_list_1)
b= set(num_list_2)

print("List 1 as set1:",a)
print("List 2 as set2:",b)

print("Intersection is:",a & b)
print("Diff b/w list1 and list 2:",a-b)
print("Diff b/w list 2 and list 1 :",b-a)





