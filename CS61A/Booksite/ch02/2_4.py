# 2.4.4   Local State
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call.
    
    The nonlocal statement indicates that the name appears somewhere 
    in the environment other than the first (local) frame or the last (global) frame.
    """

    def withdraw(amount):
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount  # Re-bind the existing balance name
        return balance

    return withdraw


def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)

    return dispatch


# 2.4.8   Dispatch Dictionaries


def account(initial_balance):

    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': initial_balance
    }
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)


def deposit(account, amount):
    return account['deposit'](amount)


def check_balance(account):
    return account['balance']


a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)
