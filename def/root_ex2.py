def root_ex(a,b,c):
    x_1 =(-b + (b**2-4*a*c)**0.5)/(2*a)
    x_2 =(-b - (b**2-4*a*c)**0.5)/(2*a)

    return x_1, x_2

a = int(input('이차항의 개수'))
b = int(input('일차항의 개수'))
c = int(input('상수의 개수')) 

root_ex(a,b,c)


x1 , x2 = root_ex(a,b,c)
print(f'해는 {x1} 또는 {x2}')