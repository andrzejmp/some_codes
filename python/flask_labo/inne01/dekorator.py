def new_decorator(func):
    def wrap_func():
        print('aaaaaaaaaaaa')
        func()
        print('cccccccccccc')
    return wrap_func

#@new_decorator
def func_needs_decoration():
    print('bbbbbbb')


func_needs_decoration = new_decorator(func_needs_decoration)
func_needs_decoration()

print(__name__)