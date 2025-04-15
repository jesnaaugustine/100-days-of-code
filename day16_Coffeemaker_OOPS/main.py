from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
if __name__=='__main__':
    is_on =True
    menu =Menu()
    coffemaker =CoffeeMaker()
    moneymachine =MoneyMachine()
    while is_on:
        choice_li = menu.get_items()
        choice =input(f'What would you like? ({choice_li}): ')
        if choice.lower() =='off':
            is_on=False
        elif choice.lower() =='report':
            coffemaker.report()
            moneymachine.report()
        elif choice.lower() in [item.name for item in menu.menu]:
            drink =[item for item in menu.menu if item.name==choice.lower()][0]
            res_aval = coffemaker.is_resource_sufficient(drink)
            if res_aval:
                is_payment = moneymachine.make_payment(drink.cost)
                if is_payment:
                    coffemaker.make_coffee(drink)
                    
        else:
            print('Give proper input. ')
