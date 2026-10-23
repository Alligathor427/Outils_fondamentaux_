import sys

epsilon = 1.0
while 1.0 + epsilon / 2 != 1.0:
    epsilon = epsilon / 2

print(epsilon)
print(sys.float_info.epsilon)
print(epsilon == 2 ** -52)