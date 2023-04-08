# Subgraph data (GraphQL)

## The Graph and GraphQL

The Graph is a decentralized protocol for indexing and querying data from blockchains, starting with Ethereum. What that means: it is an easier way to retrieve specific data from the blockchain, within the ethos of web3, with the advantages of decentralization and reliability.

GraphQL is the underlying query language utilised in The Graph. What is the difference between standard RESTFUL API calls and GraphQL calls? The difference is that traditional APIs require the developers to create specific endpoints for users that return specific data. If the user requires more information, they may need to make multiple API calls, sometimes hundreds of API calls, to get the information they require. With The Graph (which uses GraphQL), only one call is needed to a _subgraph_, as long as the developer has created a flexible schema.

For more information on The Graph and the underlying GraphQL, see [this GraphQL primer](https://medium.com/graphprotocol/graphql-will-power-the-decentralized-web-d7443a69c69a).&#x20;

If you are consuming GraphQL data in your app, we'd recommend using a fully featured package such as [Apollo](https://www.apollographql.com) or a minimal implementation such as [GraphQL-Request](https://github.com/prisma-labs/graphql-request).

## Aave's Subgraphs

To view the source of our subgraphs, see our [Github repo](https://github.com/aave/protocol-v2-subgraph).

{% hint style="info" %}
For V1 subgraphs, refer to the [V1 documentation](https://docs.aave.com/developers/v/1.0/integrating-aave/using-graphql).
{% endhint %}

{% tabs %}
{% tab title="V2" %}
| Return Data Types                                | Subgraph Address                                                                                                                                   |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mainnet                                          | [https://thegraph.com/explorer/subgraph/aave/protocol-v2?version=current](https://thegraph.com/explorer/subgraph/aave/protocol-v2?version=current) |
| [Governance](../protocol-governance/governance/) | [https://thegraph.com/explorer/subgraph/aave/governance-v2](https://thegraph.com/explorer/subgraph/aave/governance-v2)                             |
| Kovan                                            | [https://thegraph.com/explorer/subgraph/aave/protocol-v2-kovan](https://thegraph.com/explorer/subgraph/aave/protocol-v2-kovan)                     |
| Kovan Governance                                 | [https://thegraph.com/explorer/subgraph/aave/governance-v2-kovan](https://thegraph.com/explorer/subgraph/aave/governance-v2-kovan)                 |
{% endtab %}

{% tab title="Polygon" %}
| Return Data Types | Subgraph Address                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Mainnet           | [https://thegraph.com/explorer/subgraph/aave/aave-v2-matic](https://thegraph.com/explorer/subgraph/aave/aave-v2-matic)                   |
| Mumbai            | [https://thegraph.com/explorer/subgraph/aave/aave-v2-polygon-mumbai](https://thegraph.com/explorer/subgraph/aave/aave-v2-polygon-mumbai) |
{% endtab %}

{% tab title="Avalanche" %}
| Subgraph | Url                                                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mainnet  | [https://thegraph.com/legacy-explorer/subgraph/aave/protocol-v2-avalanche](https://thegraph.com/legacy-explorer/subgraph/aave/protocol-v2-avalanche) |
| Fuji     | [https://thegraph.com/legacy-explorer/subgraph/aave/protocol-v2-fuji](https://thegraph.com/legacy-explorer/subgraph/aave/protocol-v2-fuji)           |
{% endtab %}
{% endtabs %}

### How to use the playground

If you visit the above **playground** links in your browser, you will be taken to The Graph’s playground, where you can easily construct and test GraphQL queries.&#x20;

* To execute your query, select the purple play button.&#x20;
* The query results will be returned in the middle column.&#x20;
* To find out what data is available, use the ‘Schema’ column on the right, which can be explored to discover the underlying data.&#x20;
* You can also type in the left column and use the auto-complete to find the correct query/types.

### Common 'Gotchas'

* All address values (e.g. when used for `id`) must be in **lower case** format.
* The ID of reserves is the address of the asset and the address of the market's LendingPoolAddressProvider, in lower case.
* When using the **raw** endpoints, depending on the type of numeric value queried, it will be returned either in `wei` units (i.e. 10^18), the decimals of the asset itself (i.e. 10^6 for USDC), or `ray` units (i.e. 10^27).
* Each results 'page' returns 100 entries by default. This can be increased to a maximum of 1000 entries per page.
  * E.g. to list the next 1000 entries, append something similar to: `(skip:1000, first: 1000)` to your query's parameters.
  * This also applies to nested entries, such as arrays.
* All data on our Graph endpoint is static. Therefore to get the latest balance of a user (which includes the interest earned up to that second), you would need to either calculate it yourself or make a `balanceOf()` call to the [aToken contract](../deployed-contracts/deployed-contracts.md#supported-assets).

## Accessing GraphQL data from your app

The **recommended** way is to use a client library that can take care of the 'plumbing' to ensure you have up to date data (with caching sometimes included). Internally we use Apollo, but there are many options depending on your programming language, see the official GraphQL page.

If for some reason you cannot use a client library (e.g. querying via Postman), then you can create a POST request to our subgraph's HTTP endpoint, with header: `Content-Type: application/json` and the body consisting of your query on one line in quotations. For example:

```graphql
{"query": "{ reserves (where: {usageAsCollateralEnabled: true})  { id name price {id} liquidityRate variableBorrowRate stableBorrowRate}}" }
```

## Example Queries

{% hint style="info" %}
In the below queries, we'll be using the mainnet `Big uints` GraphQL endpoints. You can copy and paste these queries into [the Graph playground links](using-graphql.md#aaves-subgraphs).
{% endhint %}

### Reserve data

If we want to get a list of all the reserves that are able to be used as collateral, along with each reserve's interest rate details , our query would look like:

```javascript
{
  reserves (where: {
    usageAsCollateralEnabled: true
  }) {
    id
    name
    price {
      id
    }
    liquidityRate
    variableBorrowRate
    stableBorrowRate
  }
}
```

If we want to fetch data for a specific reserve, then we would use the reserves ERC20 token address. E.g. for the Chainlink reserve:

```javascript
{
  reserve(id: "0x514910771af9ca656af840dff83e8264ecf986ca0x24a42fd28c976a61df5d00d0599c34c4f90748c8") { // LINK
    symbol
    price
    aToken {
      id
    }
  }
}
```

If we want to fetch historic interest rate data for a particular reserve and paginate through the records, our query could look something like:

```javascript
{
  reserve (id: "0x0000000000085d4780b73119b644ae5ecd22b3760x24a42fd28c976a61df5d00d0599c34c4f90748c8") { // TUSD
    id
    paramsHistory(skip:1000, first: 1000) {
      id
      variableBorrowRate
      utilizationRate
      liquidityRate
      timestamp
    }
  }
}
```

### User data

When an address interacts with the Aave Protocol, a `UserReserve` is created with the user ID being the user's address + the reserve's ID (which is the ERC20 token address).

To fetch the details of a particular `UserReserve`:

```graphql
{
  userReserve(id: "USER_ADDRESS_AND_RESERVE_ADDRESS") {
    reserve {
      id
      symbol
    }
    user {
      id
    }
  }
}
```

To fetch all the reserves (i.e. positions) that a specific user has (note that `user` address **must** be lower case):

```graphql
{
  userReserves(where: { user: "USER_ADDRESS"}) {
    id
    reserve{
      id
      symbol
    }
    user {
      id
    }
  }
}
```

### Deposit data

To get recent deposits for a particular asset:

```graphql
{
  deposits (orderBy: timestamp, orderDirection: desc, where: { 
    reserve: "0xdac17f958d2ee523a2206206994597c13d831ec70x24a42fd28c976a61df5d00d0599c34c4f90748c8" // USDT
  }) {
    id
    amount
    timestamp
  }
}
```

### Borrow data

To get recent borrows for a particular asset:

```graphql
{
  borrows (orderBy: timestamp, orderDirection: desc, where: { 
    reserve: "0xdac17f958d2ee523a2206206994597c13d831ec70x24a42fd28c976a61df5d00d0599c34c4f90748c8" // USDT
  }) {
    id
    amount
    timestamp
  }
}
```

### Flash loan data

An example query for analysing the 5 most recent Flash Loans would be:

```graphql
{ 
  flashLoans( 
    first: 5 
    orderBy: timestamp 
    orderDirection: desc 
  ) { 
    id 
    reserve { 
      id 
      name 
      symbol 
    } 
    amount 
    totalFee 
    timestamp 
  } 
} 
```
