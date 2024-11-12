def find_maximum(numbers):
    if not numbers:  
        return None
    
    maximum = numbers[0]  
    for num in numbers:
        if num > maximum:
            maximum = num  
    return maximum

numbers_list = [2,6,1,8,2,9,2,5,6]
print("The maximum number is:", find_maximum(numbers_list))