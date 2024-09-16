import frame_statistics


def count_money(how_much):
    Finance.money += how_much


def subtraction_money(price):
    Finance.money -= price  # frame_shop_balls.Shop_balls.all_shops.price_yellow  # сколько денег стоит шар (каждый по разному)!!!!!!!!!!!!!!!
    frame_statistics.Screen_statistics.all_statistics.money_value['text'] = f'{Finance.money}'


class Finance:
    money = 2500000000
