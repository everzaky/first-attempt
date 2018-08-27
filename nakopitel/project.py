import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def ver7_11_1(Potreblenie, Prisoed_moshnost, KPD, Tsikli_Zar_i_Razradki, Stoimost_emkosti_nakop, Stoimost_PG,
              Stoimost_PT, Stoimost_podkl, pik_chasi, CK, Energy_price):
    '''print('***Потребление***')
    print('Введите почасовой профиль в кВт*ч:')

    Potreblenie = list()

    for i in range(24):
        n = 999
        while n > 0:
            n = 0
            t = input()
            if ('.' in t) or (',' in t):
                print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
                n += 1
            elif int(t) < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Potreblenie.append(int(t))
    print('Введите присоединённую мощность:')

    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    Prisoed_Moshnost = t

    print('***Данные накопителя***')
    print('Введите КПД накопителя:')

    n = 999
    while n > 0:
        n = 0
        t = float(input())
        if t > 0:
            if t < 1:
                KPD = t
            else:
                print("ОШИБКА: КПД не может быть >= 1, повторите ввод!")
                n += 1
        else:
            print('ОШИБКА: Вы ввели отрицательное число или 0, повторите ввод!')
            n += 1


    print('Введите количество циклов зарядки и разрядки:')

    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    Tsikli_Zar_i_Razradki = t

    print('Введите стоимость ёмкости в руб/кВт*ч:')


    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    Stoimost_emkosti_nakop = t


    print('***Цены на электроэнергию***')

    print('Введите стоимость мощности генерации по ЦК 3,4,5,6:')
    Stoimost_PG = list()
    Stoimost_PG.append(0)
    Stoimost_PG.append(0)
    Stoimost_PG.append(0)
    for i in range(4):
        n = 999
        while n > 0:
            n = 0
            t = float(input())
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Stoimost_PG.append(t)

    print('Введите стоимость транспортной мощности по ЦК 4 и 6:')
    Stoimost_PT = list()
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    for i in range(2):
        n = 999
        while n > 0:
            n = 0
            t = float(input())
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Stoimost_PT.append(t)
        Stoimost_PT.append(0)


    print('Введите стоимость подключения:')

    n = 999
    while n > 0:
        n = 0
        t = float(input())
        if t >= 0:
            Stoimost_podkl = t
        else:
            print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
            n += 1

    print('Введите пиковые часы:')
    pik_chasi = list()
    for i in range(6):
        n = 999
        while n > 0:
            n = 0
            t = input()
            if str(t) not in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23':
                print('ОШИБКА: Вы ввели неверное число, повторите ввод!')
                n += 1
            else:
                pik_chasi.append(int(t))

    print('Введите свою ценовую категорию:')

    n = 999
    while n > 0:
        n = 0
        e = input()
        if e in ['3', '4', '5', '6']:
            CK = int(e)
        else:
            print('ОШИБКА: Вы ввели неверное число, повторите ввод!')
            n += 1

    print('Введите почасовую цену на электроэнергию в руб/кВт*ч:')

    Energy_price = list()
    Energy_price.append([0])
    Energy_price.append([0])
    Energy_price.append([0])
    for x in range(4):
        s = input().split()
        l = list()
        for i in s:
            n = 999
            while n > 0:
                n = 0
                t = float(i)
                if t < 0:
                    print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                    n += 1
            l.append(t)
        Energy_price.append(l)
        print()'''
    # ----------------------------------------------------------------------------------------------

    moshnosti0 = list(Potreblenie)
    Spisok = []
    Max = max(Potreblenie)
    Max0 = Max
    Min = min(Potreblenie)
    Min0 = Min
    PG_bez = 0
    PT_bez = 0
    PT = 0
    PG = 0
    for i in range(24):
        if i in pik_chasi:
            PG_bez += Potreblenie[i]
            if Potreblenie[i] > PT_bez:
                PT_bez = Potreblenie[i]
    PG_bez = PG_bez / 6
    Rashod_bez = 0  # Расход без накопителя
    for i in range(24):
        Rashod_bez += Potreblenie[i] * Energy_price[CK-3][i]
    Rashod_bez += PG_bez * Stoimost_PG
    if CK == 4 or CK == 6:
        Rashod_bez += PT_bez * Stoimost_PT
    NeZnayuKakNazvat = 0
    while max(moshnosti0) * (1 - 0.001) > min(moshnosti0) and NeZnayuKakNazvat < 10000:
        # moshnosti0 = list(Potreblenie)
        NeZnayuKakNazvat += 1
        x = 0.0001  # Насколько срезаем
        ost_moshnost = Max0 * (1 - x)  # остаточная мощность
        srez_moshnost = 0  # срезанная мощность на этом шаге
        srez_moshnost0 = 0  # абсолютная срезанная мощность
        for i in range(24):
            if Potreblenie[i] > ost_moshnost:
                srez_moshnost0 += Potreblenie[i] - ost_moshnost
            if moshnosti0[i] > ost_moshnost:
                srez_moshnost += moshnosti0[i] - ost_moshnost
                moshnosti0[i] = ost_moshnost
        Min0 = min(moshnosti0)
        Max0 = max(moshnosti0)
        C = (srez_moshnost0 / KPD) * 1.2  # Ёмкость
        i = moshnosti0.index(Min0)
        moshnosti0[i] = Min0 + srez_moshnost
        P = 0
        c = 0
        k = 0
        c0 = c
        if moshnosti0[0] < Potreblenie[0]:
            c00 = -1
        elif moshnosti0[0] > Potreblenie[0]:
            c00 = 1
        else:
            c00 = 0
        for i in range(24):
            if moshnosti0[i] < Potreblenie[i]:
                c = -1
            elif moshnosti0[i] > Potreblenie[i]:
                c = 1
            if c != c0 and c0 != 0:
                k += 1
            c0 = c
        if (c == c00 or c00 == 0)and(k > 1):
            T = int(Tsikli_Zar_i_Razradki / (k - 1))
        else:
            T = int(Tsikli_Zar_i_Razradki / k)
        for i in range(24):
            if abs(moshnosti0[i] - Potreblenie[i]) > P:
                P = abs(moshnosti0[i] - Potreblenie[i])
        P = (P / KPD) * 1.2 # Мощность накопителя
        Min0 = min(moshnosti0)
        Max0 = max(moshnosti0)
        PT = 0
        PG = 0
        for i in range(24):
            if i in pik_chasi:
                PG += moshnosti0[i]
                if moshnosti0[i] > PT:
                    PT = moshnosti0[i]
        PG = PG / 6
        Rashod = 0  # Расход с накопителем
        Rashod0 = 0
        for i in range(24):
            Rashod += moshnosti0[i] * Energy_price[CK-3][i]
        Rashod += PG * Stoimost_PG
        if CK == 4 or CK == 6:
            Rashod += PT * Stoimost_PT
        if CK == 4:
            Rashod0 += PT * Stoimost_PT
        if CK == 3 or CK == 4:
            for i in range(24):
                Rashod0 += moshnosti0[i] * Energy_price[CK - 1][i]
            Rashod0 += PG * Stoimost_PG
        # N = 365 * 10  # Количество циклов
        # CF = P * Stoimost_podkl + (Rashod_bez - Rashod) * Tsikli_Zar_i_Razradki  #Выгода
        CF = P * Stoimost_podkl + (Rashod_bez - Rashod) * 365  # Выгода
        CF0 = P * Stoimost_podkl + (Rashod_bez - Rashod0) * 365
        IC = C * Stoimost_emkosti_nakop  # Начальные инвестиции
        I = 0.12  # Ставка дисконтирования
        NPV = 0 - IC  # Ищем NPV
        for i in range(1, (T // 365) + 1):
            NPV += CF / ((1 + I) ** i)
        NPV += ((CF * (T % 365)) / 365) / ((1 + I) ** (T // 365) + 1)
        if CK == 3 or CK == 4:
            NPV0 = 0 - IC
            # for i in range(1,Tsikli_Zar_i_Razradki + 1):
            for i in range(1, (T // 365) + 1):
                NPV0 += CF0 / ((1 + I) ** i)
            NPV0 += ((CF0 * (T % 365)) / 365) / ((1 + I) ** (T // 365) + 1)
        else:
            NPV0 = -9999999999999999
        print(P)
        Spisok.append([C, P, NPV, NPV0, list(moshnosti0)])
        # print([C, P, NPV, moshnosti0])
    max_NPV = -999999999  # Максимальный NPV
    max_NPV0 = -999999999
    NPV_max = 0  # Индекс в списке, где NPV максимален
    NPV0_max = 0
    NeZnayuKakNazvat1 = 0
    NeZnayuKakNazvat2 = 0
    npv0pck=0
    pck=0
    sck=0
    npv0sck=0
    npvpck=0
    npvsck=0
    time=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    moshnostmaxpck = 0
    emkostmaxpck =0
    emkostnpv0pck= 0
    moshnostnpv0sck = 0
    moshnostmaxsck = 0
    emkostmaxsck = 0
    emkostnpv0sck = 0
    moshnostnpv0pck = 0
    for i in range(len(Spisok)):
        if (Spisok[i][2] >= 0) and (NeZnayuKakNazvat1 == 0):
            NeZnayuKakNazvat1 = 1
            answer=": да"
            print('При NPV = 0, ёмкость накопителя равна', round(Spisok[i][0], 2), 'кВт*ч, мощность накопителя равна',round(Spisok[i][1], 2), 'кВт')
            print(Spisok[i][4])
            plt.plot(time,Spisok[i][4],Potreblenie)
            plt.savefig('/static/css/npv=0pck'+'.png',format='png')
            emkostnpv0pck=round(Spisok[i][0], 2)
            moshnostnpv0pck=round(Spisok[i][1], 2)
            pck=1
            npv0pck=1
        if (Spisok[i][3] >= 0) and (NeZnayuKakNazvat2 == 0) and (CK == 3 or CK == 4):
            NeZnayuKakNazvat2 = 1
            answer = ": да"
            print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и NPV = 0, ёмкость накопителя равна',round(Spisok[i][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[i][1], 2), 'кВт')
            sck=1
            npv0sck=1
            print(Spisok[i][4])
            plt.plot(time,Spisok[i][4],Potreblenie)
            plt.savefig('/static/css/npv=0sck' + '.png', format='png')
            emkostnpv0sck=round(Spisok[i][0],2)
            moshnostnpv0sck=round(Spisok[i][0],2)
            #plt.plot(moshnosti0[i], Potreblenie)
            #plt.show()
        if (NeZnayuKakNazvat1 == 1) and (Spisok[i][2] < 0):
            NeZnayuKakNazvat1 += 1
            #answer = ": да"
            #emkostnpv0pck = round(Spisok[i][0], 2)
            #moshnostnpv0pck = round(Spisok[i][1], 2)
            #pck = 1
            #npv0 = 1
            #print('При NPV = 0, ёмкость накопителя равна', round(Spisok[i - 1][0], 2),'кВт*ч, мощность накопителя равна', round(Spisok[i - 1][1], 2), 'кВт')
        if (NeZnayuKakNazvat2 == 1) and (Spisok[i][3] < 0) and (CK == 3 or CK == 4):
            #NeZnayuKakNazvat2 += 1
            answer = ": да"
            #print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и NPV = 0, ёмкость накопителя равна',    round(Spisok[i - 1][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[i - 1][1], 2), 'кВт')
        if Spisok[i][2] > max_NPV:
            NPV_max = i
            max_NPV = Spisok[i][2]
        if Spisok[i][3] > max_NPV0 and (CK == 3 or CK == 4):
            NPV0_max = i
            max_NPV0 = Spisok[i][3]
    if Spisok == []:
        print('Вам не нужен аккумулятор')
        answer=': нет'
    else:
        if max_NPV > 0:
            answer=": да"
            print('При максимальном NPV, ёмкость накопителя равна', round(Spisok[NPV_max][0], 2),'кВт*ч, мощность накопителя равна', round(Spisok[NPV_max][1], 2), "кВт, NPV равен",round(Spisok[NPV_max][2], 2), 'руб.')
            npvpck = max_NPV
            print(Spisok[NPV_max][4])
            plt.plot(time,Spisok[NPV_max][4],Potreblenie)
            plt.savefig('/static/css/npvmaxpck' + '.png', format='png')
            emkostmaxpck=round(Spisok[NPV_max][0], 2)
            moshnostmaxpck= round(Spisok[NPV_max][1], 2)
        else:
            answer=": нет"
            print('Вам не нужен аккумулятор при данной ценовой категории')
        if CK == 3 or CK == 4 and max_NPV0 > 0:
            answer=': да'
            print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и максимальном NPV, ёмкость накопителя равна',round(Spisok[NPV0_max][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[NPV0_max][1], 2),"кВт, NPV равен", round(Spisok[NPV0_max][3], 2), 'руб.')
            npvsck=max_NPV0
            print(Spisok[NPV0_max][4])
            plt.plot(time,Spisok[NPV0_max][4],Potreblenie)
            plt.savefig('/static/css/npvmaxsck' + '.png', format='png')
            emkostmaxsck=round(Spisok[NPV0_max][0], 2)
            moshnostmaxsck=round(Spisok[NPV0_max][1], 2)
        elif ((CK == 3) or( CK == 4))and(max_NPV0 < 0):
            answer=": нет"
            print('Вам не нужно менять ценовую категорию')
    return (answer,npv0pck,pck,moshnostnpv0pck,emkostnpv0pck,npvpck,emkostmaxpck,moshnostmaxpck,npv0sck,sck,emkostnpv0sck,moshnostnpv0sck,npvsck,emkostmaxsck,moshnostmaxsck)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def ver7_11_2(Potreblenie, propusk_moshnost, KPD, Tsikli_Zar_i_Razradki, Stoimost_emkosti_nakop, Stoimost_PG,
              Stoimost_PT, Stoimost_podkl, pik_chasi, CK, Energy_price):
    ''''print('***Потребление***')
    print('Введите почасовой профиль в кВт*ч:')

    Potreblenie = list()

    for i in range(24):
        n = 999
        while n > 0:
            n = 0
            t = input()
            if ('.' in t) or (',' in t):
                print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
                n += 1
            elif int(t) < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Potreblenie.append(int(t))
    print('Введите максимальную мощность, возможную для подключения к сети:')

    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    propusk_moshnost = t

    print('***Данные накопителя***')
    print('Введите КПД накопителя:')

    n = 999
    while n > 0:
        n = 0
        t = float(input())
        if t > 0:
            if t < 1:
                KPD = t
            else:
                print("ОШИБКА: КПД не может быть >= 1, повторите ввод!")
                n += 1
        else:
            print('ОШИБКА: Вы ввели отрицательное число или 0, повторите ввод!')
            n += 1


    print('Введите количество циклов зарядки и разрядки:')

    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    Tsikli_Zar_i_Razradki = t

    print('Введите стоимость ёмкости в руб/кВт*ч:')


    n = 999
    while n > 0:
        n = 0
        t = input()
        if ('.' not in t) and (',' not in t):
            t = int(t)
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        else:
            print('ОШИБКА: Вы ввели дробное число, повторите ввод!')
            n += 1

    Stoimost_emkosti_nakop = t


    print('***Цены на электроэнергию***')

    print('Введите стоимость мощности генерации по ЦК 3,4,5,6:')
    Stoimost_PG = list()
    Stoimost_PG.append(0)
    Stoimost_PG.append(0)
    Stoimost_PG.append(0)
    for i in range(4):
        n = 999
        while n > 0:
            n = 0
            t = float(input())
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Stoimost_PG.append(t)

    print('Введите стоимость транспортной мощности по ЦК 4 и 6:')
    Stoimost_PT = list()
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    Stoimost_PT.append(0)
    for i in range(2):
        n = 999
        while n > 0:
            n = 0
            t = float(input())
            if t < 0:
                print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                n += 1
        Stoimost_PT.append(t)
        Stoimost_PT.append(0)


    print('Введите стоимость подключения:')

    n = 999
    while n > 0:
        n = 0
        t = float(input())
        if t >= 0:
            Stoimost_podkl = t
        else:
            print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
            n += 1

    print('Введите пиковые часы:')
    pik_chasi = list()
    for i in range(6):
        n = 999
        while n > 0:
            n = 0
            t = input()
            if t not in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23':
                print('ОШИБКА: Вы ввели неверное число, повторите ввод!')
                n += 1
        pik_chasi.append(int(t))

    print('Введите свою ценовую категорию:')

    n = 999
    while n > 0:
        t = input()
        n = 0
        if t in ['3','4','5','6']:
            CK = int(t)
        else:
            print('ОШИБКА: Вы ввели неверное число, повторите ввод!')
            n += 1

    print('Введите почасовую цену на электроэнергию в руб/кВт*ч:')

    Energy_price = list()
    Energy_price.append([0])
    Energy_price.append([0])
    Energy_price.append([0])
    for x in range(4):
        s = input().split()
        l = list()
        for i in s:
            n = 999
            while n > 0:
                n = 0
                t = float(i)
                if t < 0:
                    print('ОШИБКА: Вы ввели отрицательное число, повторите ввод!')
                    n += 1
            l.append(t)
        Energy_price.append(l)
        print()'''
    # ----------------------------------------------------------------------------------------------

    moshnosti0 = list(Potreblenie)
    Spisok = []
    Max = max(Potreblenie)
    Max0 = Max
    Min = min(Potreblenie)
    Min0 = Min
    PG_bez = 0
    PT_bez = 0
    PT = 0
    PG = 0
    for i in range(24):
        if i in pik_chasi:
            PG_bez += Potreblenie[i]
            if Potreblenie[i] > PT_bez:
                PT_bez = Potreblenie[i]
    PG_bez = PG_bez / 6
    Rashod_bez = 0  # Расход без накопителя
    for i in range(24):
        Rashod_bez += Potreblenie[i] * Energy_price[CK][i]
    Rashod_bez += PG_bez * Stoimost_PG[CK]
    if CK == 4 or CK == 6:
        Rashod_bez += PT_bez * Stoimost_PT[CK]
    NeZnayuKakNazvat = 0
    while NeZnayuKakNazvat < 10000 and max(moshnosti0) > 0.8 * propusk_moshnost:  # максимальная пропускная способность
        # moshnosti0 = list(Potreblenie)
        NeZnayuKakNazvat += 1
        x = 0.0001  # Насколько срезаем
        ost_moshnost = Max0 * (1 - x)  # остаточная мощность
        srez_moshnost = 0  # срезанная мощность на этом шаге
        srez_moshnost0 = 0  # абсолютная срезанная мощность    for i in range(24):
        for i in range(24):
            if Potreblenie[i] > ost_moshnost:
                srez_moshnost0 += Potreblenie[i] - ost_moshnost
            if moshnosti0[i] > ost_moshnost:
                srez_moshnost += moshnosti0[i] - ost_moshnost
                moshnosti0[i] = ost_moshnost
        Max0 = max(moshnosti0)
        Min0 = min(moshnosti0)
        C = (srez_moshnost0 / KPD) * 1.2  # Ёмкость
        i = moshnosti0.index(Min0)
        moshnosti0[i] = Min0 + srez_moshnost
        P = 0
        c = 0
        k = 0
        c0 = c
        if moshnosti0[0] < Potreblenie[0]:
            c00 = -1
        elif moshnosti0[0] > Potreblenie[0]:
            c00 = 1
        else:
            c00 = 0
        for i in range(24):
            if moshnosti0[0] < Potreblenie[0]:
                c = -1
            elif moshnosti0[0] > Potreblenie[0]:
                c = 1
            if c != c0 and c0 != 0:
                k += 1
            c0 = c
        if c == c00 or c00 == 0:
            T = Tsikli_Zar_i_Razradki / k - 1
        else:
            T = Tsikli_Zar_i_Razradki / k
        for i in range(24):
            if abs(moshnosti0[i] - Potreblenie[i]) > P and Potreblenie[i] <= propusk_moshnost:
                P = abs(moshnosti0[i] - Potreblenie[i])
            elif abs(moshnosti0[i] - Potreblenie[i]) > P and Potreblenie[i] > propusk_moshnost:
                P = abs(moshnosti0[i] - propusk_moshnost)
        P = (P / KPD) * 1.2  # Мощность накопителя
        Max0 = max(moshnosti0)
        Min0 = min(moshnosti0)
        PT = 0
        PG = 0
        for i in range(24):
            if i in pik_chasi:
                PG += moshnosti0[i]
                if moshnosti0[i] > PT:
                    PT = moshnosti0[i]
        PG = PG / 6
        Rashod = 0  # Расход с накопителем
        Rashod0 = 0
        for i in range(24):
            Rashod += moshnosti0[i] * Energy_price[CK][i]
        Rashod += PG * Stoimost_PG[CK]
        if CK == 4 or CK == 6:
            Rashod += PT * Stoimost_PT[CK]
        if CK == 4:
            Rashod0 += PT * Stoimost_PT[CK + 2]
        if CK == 3 or CK == 4:
            for i in range(24):
                Rashod0 += moshnosti0[i] * Energy_price[CK + 2][i]
            Rashod0 += PG * Stoimost_PG[CK + 2]
        # N = 365 * 10  # Количество циклов
        CF = P * Stoimost_podkl + (Rashod_bez - Rashod) * 365  # Выгода
        CF0 = P * Stoimost_podkl + (Rashod_bez - Rashod0) * 365
        IC = (Rashod / 24) + C * Stoimost_emkosti_nakop  # Начальные инвестиции
        I = 0.12  # Ставка дисконтирования
        NPV = 0 - IC  # Ищем NPV
        for i in range(1, (T // 365) + 1):
            NPV += CF / ((1 + I) ** i)
        NPV += ((CF * (T % 365)) / 365) / ((1 + I) ** (T // 365) + 1)
        if CK == 3 or CK == 4:
            NPV0 = 0 - IC
            # for i in range(1,Tsikli_Zar_i_Razradki + 1):
            for i in range(1, (T // 365) + 1):
                NPV0 += CF0 / ((1 + I) ** i)
            NPV0 += ((CF0 * (T % 365)) / 365) / ((1 + I) ** (T // 365) + 1)
        else:
            NPV0 = -9999999999999999
        Otnoshenie = ost_moshnost / propusk_moshnost
        Spisok.append([C, P, NPV, NPV0, Otnoshenie])
        # print([C, P, NPV])
    max_NPV = -9999999999  # Максимальный NPV
    max_NPV0 = -9999999999
    NPV_max = 0  # Индекс в списке, где NPV максимален
    NPV0_max = 0
    NeZnayuKakNazvat1 = 0
    NeZnayuKakNazvat2 = 0
    for i in range(len(Spisok)):
        if (Spisok[i][2] >= 0) and (NeZnayuKakNazvat1 == 0):
            NeZnayuKakNazvat1 = 1
            print('При NPV = 0, ёмкость накопителя равна', round(Spisok[i][0], 2), 'кВт*ч, мощность накопителя равна',
                  round(Spisok[i][1], 2), 'кВт')
        if (Spisok[i][3] >= 0) and (NeZnayuKakNazvat2 == 0) and (CK == 3 or CK == 4):
            NeZnayuKakNazvat2 = 1
            print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и NPV = 0, ёмкость накопителя равна',
                  round(Spisok[i][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[i][1], 2), 'кВт')
        if (NeZnayuKakNazvat1 == 1) and (Spisok[i][2] < 0):
            NeZnayuKakNazvat1 += 1
            print('При NPV = 0, ёмкость накопителя равна', round(Spisok[i - 1][0], 2),
                  'кВт*ч, мощность накопителя равна', round(Spisok[i - 1][1], 2), 'кВт')
        if (NeZnayuKakNazvat2 == 1) and (Spisok[i][3] < 0) and (CK == 3 or CK == 4):
            NeZnayuKakNazvat2 += 1
            print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и NPV = 0, ёмкость накопителя равна',
                  round(Spisok[i - 1][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[i - 1][1], 2), 'кВт')
        if Spisok[i][2] > max_NPV:
            NPV_max = i
            max_NPV = Spisok[i][2]
        if Spisok[i][3] > max_NPV0 and (CK == 3 or CK == 4):
            NPV0_max = i
            max_NPV0 = Spisok[i][3]
    if Spisok == []:
        print('Вам не нужен аккумулятор')
    else:
        if max_NPV > 0:
            print('При максимальном NPV, ёмкость накопителя равна', round(Spisok[NPV_max][0], 2),
                  'кВт*ч, мощность накопителя равна', round(Spisok[NPV_max][1], 2), "кВт, NPV равен",
                  round(Spisok[NPV_max][2], 2), 'руб.')
        else:
            print('Вам не нужен аккумулятор при данной ценовой категории')
        if CK == 3 or CK == 4 and max_NPV0 > 0:
            print('При переходе с ценовой категории', CK, 'на', CK + 2, 'и максимальном NPV, ёмкость накопителя равна',
                  round(Spisok[NPV0_max][0], 2), 'кВт*ч, мощность накопителя равна', round(Spisok[NPV0_max][1], 2),
                  "кВт, NPV равен", round(Spisok[NPV0_max][3], 2), 'руб.')
        elif CK == 3 or CK == 4:
            print('Вам не нужно менять ценовую категорию')
    input('Press Enter')
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

