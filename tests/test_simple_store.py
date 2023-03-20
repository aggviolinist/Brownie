from brownie import storeHere, accounts


def test_deploy():
    # Arrange
    account = accounts[3]
    # Act
    simple_container = storeHere.deploy({"from": account})
    starting_value = simple_container.getBackGang()
    expected = 21
    # Assert
    assert starting_value == expected


def test_updating_store():
    # Arrange
    account = accounts[4]
    simple_kasuku = storeHere.deploy({"from": account})
    # Act
    expected = 76
    simple_kasuku.addItemTwo(expected, {"from": account})
    # Assert
    assert 76 == simple_kasuku.getBackGang()


# def get_wallet():
#     if network.show_active() == "development":
#         return accounts[1]
#     else:
#         return accounts.add(config["wallets"]["from_key_two"])
