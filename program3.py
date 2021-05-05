number_list =[]
n = int(input("Enter the number of elements:\n"))

for i in range(0,n):
    print("Enter the number",i+1)
    ele = int(input())
    number_list.append(ele)

print("The user list is:", number_list)

number_list.sort()
print("List in ascending order:", number_list) #Print number in ascending order

number_list.sort(reverse=True)
print("List in desecnding order is:", number_list) #Print number in descending order

total = sum(number_list) #Print a sum of all the elements in the list
print("Sum of all elements in list:", total)

minimum = min(number_list) #Print the minimum of all the elements in the list
print("The minimum number in the list is:",minimum)

unique = set(number_list) #Print unique values available in the list
print("The unique number in the list is:", unique)
