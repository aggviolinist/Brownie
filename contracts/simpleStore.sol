//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract storeHere {
    uint256 storeNum = 21;

    struct Kangemi {
        string name;
        int256 regNumber;
    }

    mapping(string => int256) public wareHousing;
    Kangemi[] public wareHouse;

    function getStoreNumber(uint256 myStoreNumber) public {
        storeNum = myStoreNumber;
    }

    function getBackGang() public view returns (uint256) {
        return storeNum;
    }

    function addItem(string memory goods, int256 services) public {
        wareHouse.push(Kangemi(goods, services));
        wareHousing[goods] = services;
    }

    function addItemTwo(uint256 goodsTwo) public returns (uint256) {
        storeNum = goodsTwo;
        return goodsTwo;
    }
}
