# Parameter Tuning

The Aave Pool in V3 has a variety of parameters which can be adjusted:

* Asset Parameters
* Bridge Parameters

This guide details the process of executing a proposal for parameter adjustments:

* [ARC](https://www.notion.so/Asset-Listing-0ef43bf40ac845b7b94b66dfa4c4b3d6)
* [AIP](https://www.notion.so/Asset-Listing-0ef43bf40ac845b7b94b66dfa4c4b3d6)
* [Creating the proposal](https://www.notion.so/Asset-Listing-0ef43bf40ac845b7b94b66dfa4c4b3d6)

## ARC

The ARC (Aave Request for Comment) is the first step in the proposal process. This is where the idea is proposed and the community can discuss. All ARCs should follow these standard [requirements](https://docs.aave.com/governance/arcs). In addition, parameter adjustments should include [asset risk analysis](https://docs.aave.com/risk/asset-risk/introduction) and rationale for changes. Here is a template which you can reference:

* [Sample ARC from Gauntlet](https://governance.aave.com/t/arc-risk-parameter-updates-2022-01-14/6942)

## AIP

The AIP is a document containing the proposal details which is uploaded to IPFS. The hash of this documented is passed as a parameter when the on-chain proposal is submitted. To create an AIP for a new asset listing follow the steps from the AIP [repo](https://aave.github.io/aip/).

Once the AIP has been reviewed and merged to generate an ipfs hash, and the payload has been created, the proposal can now be submitted on-chain.
