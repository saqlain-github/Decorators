def decorate_it(func):
    def adding_extra_behavior():
        print("*"*10)
        func()
        print("*"*10)
        
    return adding_extra_behavior


def decorate_it_args(func):
    def adding_extra_behavior(*args,**kargs):
        print("*"*10)
        func(*args,**kargs)
        print("*"*10)
        
    return adding_extra_behavior


def decorate_it_with_args_return(func):
    def adding_extra_behavior(*args,**kargs):
        print("*"*10)
        result = func(*args,**kargs)
        print("*"*10)
        return result
    
    return adding_extra_behavior


def multi_decorator_inner(func):
    def multi(*args,**kwargs):
        print("i"*10)
        result = func(*args,**kwargs)
        print("i"*10)
        return result
    
    return multi

def multi_decorator_outer(func):
    def multi(*args,**kwargs):
        print("o"*10)
        result = func(*args,**kwargs)
        print("o"*10)
        return result
    
    return multi
