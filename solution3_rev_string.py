# Write a Python function called rev_string() to reverse a string.

#Method 1

def rev_string(string):
    # reverse now become a iterable object.
    reverse = reversed(string)
    #print: give the reference memory address of the object
    print (reverse)
    

    for i in reverse:
        print (i)

    #we have to use the join() method to constitute each element back into one string.
    new_string = "".join(reversed(string))
    return new_string 

string = 'solution'

print(f'The original string is ', string)
print(f'The new reversed string is now' ,rev_string(string))


#method 2

def reverse(string):
    str = ""
    for i in string:
        #str add the next letter/string infront of the previous letter.
        str = i + str
        print(str)
    return str
 
string = "Solution"
 
print("The original string is : ", string)
print("The new reversed string(using iteration loop) is now: ", reverse(string))

