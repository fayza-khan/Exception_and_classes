x = int(input())
y = int(input())
try:
    z = x / y
except ZeroDivisionError as e:
    print('exception occurred:', e)
    z = None
except Exception as e:
    print('exception type:', type(e).__name__)
    z = None
print("Division is:", z)
