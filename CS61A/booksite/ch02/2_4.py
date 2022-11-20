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


# within the body of a function, all instances of a name must refer to the same frame.

# This error occurs before line 5 is ever executed, implying that Python has considered line 5 in some way before executing line 3.
# 1	def make_withdraw(balance):
# 2	    def withdraw(amount):
# 3	        if amount > balance: # Error becase 5 line
# 4	            return 'Insufficient funds'
# 5	        balance = balance - amount
# 6	        return balance
# 7	    return withdraw

# 2.4.7   Implementing Lists and Dictionaries
# def mutable_link():
#     """Return a functional implementation of a mutable linked list."""
#     contents = empty

#     def dispatch(message, value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_link(contents)
#         elif message == 'getitem':
#             return getitem_link(contents, value)
#         elif message == 'push_first':
#             contents = link(value, contents)
#         elif message == 'pop_first':
#             f = first(contents)
#             contents = rest(contents)
#             return f
#         elif message == 'str':
#             return join_link(contents, ", ")

#     return dispatch

# def to_mutable_link(source):
#     """Return a functional list with the same contents as source."""
#     s = mutable_link()
#     for element in reversed(source):
#         s('push_first', element)
#     return s


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



