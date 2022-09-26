from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[2]
    print(fund_me)
    account = get_account()
    price = fund_me.getPrice()
    print(price)
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[2]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
