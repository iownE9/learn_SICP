# Object-Oriented Programming

# 2.5.1 Objects and Classes


# 2.5.2 Defining Classes
class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


def instances():
    """
    >>> a = Account('Kirk')
    >>> # 
    >>> a.holder
    'Kirk'
    >>> a.balance
    0
    >>> a.deposit(15)
    15 
    >>> a.withdraw(10)  # The withdraw method returns the balance after withdrawal
    5
    >>> a.balance       # The balance attribute has changed
    5
    >>> a.withdraw(10)
    'Insufficient funds'
    >>> 
    >>> # Identity
    >>> b = Account('Spock')
    >>> b.balance = 200
    >>> [acc.balance for acc in (a, b)]
    [0, 200]
    >>>
    >>> a is a
    True
    >>> a is not b
    True
    >>>
    >>> spock_account = Account('Spock')
    >>> spock_account.deposit(100)
    100
    >>> spock_account.withdraw(90)
    10
    >>> spock_account.withdraw(90)
    'Insufficient funds'
    >>> spock_account.holder
    'Spock'
    >>>
    >>> getattr(spock_account, 'balance')
    10
    >>> hasattr(spock_account, 'deposit')
    True
    >>>    
    >>> type(Account.deposit)
    <class 'function'>
    >>> type(spock_account.deposit)
    <class 'method'>
    >>> Account.deposit(spock_account, 1001)  # The deposit function takes 2 arguments
    1011
    >>> spock_account.deposit(1000)           # The deposit method takes 1 argument
    2011    
    """


# class attribute
def classAttributes():
    """
    >>> spock_account = Account('Spock')
    >>> kirk_account = Account('Kirk')
    >>> spock_account.interest
    0.02
    >>> kirk_account.interest
    0.02
    >>> Account.interest = 0.04
    >>> spock_account.interest
    0.04
    >>> kirk_account.interest
    0.04
    >>> kirk_account.interest = 0.08
    >>> kirk_account.interest
    0.08
    >>> spock_account.interest
    0.04
    >>> Account.interest = 0.05  # changing the class attribute
    >>> spock_account.interest     # changes instances without like-named instance attributes
    0.05
    >>> kirk_account.interest     # but the existing instance attribute is unaffected
    0.08
    """


# Inheritance
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

    # called self.withdraw_charge rather than the equivalent CheckingAccount.withdraw_charge.


def use_inheritance():
    """
    >>> checking = CheckingAccount('Sam')
    >>> checking.deposit(10)
    10
    >>> checking.withdraw(5)
    4
    >>> checking.interest
    0.01
    """


# Multiple Inheritance
class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!


def use_multiple_inheritance():
    """
    >>> such_a_deal = AsSeenOnTVAccount("John")
    >>> such_a_deal.balance
    1
    >>> such_a_deal.deposit(20)            # $2 fee from SavingsAccount.deposit
    19
    >>> such_a_deal.withdraw(5)            # $1 fee from CheckingAccount.withdraw
    13
    >>> such_a_deal.deposit_charge
    2
    >>> such_a_deal.withdraw_charge
    1
    >>> # order
    >>> [c.__name__ for c in AsSeenOnTVAccount.mro()]
    ['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
    """