print('Калькулятор растаможки автомобилей')
year = int(input('Введите год выпуска: '))
horse_power = int(input('Введите количество л.с.: '))
# engine_volume = int(input('Введите объем двигателя: '))
price_in_usd = int(input('Введите стоимость в долларах: '))
usd_rub = 55
age = 2022 - year
all_clearence = 0

# Сбор за таможенное оформление
customs_duty_prices = {200000: 775,
                        450000: 1550,
                        1200000: 3100,
                        2700000: 8530,
                        4200000: 12000,
                        5500000: 15500,
                        7000000: 20000,
                        8000000: 23000,
                        9000000: 25000,
                        10000000: 27000}

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

#Акциз
excise_tax = {150: 53,
                200: 511,
                300: 836,
                400: 1425,
                500: 1475}

for i in excise_tax:
    if horse_power > 500:
        all_clearence += (horse_power * 1523)
        break
    else:
        if horse_power < 90:
            break
        else:
            if horse_power < i:
                plus = excise_tax[i]
                all_clearence += plus


print(all_clearence)
