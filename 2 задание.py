import re
import requests


def get_adr(new_adr, seen):

    words = {
             q[6:len(q) - 1]
             for i in range(len(new_adr))
             for text in requests.get(new_adr[i]).text.split(' ')
             for q in re.findall("href='http://www\.world-art\.ru.+'", text)
            }

    new_adr = [x for x in words if x not in seen]

    for x in words:
        if x not in seen:
            seen.append(x)
            print(x)               #
    print('Новых ', len(new_adr))  #
    print('Всего ', len(seen))     #

    if len(new_adr) > 0:
        get_adr(new_adr, seen)

    else:
        put = open("all_world-art.txt", "w", encoding='utf-8')
        put.write('\n'.join(seen))
        put.close()
        adr_mail(seen)


def adr_mail(с):

    words = {
             q
             for gr_1 in range(len(c))
             for text in requests.get(c[gr_1]).text.split(' ')
             for q in re.findall('[\w.][\w.]+@\w+\.\w+', text)
            }
    viv = open("почты_world-art.txt", "w", encoding='utf-8')
    viv.write('\n'.join(words))
    viv.close()


get_adr(new_adr=['http://www.world-art.ru/'], seen=['http://www.world-art.ru/']))