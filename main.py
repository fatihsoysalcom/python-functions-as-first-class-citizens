# 1. Assigning a function to a variable
def say_hello(name):
    """A simple function to greet someone."""
    return f"Hello, {name}!"

# In Python, functions are first-class citizens, meaning they can be assigned to variables.
# This is like assigning any other value (e.g., a number or a string).
my_greeting_function = say_hello
print(f"1. Function assigned to a variable: {my_greeting_function('Alice')}")


# 2. Passing a function as an argument to another function
def execute_function(func, *args, **kwargs):
    """A higher-order function that takes another function and its arguments, then executes it."""
    print(f"\n2. Executing function '{func.__name__}' passed as an argument:")
    return func(*args, **kwargs)

# We can pass 'say_hello' (or 'my_greeting_function') as an argument to 'execute_function'.
result_from_arg = execute_function(say_hello, "Bob")
print(f"   Result: {result_from_arg}")

# Let's try with another function
def add(a, b):
    return a + b

result_add = execute_function(add, 5, 3)
print(f"   Result from add: {result_add}")


# 3. Returning a function from another function
def create_greeter(greeting_word):
    """
    A function that acts as a factory, returning a new function.
    The returned function 'remembers' the 'greeting_word' from its creation context (closure).
    """
    def greeter(name):
        return f"{greeting_word}, {name}!"
    # The inner function 'greeter' is returned, not its result.
    return greeter

# We call 'create_greeter' to get a new function.
# This demonstrates that functions themselves can be the return value.
english_greeter = create_greeter("Hello")
spanish_greeter = create_greeter("Hola")
french_greeter = create_greeter("Bonjour")

print("\n3. Functions returned from other functions:")
print(f"   English: {english_greeter('Charlie')}")
print(f"   Spanish: {spanish_greeter('David')}")
print(f"   French: {french_greeter('Eve')}")

# We can also directly call the returned function
print(f"   Direct call: {create_greeter('Hi')('Frank')}")
