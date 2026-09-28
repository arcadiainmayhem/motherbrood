from core.utilities import scale , deadband

    

a = scale(3980, 120, 3980, 1, 0)
b = scale(2050, 120, 3980, 10, 20)


c = deadband(2813 , 2811 , 8)
d = deadband(2805 , 2811 , 8)
e = deadband(2900 , 2900 , 8)
f = deadband(2902 , 2911 , 8)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
