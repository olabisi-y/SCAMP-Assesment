print('''
Good Day SCA, 

Below is my Recursive Fibonacci Sequence program. 

It will be honoured to be among the selected for the mentorship program.

Thank you.
''')

def fibonacci(n):
    if n < 2:
        return n
    else:
        return (fibonacci(n-2) + fibonacci(n-1))

for n in range(0, 21):
    print(n, ":", fibonacci(n))