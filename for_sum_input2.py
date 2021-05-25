#어떤수를 입력하고 그 수까지의 합을 구한다.

N = int(input('수를 입력하세요 :'))
a = 0

for i in range(N+1) :
    a += i
print('1부터',N,'까지의 합은',a)
print('1부터 {}까지의 합은 {}'.format(N, a))

print(f'1부터 {N}까지의 합은 {a}')

