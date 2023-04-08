# Voting & Governance

Aave Governance V2 is an exciting new evolution of on-chain governance, allowing unique features such as delegated voting and proposition powers, rapid protocol upgrades via short time lock executors, and governance upgrades via long time lock executors.&#x20;

This ensures the protocol can rapidly adjust to changing market conditions, as well as upgrade core parts of the protocol as time goes on.

{% hint style="info" %}
This section is for developers and technical users. For a non-technical overview, see the [Protocol Governance section of Aavenomics](https://docs.aave.com/aavenomics/governance) or the [Governance Docs](https://docs.aave.com/governance/).
{% endhint %}

![](../../.gitbook/assets/Untitled.png)

## Overview

AAVE and/or stkAAVE token holders receive governance powers proportionally to the sum of their balance.

There are initially two powers associated with each governance token:

* The **proposal power** that gives access to creating and sustaining a proposal.
* The **voting power** which is used to vote for or against existing proposals.

Any user can chose to delegate one or both of the governance powers associated with a token, either through our governance portal or programatically.

{% hint style="info" %}
A user that has received delegated power can not forward this delegated power to another delegatee. I.e. delegated power cannot be passed on further.
{% endhint %}

The code for Aave Governance V2 can be found [on Github.](https://github.com/aave/governance-v2)

## Deployed Contracts

{% tabs %}
{% tab title="Mainnet" %}
| Contract                                                                                                            | Address and ABI                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [AaveGovernanceV2](https://github.com/aave/governance-v2/blob/master/contracts/governance/AaveGovernanceV2.sol)     | [0xEC568fffba86c094cf06b22134B23074DFE2252c](https://etherscan.io/address/0xEC568fffba86c094cf06b22134B23074DFE2252c)              |
| [Executor (short)](https://github.com/aave/governance-v2/blob/master/contracts/governance/Executor.sol)             | [0xee56e2b3d491590b5b31738cc34d5232f378a8d5](https://etherscan.io/address/0xee56e2b3d491590b5b31738cc34d5232f378a8d5#readContract) |
| [Executor (long)](https://github.com/aave/governance-v2/blob/master/contracts/governance/Executor.sol)              | [0x79426A1c24B2978D90d7A5070a46C65B07bC4299](https://etherscan.io/address/0x79426A1c24B2978D90d7A5070a46C65B07bC4299)              |
| [GovernanceStrategy](https://github.com/aave/governance-v2/blob/master/contracts/governance/GovernanceStrategy.sol) | [0xb7e383ef9b1e9189fc0f71fb30af8aa14377429e](https://etherscan.io/address/0xb7e383ef9b1e9189fc0f71fb30af8aa14377429e)              |
| [AAVE](https://github.com/aave/aave-token-v2/blob/master/contracts/token/AaveTokenV2.sol)                           | [0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9](https://etherscan.io/address/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9)              |
| [stkAAVE](https://github.com/aave/aave-stake-v2/blob/master/contracts/stake/StakedAaveV2.sol)                       | [0x4da27a545c0c5b758a6ba100e3a049001de870f5](https://etherscan.io/address/0x4da27a545c0c5b758a6ba100e3a049001de870f5)              |
| GovV2Helper                                                                                                         | [0x16ff7583ea21055Bf5F929Ec4b896D997Ff35847](https://etherscan.io/address/0x16ff7583ea21055bf5f929ec4b896d997ff35847#code)         |
| Ecosystem Reserve                                                                                                   | [0x25F2226B597E8F9514B3F68F00f494cF4f286491](https://etherscan.io/address/0x25f2226b597e8f9514b3f68f00f494cf4f286491)              |
{% endtab %}

{% tab title="Kovan" %}
| Contract                                                                                                            | Address and ABI                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [AaveGovernanceV2](https://github.com/aave/governance-v2/blob/master/contracts/governance/AaveGovernanceV2.sol)     | [0xc2ebab3bac8f2f5028f5c7317027a41ebfca31d2](https://kovan.etherscan.io/address/0xc2ebab3bac8f2f5028f5c7317027a41ebfca31d2)      |
| [Executor (short)](https://github.com/aave/governance-v2/blob/master/contracts/governance/Executor.sol)             | [0x2012b02574f32a96b9cfb8ba7fdfd589d5c70f50](https://kovan.etherscan.io/address/0x2012b02574f32a96b9cfb8ba7fdfd589d5c70f50)      |
| [Executor (long)](https://github.com/aave/governance-v2/blob/master/contracts/governance/Executor.sol)              | [0x7e5195b0a6a60b371ba3276032cf6958eadfa652](https://kovan.etherscan.io/address/0x7e5195b0a6a60b371ba3276032cf6958eadfa652#code) |
| [Executor (low thresh)](https://github.com/aave/governance-v2/blob/master/contracts/governance/Executor.sol)        | [0xf6a8a1411faa2bf374035bb0e9e3268e24a3ca18](https://kovan.etherscan.io/address/0xf6a8a1411faa2bf374035bb0e9e3268e24a3ca18)      |
| [GovernanceStrategy](https://github.com/aave/governance-v2/blob/master/contracts/governance/GovernanceStrategy.sol) | [0xf2e2c705712012f079416503e5d3316d79bf8a6c](https://kovan.etherscan.io/address/0xf2e2c705712012f079416503e5d3316d79bf8a6c)      |
| [AAVE](https://github.com/aave/aave-token-v2/blob/master/contracts/token/AaveTokenV2.sol)                           | [0xb597cd8d3217ea6477232f9217fa70837ff667af](https://kovan.etherscan.io/address/0xb597cd8d3217ea6477232f9217fa70837ff667af)      |
| [stkAAVE](https://github.com/aave/aave-stake-v2/blob/master/contracts/stake/StakedAaveV2.sol)                       | [0xf2fbf9a6710afda1c4aab2e922de9d69e0c97fd2](https://kovan.etherscan.io/address/0xf2fbf9a6710afda1c4aab2e922de9d69e0c97fd2)      |
| GovV2Helper                                                                                                         | [0xffd5BEb5712952FC9a9DDC7499487422B29Fdda6](https://kovan.etherscan.io/address/0xffd5BEb5712952FC9a9DDC7499487422B29Fdda6#code) |
{% endtab %}
{% endtabs %}

## Audits

| Auditor                                                                                                           | Audit Type     |
| ----------------------------------------------------------------------------------------------------------------- | -------------- |
| [PeckShield](https://github.com/aave/governance-v2/blob/master/audits/PeckShield-Audit-AaveGovernance2-final.pdf) | Smart Contract |

## Proposal Types

There are two types of proposals with different parameters which affect the length and execution of a proposal, i.e. critical proposals that affect governance consensus require more voting time and a higher vote differential, whereas proposals affecting only protocol parameters require less voting time and can be quickly implemented.&#x20;

{% hint style="info" %}
As an initial safeguard to the protocol, a **guardian** account, controlled by a community multisig, is able to cancel a proposal before the proposal is executed.
{% endhint %}

Each type of proposal can only be validated and executed by a certain executor.

### Short time lock executor

The short time lock executor can execute proposals that change parts of the Aave protocol or the Ecosystem reserve that require quick intervention.

### Long time lock executor

The long time lock executor can execute proposals that change parts of the Aave protocol that affect governance consensus.

## Proposition/Voting Power

An account's proposition/voting power at a given block is equal to the snapshot of that account's AAVE/stkAAVE balances plus the balances of all delegators.

An account's balance contributes to both proposition and voting power while delegators can choose to delegate proposition power, voting power or both to another account.

A creator must have proposition power higher than `PROPOSITION_THRESHOLD` at the block before the proposal is created and until the proposal is executed.

A user can vote only once. The weight of this vote is equal to the user's voting power at the block when [`submitVote()`](./#submitvote) is called.

Both AAVE and stkAAVE maintain `_propositionSnapshots`/`_votingSnapshots` mappings. New snapshots are taken on every call to:

* `transfer()`
* [`delegate()`](./#delegate) / [`delegateByType()`](./#delegatebytype)

Proposition/Voting power available at a specified block can be fetched from [AaveGovernanceStrategy](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/GovernanceStrategy.sol#L51)&#x20;

* System: Total supply of AAVE at that block[`getVotingPropositionSupplyAt()/getTotalPropositionSupplyAt()`](./#gettotalvotingsupplyat-gettotalpropositionsupplyat)
* &#x20;User: AAVE + stkAAVE snapshot of the user at the block[`getVotingPowerAt(), getPropositionPowerAt()`](./#getvotingpowerat-getpropositionpowerat)

## Proposal Life Cycle

### 0) Off-chain process

The ARC and AIP process should be followed, with a resulting AIP and payload ready to be used for the proposal. Learn more about the [ARC and AIP process here](https://docs.aave.com/governance/).

The AIP should be merged into the AIP repository, with an [associated IPFS hash of the parsed AIP file](https://github.com/aave/aip-uploader), before the next steps are taken.

### 1) Proposal Creation

A proposal can be created by calling [`create()`](./#create), with the following caveats:

* The proposer must have a proposal power higher than [`PROPOSITION_THRESHOLD`](./#proposition\_threshold).
* The proposer needs to maintain the proposal power threshold or higher until the proposal is actually executed (i.e. during the vote and until the actual execution of the proposal)

The proposal is now in a `PENDING` state until the vote begins.

### 2) Proposal Voting

If `votingDelay = 0`, then the voting period begins at the next block. Otherwise the voting begins after the `votingDelay`. The `votingDelay` value can be fetched from [`getVotingDelay()`](./#getvotingdelay). A snapshot of voting powers is taken and can no longer be delegated/transferred for the proposal being voted on.&#x20;

The proposal state is `ACTIVE` and users can submit a vote for or against the proposal, weighted by the users total voting power (tokens + delegated voting power), within the allotted [`VOTING_DURATION`](./#voting\_duration).

### 3) End of Voting Period

For a proposal to pass:

* The voting power (in % of total voting power) of for-votes needs to reach the quorum set by the [`MINIMUM_QUORUM`](./#minimum\_quorum) parameter, and
* The difference between for-votes and against-votes (in % of total voting power) needs to exceed the vote differential threshold set by the [`VOTE_DIFFERENTIAL`](./#vote\_differential) parameter.

If the proposal has passed, then the proposal state becomes `SUCCEEDED`, otherwise it is `FAILED`

### 4) Proposal Queuing and Execution

A `SUCCEEDED` proposal can be queued and will be executed after the execution delay and before grace period expiration. The `delay` can be fetched from [`getDelay()`](./#getdelay) and the `GRACE_PERIOD` can be fetched from [`GRACE_PERIOD()`](./#grace\_period).

The validation and execution of the proposal is performed by the time lock executor.

A queued proposal state is `QUEUED.`

A successfully executed proposal state is `EXECUTED`.

If a queued proposal has not been executed before expiration, then the proposal state is `EXPIRED`.

### (Optional) Proposal Canceling

If the proposal creator's proposal power decrease and no longer meet the [`PROPOSITION_THRESHOLD`](./#proposition\_threshold), any user can cancel the proposal.

In addition as an initial safeguard to the protocol, a **guardian** account, controlled by a communtity multisig, is able to cancel a proposal before a proposal is executed.

A cancelled proposal state is `CANCELED`.

## Integrating Governance

### Delegation

To perform delegation in your integration, call the function [`delegate()`](./#delegate) or [`delegateByType()`](./#delegatebytype) on the AAVE and/or the stkAAVE token contracts to delegate one or both of the voting and proposition powers.

### Voting

To enable your users to vote:

1. Retrieve a list of proposals and associated details. This can be done via the [subgraph](./#subgraphs) or directly from the on-chain governance contracts.
2. Vote on the proposals by using  [`submitVote()`](./#submitvote).
3. Fetch the state of the proposal via the subgraph or directly on-chain.

### Proposals

To fetch a proposal and its associated details, call `getProposal()` or `getProposals()`.

To get the token power of an address, call `getTokenPower()`.

## Subgraphs

The [governance subgraph](https://github.com/aave/governance-v2-subgraph) gives access to three main objects:&#x20;

* Proposals with their states and votes
* Available executors and their parameters
* Votes&#x20;

Subgraphs on the graph explorer:&#x20;

* [Mainnet](https://thegraph.com/explorer/subgraph/aave/governance-v2)
* [Kovan](https://thegraph.com/explorer/subgraph/aave/governance-v2-kovan)

Example query for fetching active proposals

```graphql
{
  proposals(where: {state: Active}) {
    id
    state
    ipfsHash
    creator
    executor {
      id
      authorized
      propositionThreshold
      votingDuration
      voteDifferential
    }
    votes(first: 5) {
      id
      voter
      votingPower
      support    
  	}
  }
}
```

## Relevant Methods

### create()

Contract: [`AaveGovernanceV2`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/AaveGovernanceV2.sol#L78)

**`function create(address executor, address[] memory targets, uint256[] memory values, string[] memory signatures, bytes[] memory calldatas, bool[] memory withDelegatecalls, bytes32 ipfsHash) external returns (uint256 proposalId)`**

Creates a proposal for a specific executor. A proposal includes a list of underlying transactions.

{% hint style="danger" %}
The caller must have the necessary proposition power to create a proposal.
{% endhint %}

| Parameter           | Type       | Description                                                                                                      |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| `executor`          | address    | Address of the time-locked executor                                                                              |
| `targets`           | address\[] | List of the targeted addresses by proposal transactions                                                          |
| `values`            | uint256\[] | List of the Ether values of proposal transactions                                                                |
| `signatures`        | bytes\[]   | list of function signatures (can be empty) to be used when creating the callDatas of proposal transactions       |
| `calldatas`         | bytes\[]   | list of callDatas: if associated signature empty, encoded callData, else arguments for the function signature    |
| `withDelegatecalls` | bool\[]    | List of bool determining if the proposal transactions should execute the transaction via direct or delegate call |
| `ipfsHash`          | bytes      | ipfsHash of the associated AIP                                                                                   |

**return values**

| Parameter    | Type    | Description            |
| ------------ | ------- | ---------------------- |
| `proposalId` | uint256 | The Id of the proposal |

### PROPOSITION\_THRESHOLD()

Contract: [`ProposalValidator`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ProposalValidator.sol#L20) `(Executor)`

**`function PROPOSITION_THRESHOLD()`**

Returns the minimum percentage of the voting token supply needed to submit a proposal (in BPS, e.g. 1 bps = 0.01%, 10,000 bps = 100%) in the [Proposal Creation step](./#1-proposal-creation).

Currently the Short time lock executor is 0.5% and the Long time lock executor is 2%.

### getVotingDelay()

Contract: [`AaveGovernanceV2`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/AaveGovernanceV2.sol#L326)

**`function getVotingDelay()`**

Returns the current delay before a created proposal can be voted on by the community in the [Proposal Creation phase](./#1-proposal-creation).

### VOTING\_DURATION()

Contract: [`ProposalValidator`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ProposalValidator.sol#L21) `(Executor)`

**`function VOTING_DURATION()`**

Returns the duration of the voting period (in blocks) in the [Proposal Creation phase](./#1-proposal-creation).

Currently the Short time lock executor is 3 days and the Long time lock executor is 10 days.

### MINIMUM\_QUORUM()

Contract: [`ProposalValidator`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ProposalValidator.sol#L23) `(Executor)`

**`function MINIMUM_QUORUM()`**

Returns the  minimum percentage of the voting token supply of 'for' (i.e. positive) votes of a proposal to successfully pass (in BPS, e.g. 1 bps = 0.01%, 10,000 bps = 100%), in [End of Voting phase](./#3-end-of-voting-period).

Currently the Short time lock executor is 2% and the Long time lock executor is 20%.

### VOTE\_DIFFERENTIAL()

Contract: [`ProposalValidator`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ProposalValidator.sol#L22) `(Executor)`

**`function VOTE_DIFFERENTIAL()`**

Returns the percentage of the voting token supply of 'for' (i.e. positive) votes needed over 'against' (i.e.negative) votes for a proposal to successfully pass (in BPS, e.g. 1 bps = 0.01%, 10,000 bps = 100%), in [End of Voting phase](./#3-end-of-voting-period).

Currently the Short time lock executor is 0.5% and the Long time lock executor is 15%.

### getDelay()

Contract: [`ExecutorWithTimeLock`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ExecutorWithTimelock.sol#L250) `(Executor)`

**`function getDelay()`**

Returns the delay between queuing and execution of a proposal (in seconds) in [Proposal Queueing and Execution Period](./#4-proposal-queuing-and-execution).

Currently the Short time lock executor is 1 day and the Long time lock executor is 7 days.

### GRACE\_PERIOD()

Contract: [`ExecutorWithTimeLock`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/ExecutorWithTimelock.sol#L19) `(Executor)`

**`function GRACE_PERIOD()`**

Returns the time after `delay` ([`getDelay()`](./#getdelay)) in seconds when a proposal can be executed in [Proposal Queueing and Execution Period](./#4-proposal-queuing-and-execution).

Currently the Short time lock executor is 5 days and the Long time lock executor is 5 days.

### delegate()

Contracts: [`AAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L44), [`stkAAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L44)

**`function delegate(address delegatee)`**

Delegate both powers of a token (vote and proposition) to a delegatee

| Parameter   | Type    | Description                            |
| ----------- | ------- | -------------------------------------- |
| `delegatee` | address | Address receiving the delegated powers |

### delegateByType()

Contracts: [`AAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L36), [`stkAAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L36)

**`function delegateByType(address delegatee, uint8 delegationType)`**

Delegate one specific power of a token (vote or proposition) to a delegatee

| Parameter        | Type    | Description                            |
| ---------------- | ------- | -------------------------------------- |
| `delegatee`      | address | Address receiving the delegated powers |
| `delegationType` | uint8   | 0 = Voting, 1 = Proposition            |

{% hint style="info" %}
To reset delegation, set the delegatee address to the delegator address.
{% endhint %}

### submitVote()

Contract: [`AaveGovernanceV2`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/AaveGovernanceV2.sol#L237)``

**`submitVote(uint256 proposalId, bool support)`**

Submits a vote by the caller.

| Parameter    | Type    | Description                                                |
| ------------ | ------- | ---------------------------------------------------------- |
| `proposalId` | uint256 | The ID of the governance proposal.                         |
| `support`    | bool    | A value indicating their vote (For: true, Against: false). |

### getDelegateeByType()

Contracts: [`AAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L53), [`stkAAVE`](https://github.com/aave/aave-token-v2/blob/6ebf51ddbdfb6ae66de0b4c191b978ef5149a9ce/contracts/token/base/GovernancePowerDelegationERC20.sol#L53)

**`function getDelegateeByType(address delegator, uint8 delegationType) returns(address delegatee)`**

Returns the address of the delegatee for a delegator

| Parameter        | Type    | Description                                   |
| ---------------- | ------- | --------------------------------------------- |
| `delegator`      | address | Address from which to fetch its the delegatee |
| `delegationType` | uint8   | 0 = Voting, 1 = Proposition                   |

{% hint style="info" %}
If the return value is the delegator address, then there is no delegation.
{% endhint %}

### getVotingPowerAt(), getPropositionPowerAt()

Contract: [`AaveGovernanceStrategy`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/GovernanceStrategy.sol#L77)

**`function get{Voting,Proposition}PowerAt(address user, uint256 blockNumber) returns(power uint256)`**

Returns the Voting/Proposition power of the user at a specified block

| Parameter     | Type    | Description                                                     |
| ------------- | ------- | --------------------------------------------------------------- |
| `user`        | address | Address from which to fetch the Voting/Proposition power        |
| `blockNumber` | uint256 | Block number at which to calculate the Voting/Proposition power |

{% hint style="info" %}
When submitting a vote, the voting power is calculated at the time of the beginning of the vote.
{% endhint %}

### getTotalVotingSupplyAt(), getTotalPropositionSupplyAt()

Contract: [`AaveGovernanceStrategy`](https://github.com/aave/governance-v2/blob/f7761d9ee6347a3996bea665103d8e2080d8b9b2/contracts/governance/GovernanceStrategy.sol#L51)

**`function getTotal{Voting,Proposition}SupplyAt(uint256 blockNumber) returns(totalSupply uint256)`**

Returns the total Voting/Proposition power available at a specified block

| Parameter     | Type    | Description                                                           |
| ------------- | ------- | --------------------------------------------------------------------- |
| `blockNumber` | uint256 | Block number at which to calculate the Voting/Proposition total power |

{% hint style="info" %}
The total available power is equal to the total supply of not staked AAVE + the total supply of staked AAVE = total supply of AAVE
{% endhint %}

### getProposal()

Contract: `GovV2Helper`

**`function getProposal(uint256 id, IAaveGovernanceV2 governance)`**

Returns the details of a proposal.

| Parameter    | Type              | Description             |
| ------------ | ----------------- | ----------------------- |
| `id`         | uint256           | The ID of the proposal  |
| `governance` | IAaveGovernanceV2 | The Governance contract |

### getProposals()

Contract: `GovV2Helper`

**`function getProposals(uint256 skip, uint256 limit, IAaveGovernanceV2 governance)`**

Returns an array of proposals with associated details.

| Parameter    | Type              | Description                                                             |
| ------------ | ----------------- | ----------------------------------------------------------------------- |
| `skip`       | uint256           | Use to skip a number of proposals. Use 0 to start from the beginning.   |
| `limit`      | uint256           | The limit of proposals to fetch. Use `uint(-1)` to fetch all proposals. |
| `governance` | IAaveGovernanceV2 | The Governance contract.                                                |

### getTokensPower()

Contract: `GovV2Helper`

**`function getTokensPower(address user, address[] memory tokens)`**

Return the power (voting and proposition) of the `user`.&#x20;

| Parameter | Type       | Description                      |
| --------- | ---------- | -------------------------------- |
| `user`    | addresss   | The address of the user.         |
| `tokens`  | address\[] | The array of governance tokens.  |

Returns the `votingPower`, `delegatedAddressVotingPower`, `propositionPower`, `delegatedAddressPropositionPower`.
