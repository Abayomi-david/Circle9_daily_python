# # Making use of decorators and inbuilt time module
  # # 1st sol without decorator 
# import time
# start_time = time.time()

# x = sum(range(1,1000001))
# print(f"Sum of 1 to 1,000,000 is: {x}")

# end_time = time.time()

# time_used = end_time - start_time
# print(f"Time taken to sum up 1 to 1,000,000 is:{time_used}secounds")
 # # 2ND sol filled error
# start_time = time.time()
# end_time = time.time()

# def time_it(Operation):
#     def time_used():
#       start_time
#     operation()  
#     end_time
#     time_used = end_time - start_time 

#     print(f"Time taken to sum up 1 to 1,000,000 is:{time_used}secounds")

# @time_it
# def operation():
#     x = sum(range(1,1000001))
#     print(f"Sum of 1 to 1,000,000 is: {x}")

# operation()   
 # Final solution

import time  

def time_it(operation):
    def wrapper():  
        start_time = time.time()  
        operation()  
        end_time = time.time()  
        time_used = end_time - start_time  
        
        print(f"Time taken to sum up 1 to 1,000,000 is: {time_used} seconds")

    return wrapper  

@time_it  
def operation():
    x = sum(range(1, 1000001))
    print(f"Sum of 1 to 1,000,000 is: {x}")

operation()  

# Help from ai
import time

# Define the decorator to measure execution time
def time_it(func):
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        
        # Call the original function and store the result
        result = func(*args, **kwargs)
        
        # Record the end time
        end_time = time.time()
        
        # Calculate and print the time taken
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.5f} seconds to run.")
        
        # Return the result of the original function
        return result
    return wrapper

# Apply the time_it decorator to a function
@time_it
def sum_of_numbers():
    total = sum(range(1, 1000001))  # Sum of numbers from 1 to 1 million
    return total

# Call the decorated function
sum_of_numbers()

# checking
def f1():
    print("i am here")

def my_name():
    print("Abayomi David")

def f2(f):
    f()

f2(f1)
f2(my_name)

def sum(a,b):
    print(a+b)

sum(a=2,b=4)

def name():
    print("david")

def name_caller(ww):
    ww()


name_caller(name)