pragma solidity ^0.4.24;

import "./Ownable.sol";

contract Message is Ownable {
    string private message;

    function setMessage(string newMessage) public payable {
        require(msg.value == 3 ether);
        message = newMessage;
    }

    function getMessage() public view returns (string) {
        return message;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function getBalanceInEther() public view returns (uint) {
        return getBalance() / 1e18;
    }

    function transfer(uint amount) public isOwner {
        require(address(this).balance >= amount);
        owner.transfer(amount);
    }

    function transferTo(uint amount, address to) public isOwner {
        require(address(this).balance >= amount);
        require(to != address(0));
        to.transfer(amount);
    }
}