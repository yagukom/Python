#以下内容来自《自学是门手艺--李笑来》3.2.3函数工具 最后的装饰器内容。
#即当被@修饰器所修饰的函数具有多个参数需要传入修饰器函数时，在修饰器函数内部需要使用*及**来接收这些参数。
#2021-1-22 15:46
def trace(func):  #步骤三
    def wrapper(*args, **kwargs):   #步骤五：  *为位置参数，**为关键字参数
        print(f"Trace: You've called a function: {func.__name__}(),",
              f"with args: {args}; kwargs: {kwargs}")

        original_result = func(*args, **kwargs)
        print(f"Trace: {func.__name__}{args} returned: {original_result}")
        return original_result  #步骤六，最后的步骤。
    return wrapper  #步骤四

@trace  #步骤二
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'

print(say_hi('Hello', name = 'Jack')) #步骤一
