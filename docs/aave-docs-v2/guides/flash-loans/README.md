# Flash Loans

Flash Loans are special uncollateralised loans that allow the borrowing of an asset, as long as the borrowed amount (and a fee) is returned before the end of the transaction. There is no real world analogy to Flash Loans, so it requires some basic understanding of how state is managed within blocks in blockchains.

{% hint style="warning" %}
Flash Loans are an advanced concept aimed at developers. You **must** have a good understanding of Ethereum, programming, and smart contracts to take advantage of them.
{% endhint %}

## Overview

For developers, a helpful mental model to consider when developing your solution:

1. Your contract calls the `LendingPool` contract, requesting a Flash Loan of a certain `amounts` of `reserves` using [`flashLoan()`](../../the-core-protocol/lendingpool/#flashloan).
2. After some sanity checks, the `LendingPool` transfers the requested `amounts` of the `reserves` to your contract, then calls `executeOperation()` on your contract (or another contract that you specify as the `_receiver`).
3. Your contract, now holding the flash loaned `amounts`, executes any arbitrary operation in its code.&#x20;
   * If you are performing a **'traditional' flash loan**, then when your code has finished, you transfer the flash loaned `amounts` of `reserves` back to the `LendingPool`.
     * The `LendingPool` contract updates the relevant details of the reserves and **pulls** the flash loaned amount + fee.&#x20;
       * This is different from v1 flash loans, where the flash loaned amount needed to be pushed back to the `LendingPool` contract.
     * If the amount owing is not available (due to a lack of balance or approval), then the transaction is reverted.
   * If you are performing a **flash loan to incur debt** (see the `mode` parameter in the [`flashLoan()`](../../the-core-protocol/lendingpool/#flashloan) function), then a debt will be incurred.
4. All of the above happens in 1 transaction (hence in a single ethereum block).

### Applications of Flash Loans

Aave Flash Loans are already used extensively with Aave v2 for swapping and/or migrating positions. Other examples in the wild include:

* Arbitrage between assets, without needing to have the principal amount to execute the arbitrage. Example: [ArbitrageDAO](https://medium.com/@bneiluj/flash-boys-arbitrage-dao-c0b96d094f93).
* Swapping collateral of loan positions, without having to repay the debt of the loan positions. Example: [Collateral Swap](https://collateralswap.com), [DeFiSaver](https://defisaver.com).
* Other examples and ideas are listed on our blog [here](https://medium.com/aave/sneak-peek-at-flash-loans-f2b28a394d62) and [here](https://medium.com/aave/building-the-post-liquidation-era-4e650935fc88).

## Example Code

The examples listed below are code examples from the community or from the Genesis team, which can be used as a starter or a guide for your own project.

[Flash loans example](https://github.com/aave/code-examples-protocol/tree/main/V2/Flash%20Loan%20-%20Batch) (as detailed in the [Step by step](./#step-by-step))

[Flash loans using Scaffold-ETH](https://github.com/kartojal/flash-loans-workshop) by David K

[Flash loans using Remix](https://github.com/fifikobayashi/AaveV2-BatchFlashDemo) by Fiona K

[Flash Loan Tutorial Video](https://www.youtube.com/watch?v=Aw7yvGFtOvI) by Alpha Chain

## Flash loan fee

The flash loan fee is currently 0.09%, changeable via the normal governance process. To get the current value, call `FLASHLOAN_PREMIUM_TOTAL()` on the LendingPool contract, e.g. [number 1 here](https://etherscan.io/address/0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9#readProxyContract).

## Step by step

{% hint style="info" %}
TL;DR: A reference example flash loan contract can be found on [Kovan etherscan](https://kovan.etherscan.io/address/0x6d3ff1dc2f50456a83105ccf9ccd70e960de5e75#code) and [Github code examples repo](https://github.com/aave/code-examples-protocol/blob/main/V2/Flash%20Loan%20-%20Batch/MyV2FlashLoan.sol).
{% endhint %}

### 1. Setting up

Your contract that receives the flash loaned amounts **must** conform to the [`IFlashLoanReceiver`](iflashloanreceiver.md) interface by implementing the relevant `executeOperation()` function. In the example below, we inherit from [`FlashLoanReceiverBase`](iflashloanreceiver.md#flashloanreceiverbase), which conforms to the `IFlashLoanReceiver`.

Also note that since the owed amounts will be _pulled_ from your contract, your contract must give allowance to the `LendingPool` to pull those funds to pay back the flash loan debts + premiums.&#x20;

```javascript
pragma solidity 0.6.12;

import { FlashLoanReceiverBase } from "./FlashLoanReceiverBase.sol";
import { ILendingPool } from "./ILendingPool.sol";
import { ILendingPoolAddressesProvider } from "./ILendingPoolAddressesProvider.sol";
import { IERC20 } from "./IERC20.sol";

/** 
    !!!
    Never keep funds permanently on your FlashLoanReceiverBase contract as they could be 
    exposed to a 'griefing' attack, where the stored funds are used by an attacker.
    !!!
 */
contract MyV2FlashLoan is FlashLoanReceiverBase {

    /**
        This function is called after your contract has received the flash loaned amount
     */
    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    )
        external
        override
        returns (bool)
    {

        //
        // This contract now has the funds requested.
        // Your logic goes here.
        //
        
        // At the end of your logic above, this contract owes
        // the flashloaned amounts + premiums.
        // Therefore ensure your contract has enough to repay
        // these amounts.
        
        // Approve the LendingPool contract allowance to *pull* the owed amount
        for (uint i = 0; i < assets.length; i++) {
            uint amountOwing = amounts[i].add(premiums[i]);
            IERC20(assets[i]).approve(address(LENDING_POOL), amountOwing);
        }
        
        return true;
    }
}
```

### 2. Calling `flashLoan()`

To call `flashloan()` on the `LendingPool`, we need to pass in the relevant parameters. There are 3 ways you can do this.

#### From an EOA ('normal' ethereum account)

To use an EOA, send a transaction to the relevant `LendingPool` calling the `flashLoan()` function. See the [`flashLoan()`](../../the-core-protocol/lendingpool/#flashloan) function documentation for parameter details, ensuring you use your contract address from step 1 for the `receiverAddress`.

#### From a different contract

Similar to sending a transaction from an EOA as above, ensure the `receiverAddress` is your contract address from step 1.

#### From the _same_ contract

If you want to use the same contract as in step 1, use `address(this)` for the `receiverAddress` parameter in the [flashLoan function.](../../the-core-protocol/lendingpool/#flashloan)

The example below shows this third case, where the `executeOperation()` is in the same contract calling `flashLoan()` on the `LendingPool`.

{% hint style="danger" %}
Never keep funds permanently on your `FlashLoanReceiverBase` contract as they could be exposed to a ['griefing' attack](https://ethereum.stackexchange.com/a/92457/19365), where the stored funds are used by an attacker.
{% endhint %}

```javascript
pragma solidity 0.6.12;

import { FlashLoanReceiverBase } from "./FlashLoanReceiverBase.sol";
import { ILendingPool } from "./ILendingPool.sol";
import { ILendingPoolAddressesProvider } from "./ILendingPoolAddressesProvider.sol";
import { IERC20 } from "./IERC20.sol";

/** 
    !!!
    Never keep funds permanently on your FlashLoanReceiverBase contract as they could be 
    exposed to a 'griefing' attack, where the stored funds are used by an attacker.
    !!!
 */
contract MyV2FlashLoan is FlashLoanReceiverBase {

    /**
        This function is called after your contract has received the flash loaned amount
     */
    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    )
        external
        override
        returns (bool)
    {

        //
        // This contract now has the funds requested.
        // Your logic goes here.
        //
        
        // At the end of your logic above, this contract owes
        // the flashloaned amounts + premiums.
        // Therefore ensure your contract has enough to repay
        // these amounts.
        
        // Approve the LendingPool contract allowance to *pull* the owed amount
        for (uint i = 0; i < assets.length; i++) {
            uint amountOwing = amounts[i].add(premiums[i]);
            IERC20(assets[i]).approve(address(LENDING_POOL), amountOwing);
        }
        
        return true;
    }
    
    function myFlashLoanCall() public {
        address receiverAddress = address(this);

        address[] memory assets = new address[](2);
        assets[0] = address(INSERT_ASSET_ONE_ADDRESS);
        assets[1] = address(INSERT_ASSET_TWO_ADDRESS);

        uint256[] memory amounts = new uint256[](2);
        amounts[0] = INSERT_ASSET_ONE_AMOUNT;
        amounts[1] = INSERT_ASSET_TWO_AMOUNT;

        // 0 = no debt, 1 = stable, 2 = variable
        uint256[] memory modes = new uint256[](2);
        modes[0] = INSERT_ASSET_ONE_MODE;
        modes[1] = INSERT_ASSET_TWO_MODE;

        address onBehalfOf = address(this);
        bytes memory params = "";
        uint16 referralCode = 0;

        LENDING_POOL.flashLoan(
            receiverAddress,
            assets,
            amounts,
            modes,
            onBehalfOf,
            params,
            referralCode
        );
    }
}
```

### 3. Completing the flash loan

Once you have performed your logic with the flash loaned assets (in your `executeOperation()` function), you will need to pay back the flash loaned amounts if you used `mode=0` for any of the assets in the [`modes`](../../the-core-protocol/lendingpool/#flashloan) parameter.

#### Paying back a flash loaned asset

Ensure your contract has the relevant amount + premium to payback the loaned asset. You can calculate this by taking the sum of the relevant entry in the `amounts` and `premiums` array passed into the `executeOperation()` function.

You **do not** need to transfer the owed amount back to the `LendingPool`. The funds will be automatically _pulled_ at the conclusion of your operation.

#### Incurring a debt (i.e. not immediately paying back)

If you initially used a `mode=1` or `mode=2` for any of the assets in the [`modes`](../../the-core-protocol/lendingpool/#flashloan) parameter, then the address passed in for `onBehalfOf` will incur the debt **if** the `onBehalfOf` address has previously approved the `msg.sender` to incur debts on their behalf.

This means that you can have some assets that are paid back immediately, while other assets incur a debt.

## Encoding and Decoding Parameters

If you would like to pass parameters into your flash loan function, you will first need to encode them, then decode them in your `executeOperation()`.

### Encoding

If you're encoding in solidity, you can use the in-built `abi.encode()`:

```javascript
// Encoding an address and a uint
bytes memory params = abi.encode(address(this), 1234);
```

If you're encoding off-chain, then you can use a package like web3.js which has an [`abi.encodeParameters()`](https://web3js.readthedocs.io/en/v1.3.0/web3-eth-abi.html?highlight=encodeParameters#encodeparameters):

```javascript
const params = web3.eth.abi.encodeParameters(
	["bytes32"],
	[
		web3.utils.utf8ToHex("some_value")
	]
)
```

### Decoding

When decoding in your `executeOperation()`, you will need to use the in-build `abi.decode()`:

```javascript
(bytes32 someValue) = abi.decode(params, (bytes32));
```

For more, see the [official Solidity docs](https://docs.soliditylang.org/en/v0.8.0/units-and-global-variables.html?highlight=abi.decode#abi-encoding-and-decoding-functions).
