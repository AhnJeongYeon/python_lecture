# selected = None
# while selected not in ['가위','바위','보']:
#     selected = input('가위, 바위, 보 중에서 선택하세요>')
# print('선택한 값은:', selected)


# selected = None
# computer = '가위'
# while selected not in ['가위','바위','보']:
#     selected = input('가위, 바위, 보 중에서 선택하세요>')
#     if(selected == '가위' or selected = '바위' or selected == '보'):
#          if (selected == '바위'):
#             selected == selected
#             print('U win')
#         else : 
#             selected == None
#             print('이길때까지 못나와')
#     else :
#         print("가위,바위,보 중에서 선택하시오")

selected = None
com_selected = '가위'
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에서 선택하세요> ')
    if(selected == '가위' or selected == '바위' or selected == '보' ):
        if(selected =='바위'):
            selected==selected
            print('U WIn')
        else:
            selected = None
            print('이길떄까지 못나와')
    else:
        print("가위 바위 보중에 하나 선택하세요")