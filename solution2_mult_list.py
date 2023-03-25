
# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list_of_numbers):
    product = 1

    for i in list_of_numbers:
      
        product = product * i
        print(product)


    return product

list_of_num1 = [ 1, 2, 3, 4, 5 ]
list_of_num2 = [ 10, 10, 10, 10, 2 ]

print(f'The product of all numbers is  {mult_list(list_of_num1)}')
print(f'The product of all numbers is  {mult_list(list_of_num2)}')


        


# Write a Python function called add_list() to add all the numbers in a list.