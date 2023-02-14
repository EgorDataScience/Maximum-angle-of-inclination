import math
rad = 360/(2*math.pi)
f = input()
x = 0
n = 1000
d = 0

for i in range(n):                        
    x = x + 1
    y1 = eval(f)
    x = x + 1
    y2 = eval(f)
    r = (math.atan(abs(y2-y1)) * rad )    #r = the result is at one point
    d = d + r                             #d = sum of results
print(d/n)                                #d/n = the limit value of the angle of inclination
    


