# Permissions

The `ACLManager` (Asset Control List Manager) contract manages the permissions of an Aave market. The Aave Governance serves as the `ROLE_ADMIN` and can approve any of the defined roles: `RISK_ADMIN`, `POOL_ADMIN`, `ASSET_LISTING_ADMIN`, `BRIDGE`, `FLASH_BORROWER`.

More details on roles can be found [here](../../core-contracts/aclmanager.md/#roles).

This guide details the steps for enabling or disabling permissions on the `ACLManager`:

- [ARC]()
- [AIP]()
- [Creating the proposal]()

## ARC

The ARC (Aave Request for Comment) is the first step in the proposal process. This is where the idea is proposed, and the community can discuss the proposal. All ARCs should follow these standard [requirements](https://docs.aave.com/governance/arcs). Permissions proposals should provide extensive background on the qualifications and reputability of the requesting entity.

## AIP

The AIP is a document containing the proposal details which is uploaded to IPFS. The hash of this documented is passed as a parameter when the on-chain proposal is submitted. To create an AIP for adjusting address permissions, follow the steps from the AIP [repo](https://aave.github.io/aip/).

Once the AIP has been reviewed and merged to generate an ipfs hash, and the payload has been created, the proposal can now be submitted on-chain.