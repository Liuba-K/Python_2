duration = int(input("введите время в секундах"))
if 0 <= duration < 60:
    print (duration, " сек")
elif 60 <= duration < 3600:
    second = duration % 60
    minute = duration // 60
    print(minute, ' мин', second, ' сек')
elif 3600 <= duration < 60**3:
    hour = duration // 3600
    second = duration % 3600 % 60
    minute = duration % 3600 // 60
    print(hour, ' час', minute, ' мин', second, ' сек')
elif 60**3 < duration:
    day = duration // (24*3600)
    hour = (duration % (24*3600)) // 3600
    minute = ((duration % (24*3600)) % 3600) // 60
    second = (duration - 3600 * hour) % 60
    print(day, ' дн', hour, ' час', minute, ' мин', second, ' сек')
else:
    print('данные введены не корректно')
