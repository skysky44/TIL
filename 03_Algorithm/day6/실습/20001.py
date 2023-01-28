start = input()
if start == '고무오리 디버깅 시작':
    problem = []
    while True:
        shout = input()
        if shout == '문제':
            problem.append(shout)
        elif shout == '고무오리':
            if problem:
                problem.pop()
            else:
                problem.append('문제')
                problem.append('문제')
        elif shout == '고무오리 디버깅 끝':
            if problem:
                print('힝구')
            else:
                print('고무오리야 사랑해')
            break
