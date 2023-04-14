# Rewards

In Aave V3, the rewards system has been updated. Now aToken, variableDebtToken and stableDebtToken has an attached array which can accumulate any number of rewards. Each Aave market contains a [RewardsController](../../periphery-contracts/rewardscontroller.md) contract which registers the reward emissions for each aToken and debtToken. 

This guide details the steps for registering a new reward on the `RewardsController`.

- [ARC]
- [AIP]
- [Creating Proposal]
- [Add to Aave Ui]

## ARC

The ARC (Aave Request for Comment) is the first step in the proposal process. This is where the idea is proposed, and the community can discuss the proposal. All ARCs should follow these standard [requirements](https://docs.aave.com/governance/arcs). In addition, new incentive proposals should specify:

- Assets receiving rewards
- Duration of rewards program
- Total emission amount

## AIP

The AIP is a document containing the proposal details which is uploaded to IPFS. The hash of this documented is passed as a parameter when the on-chain proposal is submitted. To create an AIP for a reward emission, follow the steps from the AIP [repo](https://aave.github.io/aip/).

Sample AIPs:

- https://github.com/aave/aip/pull/93

Once the AIP has been reviewed and merged to generate an ipfs hash, and the payload has been created, the proposal can now be submitted on-chain.

## Create Proposal
`EMISSION_ADMIN` set by owner of the EmissionManager contract can configure rewards by calling `configureAssets`.

## Add To Aave Ui

In order for your reward token name and symbol to appear on the Aave frontend, you will need to add your asset to the [Aave Interface repo](https://github.com/aave/interface/blob/main/CONTRIBUTING.md#token-addition).