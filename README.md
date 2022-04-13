# Simping Web

We will be using https://nft.storage/docs/client/js/ i.e. NFT Storage to store data on IPFS and get the hash from NFT Storage.

## List of Views

1. Homepage
   1. R: Features of Simping such as creating collections, minting, fractionalising NFTs to ERC20, interface with CP's swap and perps
   2. R: Created collections
   3. R: minted tokens
   4. R: start auction
   5. R: completed auction
   6. R: start for sale
   7. R: completed for sale

2. Explore
   1. R: recently created collections
   2. R: recently minted
   3. R: The above but filter with table
   
3. Dashboard
   1. R: Collection created by user
   2. R: Tokens minted by user per collection
   3. R: Tokens sold by user
   4. R: Tokens bought by user
   5. R: User's wallet balance
   6. W: Login via social media, to get User ID and Post ID
   7. W: Create collection
   8. W: Mint token, allow users to select unminted tokens only
   9. W: Initiliase collection i.e. setting royalty
   10. W: Fractionalise the minted NFT to the DAO

4. Profile
   1. R: User's collections minted
   2. R: User's tokens bought
   3. R: User's tokens sold
   
5. NFT Detail
   1. W: Buy Token
   2. W: Bid Token
   3. W: Sell Token
   4. W: Auction Token
   5. W: Accept Token
   6. W: Retract Token Sale


6. Factory
   1. W: Create custom collection
   2. W: Mint custom item, together with metadata & custom attributes and upload media
      1. [INFO] Please do note that minting will upload media first then get the CID, then we customise the metadata and upload the metadata and store the CID of the metadata on the blockchain.
   3. W: Fractionalise the minted NFT to the DAO

## Deployed Contracts

1. SimpingToken deployed to: 0xb378605a1A2a30229C91cbb263523E2bD7D28e84
* SimpingGovernor deployed to: 0x03673218758039AbC70285d1D7f555CB228937Ad
* Factory deployed to: 0xfc18d25A90c83b94d05C3C942cc14508f03346Bb
* Market deployed to: 0x63C5EC940d262F6cA16983898dD7949EDA3786d1

## Simping Factory

Main features include create new collection and mint token per collection...


```json
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


```json
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

## NFT Metadata Standard

Example JSON of the metadata:
```json
{    
    "media": "media_ipfs_hash", 
    "name": "name",
    "description": "description",
    "attributes": [
        "display_type": "boost_number", // optional
        "trait_type": "Base", 
        "value": "Starfish"
    ], 
}
```

For simping, maybe we add platform, date-posted, date-minted