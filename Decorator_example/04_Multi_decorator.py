from decorators import multi_decorator_inner, multi_decorator_outer


# def multi_decorator_inner(func):
#     def multi(*args,**kwargs):
#         print("i"*10)
#         result = func(*args,**kwargs)
#         print("i"*10)
#         return result
    
#     return multi

# def multi_decorator_outer(func):
#     def multi(*args,**kwargs):
#         print("o"*10)
#         result = func(*args,**kwargs)
#         print("o"*10)
#         return result
    
#     return multi


@multi_decorator_outer
@multi_decorator_inner
def print_name(name):
    return print(f"{name}")

print_name("saqlain")