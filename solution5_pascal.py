# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.

def pascal(n):
    #print Row 1 Position 1 : alway equal to 1
    if n>= 1:
        print('1')
    #create list to store posistion values. seeded with row 2 values needed to start calculations
    row_pos = [ 1, 1]
    if n>= 2:
        print("1 1 ")
    #loop for number of row  minus row 1 & row 2.
    
    for i in range( n-2):
        #print row(nth) position 1, which is alway 1.
        print('1', end=" ")

        for i in range(0, n-2, 1):
            row_pos.insert(i+1,(row_pos[i] + row_pos[i+1]))
            print(row_pos[i+1], end=" ")
           
          

        #print row(nth) position nth, which is alway 1.
        print('1')

    
    
  

pascal(3)
        
