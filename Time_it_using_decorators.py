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
