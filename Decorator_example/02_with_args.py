
# def decorate_it_args(func):
#     def adding_extra_behavior(*args,**kargs):
#         print("*"*10)
#         func(*args,**kargs)
#         print("*"*10)
        
#     return adding_extra_behavior



from decorators import decorate_it_args
@decorate_it_args
def print_name(name):
    print(f"Hi, From {name}")

print_name("Saqlain")
print_name("Channcel")
