def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_function("arg1", "arg2", keyword1="value1", keyword2="value2")
