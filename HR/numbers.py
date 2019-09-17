"""
Algorithm

Framkvæmd:
1. Leysa báða parta í sitthvoru lagi og púsla svo saman
2. áður en byrjað er á mission 1 & 2 þá er tekið input fra user

Mission 1
---------
Finnur og skrifar út allar pósítívar tveggja stafa tölur sem eru þannig að
annað veldi af summu einstakra tölustafa er jafnt tölunni sjálfri.
---------
búa til counter
búðu til while loop sem að prufar tölur frá 10-99
    taka fyrsta tölustafinn í tölunni og seinni tölustafinn í tölunni
    plúsa fyrstu töluna og seinni töluna saman
    setja þá tölu í annað veldi og kíkja hvort hún sé sú sama og fyrsta talan sem að kom inn
    ef svo er, prenta hana út

Mission 2
---------
Finnur og skrifar út allar pósítivar tölur < 100 sem eiga sér nákvæmlega
10 deila (e. divisors)
---------
búa til counter
búa til while loop sem að prufar tölur undir hundrað
    kíkja á allar tölur sem eru minna en og jafnt og talan
    telja hversu marga divisors talan á sér
    ef að hún á sér nákvæmlega tíu skal prenta töluna
    
"""

num = 10
while num < 100:
    first_num = num // 10
    second_num = num % 10
    sum_num = first_num + second_num
    if sum_num ** 2 == num:
        print (num)
    num += 1
num2 = 2
while num2 < 100:
    counter = 0
    for i in range(1,num2+1):
        if num2 % i == 0:
            counter += 1
    if counter == 10:
        print (num2)
    num2 += 1

