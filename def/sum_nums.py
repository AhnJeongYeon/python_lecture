# def greet(*m):
#     for n in m:
#         print(f({n}개의 인자 {*m})) 


def sum_nums(*args):
    data = 0
    for i in args:
        data += i
    data_mean = data / len(args)
    return data, data_mean

a, b = sum_nums(10 , 20 , 30)
print(f"합은 : {a} , 평균은 {b}")
a, b = sum_nums(10 , 20 , 30 , 40 , 50)
print(f"합은 : {a} , 평균은 {b}")
