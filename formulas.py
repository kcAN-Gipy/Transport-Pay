# Формулы для подсчета и сравнения

import priceBase as pb

# Только подорожник
only = pb.mb * 2 * int(pb.day)

# Подорожник + 5 дней
onlyDay5 = (pb.mb + int(pb.day5)) * int(pb.week)

# Подорожник + 3 дня + 1 день
day31 = ((pb.mb * 2) + int(pb.day1 + pb.day3)) * int(pb.week)

# Подорожник + 3 дня (понедельник 77 + 77, пятница 77 + 77, четверг 77)
only3 = ((pb.mb * 2) + (pb.mb * 2) + pb.mb + int(pb.day3)) * int(pb.week)

# Результат
res = [only, onlyDay5, day31, only3, 3255]

def result():
    if res[0] == min(res):
        print('Только подорожник - ', min(res))
    elif res[1] == min(res):
        print('Подорожник и проездной на 5 дней - ', min(res))
    elif res[2] == min(res):
        print('Подорожник и проездной на 3 дня, и на 1 день - ', min(res))
    elif res[3] == min(res):
        print('Подорожник и проездной на 3 дня - ', min(res))
    else:
        print('Единый проездной за - ', min(res))