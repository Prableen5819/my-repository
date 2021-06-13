def solution(list_len, ele, fibonacci_list):
    result_list = []
    
    for i in fibonacci_list:
        if (ele == i):
            print(ele, 'already lies in the series')
            break
    else:
        for y in fibonacci_list:
            result = abs(ele - y)
            result_list.append(result)
                
        difference = min(result_list)
        for i in fibonacci_list:
            if ((ele + difference) == i):
                print('After adding difference of ',difference, 'to', ele, ',',ele, 'now lies in the series.')
            elif ele - difference == i:
                print('After subtracting difference of ',difference, 'from', ele, ',',ele, 'now lies in the series.')
        else:
            print(' ')
                
                
no_of_terms = int(input('Enter the number of terms: '))
    
a = -1
b = 1
i = 1
    
fibonacci_list = []
    
while i <= no_of_terms:
    c = a + b
    fibonacci_list.append(c)
    a = b
    b = c
    i = i + 1
        
print(fibonacci_list)
    
ele = int(input('Enter the number to find in the list :'))
    
solution(list_len, ele, fibonacci_list)
        
    




