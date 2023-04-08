# SDKs

Currently there is a [Typescript package available on NPM](https://www.npmjs.com/package/@aave/protocol-js) to help with your implementation of the Aave Protocol. The SDK provides easy to use methods to interact with the Aave Protocol, as well as methods to calculate user positions such as the health factor.

{% hint style="info" %}
The SDK requires a basic understanding of Javascript/Typescript, as well as experience using NPM.
{% endhint %}

You can easily install the SDK using the command:

```bash
// with npm
npm install @aave/protocol-js

// or with yarn
yarn add @aave/protocol-js
```

## Protocol-js

An example of using the SDK with data fetched from the [subgraph](using-graphql.md):

```javascript
import { v1, v2 } from '@aave/protocol-js';

// returns user summary data in big units.
v1.formatUserSummaryData(
  poolReservesData,
  rawUserReserves,
  userId,
  usdPriceEth,
  currentTimestamp
);

// returns user summary data in small units with 0 decimal places, except health-factor.
v1.computeRawUserSummaryData(
  poolReservesData,
  rawUserReserves,
  userId,
  usdPriceEth,
  currentTimestamp
);

// returns reserves data formatted to big units.
v2.formatReserves(reserves, currentTimestamp);
```

For a list of transaction methods, see the [Github repo](https://github.com/aave/aave-js#transaction-methods).

## Rates calculation <a href="#rates-calculation" id="rates-calculation"></a>

Calculating rates in Aave is somewhat complicated due to the interest bearing nature of aTokens.

The reason for that is twofold:

1. liquidity of aTokens constantly changes which is making utilization based rates extremely dynamic (it's changing every second)
2. depositor interest is not only based on interest, but also includes factors like flash premiums (so it's usually "a little more")

Therefore the Aave protocol keeps track of two values:

**Rate**: The rate is a purely utilization based metric which represents the current rate at a specific point in time.

**Index**: The index keeps track of reserve growth also incorporating things like the flash premium.

To calculate correct historically archived deposit rates you should use [index based rate calculation](https://github.com/aave/aave-js/blob/v2/src/helpers/pool-math.ts#L124).

```javascript
/*
You can fetch the data rquired from graphql.
This query would provide the mot up to date & the first ever data.
This data could be used to calculate the average liquidityRate since inception.
{
  reserves(first: 1) {
    lastUpdateTimestamp
    liquidityIndex
    variableBorrowIndex
    paramsHistory(first: 1, orderDirection: asc, orderBy: timestamp){
      timestamp
    	liquidityIndex
    	variableBorrowIndex
    }
  }
}
*/

// data returned by gql
const result = {
  lastUpdateTimestamp: 1611926412,
  liquidityIndex: "1031830159181667334741382194",
  variableBorrowIndex: "1048002659480593195934069307",
  paramsHistory: [
    {
      timestamp: 1606903009,
      liquidityIndex: "1021187617641523092754480830",
      variableBorrowIndex: "1034162815675781948442542345",
    },
  ],
};
const archivedRate = calculateAverageRate(
  result.paramsHistory[0].liquidityIndex,
  result.liquidityIndex,
  result.paramsHistory[0].timestamp,
  result.lastUpdateTimestamp
);
```
