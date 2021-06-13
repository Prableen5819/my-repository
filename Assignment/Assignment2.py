basket_list = []
sum = 0
counter = 0

max_weight_basket = int(input('Enter the maximum weight a basket can hold : '))

n = int(input('Enter the number of elements : '))
for i in range(0,n):
    ele = int(input('Enter element :'))
    basket_list.append(ele)  
basket_list.sort()
print('Sorted basket_list :',basket_list)

group_of_fruits = max(basket_list)
print('Weight of the group of fruits :',group_of_fruits)

remaining_weight = max_weight_basket - group_of_fruits

for i in basket_list:
    sum = sum + i
    if sum>remaining_weight:
       break
    counter = counter + 1
    
print('Maximum number of fruits that can be added to the basket without breaking it is : ',counter)        

    