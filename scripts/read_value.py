from brownie import accounts, config, storeHere, network


def read_from_contract():
    simple_container = storeHere[1]
    # -1 gives us the most recent contract while 0 gives us the first addy
    # ABI
    # Address
    print(simple_container.getBackGang())


def main():
    read_from_contract()
