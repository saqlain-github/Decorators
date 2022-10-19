
# def decorate_it_with_args_return(func):
#     def adding_extra_behavior(*args,**kargs):
#         print("*"*10)
#         result = func(*args,**kargs)
#         print("*"*10)
#         return result
#     return adding_extra_behavior

from decorators import decorate_it_with_args_return

@decorate_it_with_args_return
def print_name(name):
    print("Hi, From {name}")
    return "welcome to my github"
    
result = print_name("Saqain")
print(result)