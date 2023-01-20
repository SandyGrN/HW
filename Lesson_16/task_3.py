class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self, years):
        self._balance = self._balance + self._balance * (self.interest/100)*years
        return self._balance


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit


lincoln_account = Account.create_account(101010)
lincoln_account._balance = 2459.3
lincoln_savings_account = SavingsAccount(3456.3, 101010, 6.7)
lincoln_current_account = CurrentAccount(2474.9, 101010, 5000)

# print(lincoln_savings_account.add_interest(2))


class Bank:
    def __init__(self, accounts: list[Account]) -> None:
        self.accounts = accounts

    def update(self):

        def up_curr():
            x = getattr(account, '_balance')
            y = getattr(account, 'overdraft_limit')
            if x < y:
                return (f'Your account №{account._account_number} is overdrafted')
            if x > y:
                return ("You don't have any debt")

        for account in self.accounts:
            if hasattr(account, 'overdraft_limit'):
                return up_curr()
            elif hasattr(account, 'interest'):
                print(f'Actual balance for №{account._account_number} is {account.add_interest(1)}')

    def open_acc(self, account):
        self.accounts.append(account)
        return (f'Account {account._account_number} has been opened')

    def close_acc(self, account):
        self.accounts.remove(account)
        return (f'Account {account._account_number} has been closed')

    def pay_divident(self):
        for account in self.accounts:
            divident = account._balance * 0.05
            account._balance = account._balance + divident
            return (f'For account №{account._account_number}\nDivident - {divident}$. Your balance - {account._balance}$')


bank_1 = Bank([lincoln_account, lincoln_savings_account])
bank_1.open_acc(lincoln_current_account)

print(bank_1.update())
print(bank_1.pay_divident())
