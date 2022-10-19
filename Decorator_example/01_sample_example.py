
# '''
# def decorate_it(func):
#     def adding_extra_behavior():
#         print("*"*10)
#         func()
#         print("*"*10)
        
#     return adding_extra_behavior


# def print_name():
#     print("Hi, From Saqlain")


    
# print_name()

# '''
# Two ways to add functionality to existing function
# '''

# # First way(easy way)

# my_name = decorate_it(print_name)
# my_name()
# '''

# # Second way 

from decorators  import  decorate_it

@decorate_it
def print_name():
    print("Hi, From Saqlain")
    
print_name()

@decorate_it
def print_welcome():
    print("Welcome to my youtube channel")
    
print_welcome()