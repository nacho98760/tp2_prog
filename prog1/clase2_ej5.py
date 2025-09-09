
import math

"""
es_oblongo = lambda n : int(math.sqrt(n)) * (int(math.sqrt(n)) + 1) == n

print(es_oblongo(42))
print(es_oblongo(22))
print(es_oblongo(20))
"""

es_triangular = lambda n : (math.sqrt((n * 8) + 1 )).is_integer()

print(es_triangular(10))
print(es_triangular(15))
print(es_triangular(6))
print(es_triangular(17))
print(es_triangular(34))
print(es_triangular(28))