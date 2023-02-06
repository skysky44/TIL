# import sys
# sys.stdin = open('input.txt')
sms = input()
happy = ':-)'
sad = ':-('
cnt_happy = sms.count(happy)
cnt_sad = sms.count(sad)
if cnt_happy == 0 and cnt_sad == 0:
    print('none')
elif cnt_happy == cnt_sad:
    print('unsure')
elif cnt_happy > cnt_sad:
    print('happy')
elif cnt_happy < cnt_sad:
    print('sad')
