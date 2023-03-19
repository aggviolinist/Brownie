from brownie import accounts, config, storeHere
import os


def deployment():
    print("*******encryption of private keys********")
    account = accounts.load("hellcats")
    print(account)
    print("*******using environment variables*******")

    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)

    print("********using config yaml***************")
    account = accounts.add(config["wallets"]["from_key"])
    print(account)

    print("******************************")
    print("******************************")
    print("******************************")

    account = accounts[2]
    simple_store = storeHere.deploy({"from": account})
    print(simple_store)

    print("******************************")
    print("******************************")
    print("******************************")

    stored_value = simple_store.getBackGang()
    print(stored_value)


def main():
    print("Hello Im enjoying this brownie ting")
    deployment()
