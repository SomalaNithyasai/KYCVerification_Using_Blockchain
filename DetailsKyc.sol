// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

contract DetailsKyc {
    struct KYC {
        uint256 id;
        uint256 companyId;
        uint256 userId;
        string fullName;
        string motherName;
        string adhaarName;
        string panNumber;
        string drivingPath;
        string adhaarPath;
        string photoPath;
        string status;
        string appliedOn;
    }
    mapping(address => KYC[]) public kyclist;

    function addPress(
        uint256 _companyId,
        uint256 _userId,
        string memory _fullName,
        string memory _motherName,
        string memory _adhaarName,
        string memory _panNumber,
        string memory _drivingPath,
        string memory _adhaarPath,
        string memory _photoPath,
        string memory _status,
        string memory _appliedOn
    ) public {
        uint256 id = kyclist[msg.sender].length + 1;

        kyclist[msg.sender].push(
            KYC(
                id,
                _companyId,
                _userId,
                _fullName,
                _motherName,
                _adhaarName,
                _panNumber,
                _drivingPath,
                _adhaarPath,
                _photoPath,
                _status,
                _appliedOn
            )
        );
    }

    function getUsers()
        public
        view
        returns (
            uint256[] memory,
            uint256[] memory,
            uint256[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory
        )
    {
        uint256 count = kyclist[msg.sender].length;
        uint256[] memory _id = new uint256[](count);
        uint256[] memory _companyId = new uint256[](count);
        uint256[] memory _userId = new uint256[](count);
        string[] memory _fullName = new string[](count);
        string[] memory _motherName = new string[](count);
        string[] memory _adhaarName = new string[](count);
        string[] memory _panNumber = new string[](count);
        string[] memory _drivingPath = new string[](count);
        string[] memory _adhaarPath = new string[](count);
        string[] memory _photoPath = new string[](count);
        string[] memory _status = new string[](count);
        string[] memory _applied = new string[](count);

        for (uint256 index = 0; index < count; index++) {
            KYC storage user = kyclist[msg.sender][index];
            _id[index] = user.id;
            _companyId[index] = user.companyId;
            _userId[index] = user.userId;
            _fullName[index] = user.fullName;
            _motherName[index] = user.motherName;
            _adhaarName[index] = user.adhaarName;
            _panNumber[index] = user.panNumber;
            _drivingPath[index] = user.drivingPath;
            _adhaarPath[index] = user.adhaarPath;
            _photoPath[index] = user.photoPath;
            _status[index] = user.status;
            _applied[index] = user.appliedOn;
        }

        return (
            _id,
            _companyId,
            _userId,
            _fullName,
            _motherName,
            _adhaarName,
            _panNumber,
            _drivingPath,
            _adhaarPath,
            _photoPath,
            _status,
            _applied
        );
    }

    function updateStatus(string memory pointPoint, uint256 id) public {
        for (uint256 index = 0; index < kyclist[msg.sender].length; index++) {
            KYC storage user = kyclist[msg.sender][index];
            if (id == user.id) {
                user.status=pointPoint;
            }
        }
    }
}
