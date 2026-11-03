"""
Создать «банковский счёт» в классе.** Класс `BankAccount` с полями `owner`, `balance` (`__init__`), методами
`deposit(amount)`, `withdraw(amount)` и `show()`. Метод `withdraw` не должен позволять уйти в минус: если сумма больше
остатка — выводить сообщение и ничего не менять. Создать 2 счёта, проверить операции на каждом.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Внесение суммы в размере amount на счет
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Списывание средств со счета в размере amount если можно
        """
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств!")

    def show(self):
        print(f"Баланс: {self.balance}\nВладелец счета: {self.owner}\n")

Alieshas_account = BankAccount("Алёша", 0)
Edwards_account = BankAccount("Эдвард", 1000000)

Edwards_account.show()
Alieshas_account.show()

Alieshas_account.deposit(23185)
Alieshas_account.withdraw(15.99)
Alieshas_account.withdraw(3054)
Alieshas_account.withdraw(6000)
Alieshas_account.withdraw(1856.50)
Alieshas_account.withdraw(1856.50)
Edwards_account.withdraw(300000)
Edwards_account.withdraw(7000)
Edwards_account.deposit(45000)
Alieshas_account.withdraw(11149.99)
Alieshas_account.withdraw(149.99)

Edwards_account.show()
Alieshas_account.show()
