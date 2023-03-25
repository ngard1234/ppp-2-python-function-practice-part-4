# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.

def pascal(n):
    #print Row 1 Position 1 : alway equal to 1
    if n>= 1:
        print('1')
    #create list to store posistion values. seeded with row 2 values needed to start calculations
    # two list one to read and on to write. Once the numbers for the prior row is on the Write List , 
    # it is then transfered to the Read List, so it's not overwritten. Then the Write List is reset to [1, 1]
    # [1, 1 ] represent the 1st and the last numbers in each row.
    row_pos_read = [ 1, 1 ]
    row_pos_write= [ 1, 1 ]
    if n>= 2:
        print("1 1 ")
    #loop for number of row  minus row 1 & row 2. loop starts at row 3 to row n+1.
      
    for row in range (3, n+1):
        #print first position 1, which is alway 1 in all rows.
        print('1', end=" ")
        
     
        for i in range(0, row-2): 
            row_pos_write.insert(i+1,(row_pos_read[i] + row_pos_read[i+1]))
           
            print(row_pos_write[i+1], end=" ")
        
        #print last position nth, which is alway 1 in all row.
        print('1')
        row_pos_read = row_pos_write
        # print(row_pos_read)
        row_pos_write=[ 1, 1 ]
        

    
pascal(7)
        
