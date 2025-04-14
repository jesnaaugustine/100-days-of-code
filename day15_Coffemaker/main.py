MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit" :0
}
resource ={'water':300,'milk':200,'coffee':100,'profit':0}
def is_resource_available(drink):
    for ing in drink['ingredients'].keys():
        if drink['ingredients'][ing]>resource[ing]:
            print(f'Sorry there is not enough {ing}.')
            return False
    return True

def process_coins():
    total = 0
    total +=int(input('How many quarters: '))*0.25
    total +=int(input('How many dimes: '))*0.10
    total +=int(input('How many nickles: '))*0.05
    total +=int(input('How many pennies: '))*0.01
    return total
def is_transaction_success(coin,cost):
    global resource
    if coin<cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resource['profit']+=cost
        if coin>cost:
            print(f'Here is ${round(coin-cost,2)} dollers in change.')
        return True
        
def make_coffee(drink):
    global resource
    for ing in drink['ingredients'].keys():
        resource[ing] -= drink['ingredients'][ing]


                


if __name__=='__main__':
    is_on =True
    while is_on:
        choice =input('What would you like? (espresso/latte/cappuccino): ')
        if choice.lower() =='off':
            is_on=False
        elif choice.lower() =='report':
            print(f'Water: {resource["water"]}ml')
            print(f'Milk: {resource["milk"]}ml')
            print(f'Coffee: {resource["coffee"]}g')
            print(f'Money: ${resource["profit"]}')
        elif choice.lower() in MENU.keys():
            drink =MENU[choice.lower()]
            res_aval = is_resource_available(drink)
            if res_aval:
                total_coins = process_coins()
                if is_transaction_success(total_coins,drink['cost']):
                    make_coffee(drink)
                    print(f'Here is your {choice.lower()}☕. Enjoy!!')
        else:
            print('Give proper input. ')
                


