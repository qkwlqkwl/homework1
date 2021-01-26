import money

def select_money():
    if(money.isSend)==True:
        print(f"原有存款{money.savedMoney},工资发了{money.sendMoney}元")
        money.savedMoney+=money.sendMoney
        print(f"存款总额为{money.savedMoney}")
    else:
        print(f"原有存款{money.savedMoney},没有发工资,不开心")
        print(f"存款总额为{money.savedMoney}")

