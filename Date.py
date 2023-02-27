# AsHMagic이 제작 하였습니다.
# 감사합니다 :)


import datetime

day = datetime.datetime.now()

scan = str(input('날짜 더하기 혹은 빼기를 써주세요: '))

if scan == "더하기":
    date = int(input('더하실 날짜를 적어주세요(숫자만): '))
    dayplus = day + datetime.timedelta(days=date)
    print(dayplus)

elif scan == "빼기":
    date = int(input('빼실 날짜를 적어주세요(숫자만): '))
    dayminus = day - datetime.timedelta(days=date)
    print(dayminus)
