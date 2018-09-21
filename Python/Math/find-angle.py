import math

ab = float(input())
bc = float(input())
print('{}\xb0'.format(round(math.degrees(math.atan2(ab,bc)))))
