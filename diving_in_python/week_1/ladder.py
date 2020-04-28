import sys

a = int(sys.argv[1])
for i in range(a):
    print(" " * (a - (i + 1)) + "#" * (i + 1))
