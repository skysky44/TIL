from collections import deque
T = int(input())
for _ in range(T):
    parenthesis = deque(list(input()))
    stack = []
    while len(parenthesis) > 0:
        p = parenthesis.popleft()
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                stack.append(p)  # 이렇게 안하면 마지막에 ')'하나일때 print('YES')나옴
                break
            else:
                stack.pop()

    if len(parenthesis) == 0 and len(stack) == 0:
        print('YES')
    else:
        print('NO')


# if 뒤에 리스트: 하면 리스트가 비어있으면  0이고 안비어있으면 1인듯


# 실패한 코드
# T = int(input())
# for _ in range(T):
#     parenthesis = list(input())
#     stack = []
#     for p in parenthesis:
#         if p == '(':
#             stack.append(p)
#         elif p == ')':
#             try:
#                 if stack.pop() == '(':
#                     pass

#                 else:
#                     print('NO')
#                     break
#             except:
#                 print('NO')
#                 break
