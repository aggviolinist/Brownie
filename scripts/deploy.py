from brownie import accounts, config, storeHere, network
import os


def deployment():
    print("*******encryption of private keys********")
    account = accounts.load("hellcats")
    print(account)
    print("*******using environment variables*******")

    account = accounts.add(os.getenv("SEPOLIA_PRIVATE_KEY"))
    print(account)

    print("********using config yaml***************")
    account = accounts.add(config["wallets"]["from_key"])
    print(account)

    print("************Creating a contract on the block chain************")
    print("******************************")
    print("******************************")

    account = accounts[2]
    simple_store = storeHere.deploy({"from": account})
    print(simple_store)

    print("**********Calling a value that doesnt return a value***********")
    print("******More of calling a function like we always do*************")
    print("***************************************************************")

    stored_value = simple_store.getBackGang()
    print(stored_value)

    print("**********Updating the transaction on the block chain*********")
    print("******************************")
    print("******************************")
    print("**************************************************************")
    updated_value = simple_store.addItemTwo(100, {"from": account})
    updated_value.wait(1)
    # print(updated_value)

    print("***********New updated value called********************")
    print("*******************************")

    Update = simple_store.getBackGang()
    print(Update)


def get_wallet():
    if network.show_active() == "development":
        return accounts[1]
    else:
        return accounts.add(config["wallets"]["GOERLI_PRIVATE_KEY"])


def main():
    print("Hello Im enjoying this brownie ting")
    deployment()
