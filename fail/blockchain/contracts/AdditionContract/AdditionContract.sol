pragma solidity ^0.8.17;

contract AdditionContract {
  uint public state = 0;

  function add(uint value1, uint value2) public {
    state = value1 + value2;
  }

  function getState() public constant returns (uint) {
      return state;
  }
}