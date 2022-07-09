print('Калькулятор растаможки автомобилей')
year = int(input('Введите год выпуска: '))
horse_power = int(input('Введите количество л.с.: '))
engine_volume = int(input('Введите объем двигателя: '))
price_in_usd = int(input('Введите стоимость в долларах: '))
usd_rub = 61.2664
eur_rub = 62.0499
age = 2022 - year
all_clearence = 0

# Сбор за таможенное оформление
customs_duty_prices = {
                    200000: 775,
                    450000: 1550,
                    1200000: 3100,
                    2700000: 8530,
                    4200000: 12000,
                    5500000: 15500,
                    7000000: 20000,
                    8000000: 23000,
                    9000000: 25000,
                    10000000: 27000
}

for i in customs_duty_prices:
    if price_in_usd * usd_rub > 10000000:
        all_clearence += 30000
        break
    else:
        if price_in_usd * usd_rub < i:
            plus = customs_duty_prices[i]
            all_clearence += plus
            break

# Утилизационный сбор
recycling_duty_prices = [20000, 0.17, 0.26]

if age < 3:
    all_clearence += (recycling_duty_prices[0] * recycling_duty_prices[1])
else:
    all_clearence += (recycling_duty_prices[0] * recycling_duty_prices[2])

#Таможенная пошлина
customs_fee_before_tree_years = {
    8500: [0.54, 2.5],
    16700: [0.48, 3.5],
    42300: [0.48, 5.5],
    84500: [0.48, 7.5],
    169000: [0.48, 15],
    169001: [0.48, 20]
}

if age < 3:
    for i in customs_fee_before_tree_years:
        if price_in_usd * usd_rub < i * eur_rub:
            clearece_by_price = price_in_usd * customs_fee_before_tree_years[i][0] * usd_rub
            clearence_by_volume = engine_volume * customs_fee_before_tree_years[i][1] * eur_rub
            if clearece_by_price > clearence_by_volume:
                all_clearence += clearece_by_price
                break
            else:
                all_clearence += clearence_by_volume
                break


print(round(all_clearence, 2))
