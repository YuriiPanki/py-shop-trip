import datetime

from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_check(
            self,
            shop: Shop,
            printing: bool = False
    ) -> float:
        milk = self.product_cart["milk"] * shop.products["milk"]
        bread = self.product_cart["bread"] * shop.products["bread"]
        butter = self.product_cart["butter"] * shop.products["butter"]
        result = milk + bread + butter
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought:\n"
            f"{self.product_cart['milk']} milks for {milk} dollars\n"
            f"{self.product_cart['bread']} breads for {int(bread)} dollars\n"
            f"{self.product_cart['butter']} butters for {butter} dollars\n"
            f"Total cost is {result} dollars\n"
            f"See you again!\n"
        ) if printing else result
        return result

    def trip(self, shop: Shop, fuel_price: float) -> float:
        return round(
            sqrt(
                pow(self.location[0] - shop.location[0], 2)
                + pow(self.location[1] - shop.location[1], 2)
            ) * self.car.fuel_consumption / 100 * 2 * fuel_price,
            2
        ) + self.count_check(shop, False)

    def acting(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        cost_ = []
        for shop in shops:
            cost_.append(self.trip(shop, fuel_price))
            print(f"{self.name}'s trip to the {shop.name} costs {cost_[-1]}")

        min_value = min(cost_)
        shop_min_cost = shops[cost_.index(min(cost_))]
        if min_value < self.money:
            print(f"{self.name} rides to {shop_min_cost.name}", end="\n\n")
            self.count_check(shop_min_cost, True)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money - min_value} dollars")
            print()
        else:
            print(f"{self.name} doesn't have enough", end=" ")
            print("money to make a purchase in any shop")
