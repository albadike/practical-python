"""
Common applications:

Use in callback functions.
Delayed evaluation.
Decorator functions (later).
"""
    
 
def add(x, y):
    def do_add():   # Closure
        print('Adding', x, y)
        return x + y
    return do_add

# Delayed evaluation
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
    
def greeting():
    print('Hello Guido')


def main():
    add_func = add(5, 3)
    # print(add_func)     # <function add.<locals>.do_add at 0x109db58a0>
    print(add_func())
    
    print(after(5, greeting))


if __name__ == "__main__":
    main()
