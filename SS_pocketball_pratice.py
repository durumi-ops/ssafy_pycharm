
"""import math

def cal(x1,y1,x2,y2):
    a = y1+y2
    b = x2-x1
    tan_theta = b/a
    theta = math.atan(tan_theta)
    return theta

print(math.degrees(cal(1,1,3,5))) """



import math

def cal_degree(x1,y1,x2,y2):
    w = abs(x2-x1)
    h = abs(y2-y1)
    tan_theta = h/w
    theta = math.atan(tan_theta)
    degree_theta = math.degrees(theta)
    return degree_theta

def distance(x1,y1,x2,y2):
    w = abs(x2-x1)
    h = abs(y2-y1)
    dis = math.sqrt (w**2+h**2)
    return dis

print(f'두 공 사이의 거리 = {distance(10,10,90,70)}')
print(f'각도 = {cal_degree(10,10,90,70)}')