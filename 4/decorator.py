
def announce(f):
    def wrapper():
        print('About to launch the function')
        f()
        print('End of the function')
    return wrapper


@announce
def hello():
    print('Hello world')


hello()