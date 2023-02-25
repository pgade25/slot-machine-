
import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[lines]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
        return winnings,winning_lines   
        
    
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)
        
    columns = []   
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[: ]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")    
        print()
def deposit():
    while True:
        amount = input("enter the deposit amount $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter the number")
            
    return amount
def slot_lines():
    while True:
        lines = input("enter the number of lines you want to bet on (1-"+str(MAX_LINES)+") ?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= MAX_LINES<=3:
                break
            else:
                print("please enter valid number of lines")
        else:
            print("please enter the number")
            
    return lines

def bet_amount():
    while True:
        amount = input("what would you like to bet? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"amount must be between $ {MIN_BET} - {MAX_BET}.")
        else:
            print("please enter the number")
            
    return amount
    
def spin(balance):
    lines = slot_lines()
    while True:
        bet = bet_amount()
        total  = bet* lines
        if total > balance:
            print(f"you do not have enough balance. your total balance is {balance}")
    
        else:
            break
    
    print(f"You are betting ${bet} on {lines} no of lines. and your total is{total}")
    print(balance,lines)

    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"yu won on lines:", *winning_lines)
    return winnings - total
    
def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input(" press enter to spin (q to quit).  ")
        if spin == "q":
            break
        balance += spin(balance)
        
    print(f"you left with ${balance}")
main()                 

