# Asset Listing

With Aave V3, the addition of new risk parameters (supply caps, borrow caps, isolation mode) and roles (`RISK_ADMIN` and `ASSET_LISTING_ADMIN`) will reduce the friction of onboarding new assets to Aave markets.

This guide details the process of adding a new asset from idea to implementation:

* ARC
* AIP
* On-chain listing
* Add to Aave UI

## ARC

The ARC (Aave Request for Comment) is&#x20;

the first step in the proposal process. This is where the idea is proposed and the community can discuss. All ARCs should follow these standard [requirements](https://docs.aave.com/governance/arcs). In addition, new asset listings should include:

* [Asset risk analysis](https://docs.aave.com/risk/asset-risk/introduction)
*   Parameters

    *   **Interest rate strategies**
        In Aave, the supply and borrow rates are a function of the utilization rate (amountBorrowed / amountSupplied). The following diagram demonstrates how the rate strategy parameters define the borrow rate curve:\
        <img src="../../.gitbook/assets/image (6).png" alt="" data-size="original">
    *   **LTV**
        LTV defines the maximum percentage which users can borrow against an assets value. For example, if an asset has an LTV of 80% and an oracle price of $100, then users can borrow up to $80 when supplying this asset as collateral. An LTV of 0% means the asset cannot be used as collateral.
    * **Liquidation Threshold**
      Liquidation Threshold defined the maximum collateralization ratio for an asset. If a user exceeds the liquidation threshold, then they are available to be liquidated. Liquidation means anyone can pay back a users debt and claim the corresponding amount of collateral plus a liquidation bonus.
    * **Liquidation Bonus**
      If a users borrow position exceeds the liquidation threshold for their collateral asset, anyone can perform a liquidation by paying off the users debt and claiming the corresponding amount of collateral plus a bonus, called the liquidation bonus which is expressed as a percentage of the repaid amount. The liquidation bonus can be a different percentage for each collateral asset in the protocol.
    * **Supply Cap**
      Supply caps are a new feature in Aave V3, and define the maximum amount of an asset which can be supplied to the protocol. Supply caps can be used to limit the protocol exposure to riskier asset, and prevent against infinite minting exploits. A supply cap is an optional parameter, and the value will depend on the circulating and maximum supply of the asset.
    * **Borrow Cap**
      Borrow caps are a new feature in Aave V3, and define the maximum amount of an asset which can be borrowed. Borrow caps can be used to prevent traditional and flash borrowing of an asset which may experience a price exploit and lead to protocol insolvency. A borrow cap is an optional parameter, and the value will depend on the circulating and maximum supply of the asset.
    * **Isolation Mode**
      Isolation mode is a new feature in Aave V3, which can be used to limit the systemic risk of listing riskier assets. Isolation mode limits an asset to only be
    * **Borrowing Enabled**
      Borrowing enabled is a boolean flag which defines whether an asset can be borrowed or not. An asset with borrowing disabled will have a supply and borrow APY of 0, but can still be enabled as collateral.
    * **Reserve Factor**
      The reserve factor is a percentage of protocol interest which goes to the Aave Ecosystem Reserve. Each Aave market has a collector contract which stores the revenue from the reserve factor. The collector contracts make up the ecosystem reserve which is controlled by Aave Governance, and used to promote ecosystem growth through incentives or other initiatives.


    Checkout the [template](https://docs.aave.com/governance/aip-templates/template-asset-onboarding) for an asset listing ARC, or some examples from recently listed assets:

    * [DPI](https://governance.aave.com/t/arc-add-support-for-defi-pulse-index-dpi/3576) - Collateral Asset
    * [FRAX](https://governance.aave.com/t/proposal-add-support-for-frax/2621) - Borrow Only



## AIP

The AIP is a document containing the proposal details which is uploaded to IPFS. The hash of this documented is passed as a parameter when the on-chain proposal is submitted. To create an AIP for a new asset listing follow the steps from the AIP [repo](https://aave.github.io/aip/).

Sample AIPs:

* [https://github.com/aave/aip/pull/133](https://github.com/aave/aip/pull/133)
* [https://github.com/aave/aip/pull/122](https://github.com/aave/aip/pull/122)

Once the AIP has been reviewed and merged to generate an ipfs hash, and the payload has been created, the proposal can now be submitted on-chain.

## Create Proposal
Once the AIP has been reviewed, the next step is to initialize reserves on-chain. In V3, address with `ASSET_LISTING_ADMIN` role can call [initReserves]() on PoolConfigurator to add new asset to the market.

### Add To Aave UI
In order for your reward token name and symbol to appear on the Aave frontend, you will need to add your asset to the Aave Interface repo.