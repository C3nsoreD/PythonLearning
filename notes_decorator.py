
def logging(func):
    def log_fucntion_called():
        print(f'{func} called.')
        func()
    return log_fucntion_called


if __name__ == "__main__":
    @logging
    def my_name():
        print('Gabriel')
    
    @logging
    def friend_name():
        print('John')

    my_name()
    friend_name()

    
