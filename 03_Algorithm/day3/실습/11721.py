words = input()
for i in range(len(words)//10):
    print(words[i*10:i*10+10])
if len(words) % 10 != 0:
    print(words[-(len(words) % 10):])
