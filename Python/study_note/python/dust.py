dust = 100

# 조건문 작성

if dust > 150:
    print('매우나쁨')
elif dust > 80 and dust <= 150:
    print('나쁨')
elif dust > 30 and dust <= 80:
    print('보통')
else:
    print('좋음')
