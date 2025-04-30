
from math import sqrt

a, b, c = list(map(int, input('Enter a, b, c : ').split()))
print(f'{a}x² + {b}x + {c} = 0')

d = b**2 - 4 * a * c

if d == 0:
    print('Real repeated roots:', -b / (2 * a))
elif d > 0:
    print('Real roots:', (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))
else:
    X = -b / (2 * a)
    Y = sqrt(-d) / (2 * a)
    print('Complex roots:', complex(X, Y), complex(X, Y))