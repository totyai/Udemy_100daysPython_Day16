from resources.menu import Menu
from resources.coffee_maker import CoffeeMaker
from resources.money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    cont = True
    while cont:
        order = input(f"What would you like? ({menu.get_items()}) ").lower()
        if order == "off":
            cont = False
            print("The coffee machine shuts down.")
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(order)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()