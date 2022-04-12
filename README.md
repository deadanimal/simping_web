# Simping Web

## Deployed Contracts

1. SimpingToken deployed to: 0xb378605a1A2a30229C91cbb263523E2bD7D28e84
* SimpingGovernor deployed to: 0x03673218758039AbC70285d1D7f555CB228937Ad
* Factory deployed to: 0xfc18d25A90c83b94d05C3C942cc14508f03346Bb
* Market deployed to: 0x63C5EC940d262F6cA16983898dD7949EDA3786d1

## Simping Factory

Main features include create new collection and mint token per collection...


```
[
  "constructor(uint256)",
  "event Created(uint256 indexed,address indexed,address indexed,string,string)",
  "event Minted(address indexed,address indexed,address indexed,string)",
  "event OwnershipTransferred(address indexed,address indexed)",
  "function create(string,string) payable",
  "function fee() view returns (uint256)",
  "function getBalance() view returns (uint256)",
  "function getCollection(uint256) view returns (address, address, string, string)",
  "function getCollectionCreator(uint256) view returns (address)",
  "function mint(uint256,address,string) payable",
  "function newContractOwner(uint256,address)",
  "function owner() view returns (address)",
  "function renounceOwnership()",
  "function setFee(uint256)",
  "function transferOwnership(address)",
  "function withdraw(address,uint256)"
]
```

## Simping Market 

Main features include 1) buy/sell/retract sale... 2) auction, bid, accept bid 3) initialise collection


```
[
  "constructor(address,address,uint256,uint256,uint256)",
  "event AuctionCompleted(uint256 indexed,address indexed,address indexed,uint256)",
  "event AuctionCreated(uint256 indexed,address indexed,uint256)",
  "event BidCreated(uint256 indexed,uint256 indexed,address indexed,uint256)",
  "event ForSale(uint256 indexed,address indexed,uint256)",
  "event NotForSale(uint256 indexed,address indexed)",
  "event OwnershipTransferred(address indexed,address indexed)",
  "event SaleCompleted(uint256 indexed,address indexed,address indexed,uint256)",
  "event SendAmount(address indexed,address indexed,uint256,uint256 indexed)",
  "function acceptBid(uint256)",
  "function auctionToken(uint256,address,uint256,uint256)",
  "function bidToken(uint256) payable",
  "function buy(uint256) payable",
  "function cancelFee() view returns (uint256)",
  "function commissionFee() view returns (uint256)",
  "function factory() view returns (address)",
  "function getAuction(uint256) view returns (uint256, address, uint256, uint256, address, uint256, bool)",
  "function getBalance() view returns (uint256)",
  "function getBid(uint256) view returns (uint256, address, uint256)",
  "function getHighestBid(uint256) view returns (uint256, address)",
  "function getSale(uint256) view returns (address, address, uint256, address, uint256)",
  "function initialise(uint256,uint256)",
  "function minimumPrice() view returns (uint256)",
  "function owner() view returns (address)",
  "function registrar() view returns (address)",
  "function renounceOwnership()",
  "function retract(uint256) payable",
  "function sell(uint256,address,uint256,uint256)",
  "function setFees(uint256,uint256,uint256)",
  "function transferOwnership(address)",
  "function withdraw(address,uint256)"
]
```