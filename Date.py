# AsHMagic이 제작 하였습니다.
# 감사합니다 :)


import datetime

day = datetime.datetime.now()

유무 = str(input('날짜 더하기 혹은 빼기를 써주세요: '))

if 유무 == "더하기":
    날짜 = int(input('더하실 날짜를 적어주세요(숫자만): '))
    dayplus = day + datetime.timedelta(days=날짜)
    print(dayplus)

elif 유무 == "빼기":
    날짜 = int(input('빼실 날짜를 적어주세요(숫자만): '))
    dayminus = day - datetime.timedelta(days=날짜)
    print(dayminus)
