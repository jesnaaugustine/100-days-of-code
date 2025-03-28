
import os
cal = '''  
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
def calculator(f,o,s):
    if o.strip()=='+':
        result = f+s
        print(f'{f} {o} {s} = {result}')
        return result
    elif o.strip()=='-':
        result = f-s
        print(f'{f} {o} {s} = {result}')
        return result
    elif o.strip()=='*':
        result = f*s
        print(f'{f} {o} {s} = {result}')
        return result
    elif o.strip()=='/':
        result = f/s
        print(f'{f} {o} {s} = {round(result,4)}')
        return round(result,4)
    else:
        return "invalid operator"
    ˇ


if __name__=='__main__':
    print(cal)
    first_p = 'n'
    while True:
        if first_p =='n':
            first = input("What's the first number:  ")
        print('+\n-\n*\n/\n')
        operator = input('Pick up an operator: ')
        second = input("What's the second number:  ")
        result = calculator(float(first),operator,float(second))
        if isinstance(result,str):
            first_p='y'
            print(result)
        else:
            con = input(f"Type 'y' to continue calculating with {result}, pr type 'n' to start a new calculation: ")
            if con.lower() in ['y','yes']:
                first = result
                first_p='y'
            elif con.lower() in ['n','no']:
                first_p ='n'
                os.system('cls' if os.name == 'nt' else 'clear')
                print(cal)
            else:
                break





