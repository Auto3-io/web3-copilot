# Creating an asset listing proposal

The following guide will walk you through the process of adding a new token as a whitelisted currency to be deposited/borrowed in the Aave protocol.

## 1. Complete the the off-chain process

Details of the off-chain process, including completing the ARC and starting the AIP, can be found in the [Governance Docs](https://docs.aave.com/governance/guides/new-asset-listing).&#x20;

## 2. Prepare for the on-chain process

### 1. Create a Pull Request with your token parameters

* fork from the [protocol-v2 repository@aave-v2-asset-listing](https://github.com/aave/protocol-v2/tree/aave-v2-asset-listing)
* add your token addresses to `markets/aave/index.ts`&#x20;
* create your reserve parameters inside `markets/aave/reservesConfigs.ts`&#x20;
* update the types to include your token in `/helpers/types`&#x20;
* add the current price in the `MOCK_CHAINLINK_AGGREGATORS_PRICES` object in `markets/aave/commons.ts`&#x20;
* create a PR with your changes

An example PR can be found [here](https://github.com/aave/protocol-v2/pull/11/commits/ba5d325ccb0316253720ac9afd972d436491c55c)

### 2. Run the asset deployment script

From the [protocol-v2 repository](https://github.com/aave/protocol-v2),&#x20;

&#x20;`$ npm install`

`$ SYMBOL="Your Symbol" npm run external:deploy-assets-kovan` to deploy on kovan

`$ SYMBOL="Your Symbol" npm run external:deploy-assets-main` to deploy on mainnet

This will deploy the following contracts and display the addresses:

* AToken
* variableDebt&#x20;
* stableDebt&#x20;
* InterestRateStrategy

You will need them for the last step.

## 3. Make a proposal to the Aave Governance to initialize your assets

* Get your AIP IPFS hash [here](https://github.com/aave/aip/blob/master/content/ipfs-aips/all-aips.json)

Deploy the on-chain proposal following the instruction from the [asset listing repository](https://github.com/aave/aave-asset-listing)

## 4. Follow up

You will need to connect with Aave Genesis team, to add your token price oracle as a source.

