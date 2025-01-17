// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

contract UserPoint {
    struct User {
        uint256 id;
        string name;
        string mobile;
        string mail;
        string actor;
        string passsword;
        string addressP;
    }
    mapping(address => User[]) public userList;

    function addPress(
        string memory _name,
        string memory _mobile,
        string memory _mail,
        string memory _actor,
        string memory _passsword,
        string memory _adresss
    ) public {
        uint256 id = userList[msg.sender].length + 1;
        userList[msg.sender].push(
            User(id, _name, _mobile, _mail, _actor, _passsword, _adresss)
        );
    }

    function getUsers()
        public
        view
        returns (
            uint256[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory
        )
    {
        uint256 count = userList[msg.sender].length;
        uint256[] memory id = new uint256[](count);
        string[] memory names = new string[](count);
        string[] memory mobs = new string[](count);
        string[] memory mails = new string[](count);
        string[] memory _addressP = new string[](count);
        string[] memory typePro = new string[](count);
        string[] memory _password = new string[](count);

        for (uint256 index = 0; index < count; index++) {
            User storage user = userList[msg.sender][index];
            id[index] = user.id;
            names[index] = user.name;
            mobs[index] = user.mobile;
            mails[index] = user.mail;
            typePro[index] = user.actor;
            _addressP[index] = user.addressP;
            _password[index] = user.passsword;
 
        }
        return (id, names, mobs, mails, typePro, _addressP,_password);
    }
}
