from behave import *
from src.virtual_wallet import VirtualWallet


@given(u'{username} have not create any account')
def step_chck_no_account(context,username):
    if not hasattr(context, 'wallet'):
       context.wallet = VirtualWallet()
    try:
        context.wallet.get_balance_available(username)
        context.exc = None
    except Exception as e:
        context.exc = e
    if context.exc == None:
        raise Exception("The user exist!")


@when(u'{username} request the creation of an account')
def step_create_account(context,username):
    if not hasattr(context, 'wallet'):
        context.wallet = VirtualWallet()
    context.wallet.create_account(username)


@then(u'{username} will have in the account {amount} dollar balance available')
def step_chck_balance_available(context,username,amount):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    print(context.wallet.get_balance_available(username))
    assert context.wallet.get_balance_available(username) == int(amount)


@given(u'{username} has an account with {amount} dollar balance available')
def step_init_account_and_balance(context,username,amount):
    if not hasattr(context, 'wallet'):
        context.wallet = VirtualWallet()    
    context.wallet.create_account(username)
    context.wallet.deposit_money(username,int(amount))


@when(u'{username} add {amount} dollar to the wallet')
def step_deposit_money(context,username,amount):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    context.wallet.deposit_money(username,int(amount))

@when(u'{username} buy a product of {amount} dollar')
def step_buy_product(context,username,amount):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    context.wallet.payment_transaction(username,int(amount))


@when(u'{username} try to delete his account')
def step_try_delete_account(context,username):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    try:
        context.wallet.delete_account(username)
        context.exc = None
    except Exception as e:
        context.exc = e
    pass


@then(u'{username} account has not been deleted')
def step_chck_account(context,username):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    try:
        context.wallet.create_account(username)
        raise Exception("The user did not exist !")
    except:
        pass


@then(u'An exception occurs')
def step_chck_exception(context):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    assert context.exc != None


@when(u'{username} extract all balance available in account')
def step_empty_account(context,username):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    amount = context.wallet.get_balance_available(username)
    context.wallet.withdrawal_money(username,amount)


@then(u'{username} can delete his account')
def step_delete_account(context,username):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    context.wallet.delete_account(username)


@when(u'{username} extract {amount} dollar')
def step_withdrawal(context,username,amount):
    if not hasattr(context, 'wallet'):
        raise Exception("Virtual Wallet uninitialized.")
    context.wallet.withdrawal_money(username,int(amount))



@when(u'{username} try to create another account')
def step_impl(context,username):
    if not hasattr(context, 'wallet'):
        context.wallet = VirtualWallet()
    try:
        context.wallet.create_account(username)
        context.exc = None
    except Exception as e:
        context.exc = e
    pass

