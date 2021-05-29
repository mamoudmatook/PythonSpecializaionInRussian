import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

cc = math.sqrt((b**2) - (4 * a * c))
print(int ((-b + cc)  / (2 * a) ) )
print(int ( (-b - cc)  / (2 * a) ) )


