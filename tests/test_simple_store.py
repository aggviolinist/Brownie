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
    # Act
    simple_kasuku = storeHere.
