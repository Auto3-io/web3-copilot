# AAVE Token

The AAVE token is an ERC-20 compatible token with the addition of a snapshot feature (used in governance balance tracking) and integrates [EIP 2612](https://github.com/ethereum/EIPs/blob/8a34d644aacf0f9f8f00815307fd7dd5da07655f/EIPS/eip-2612.md) permit function, allowing gas-less transactions and one transaction approval/transfer.

{% hint style="info" %}
This section will cover the technical aspects of the token.&#x20;

For governance, security, and incentive details, see the [Aavenomics](https://docs.aave.com/aavenomics/) documentation.

For LEND to AAVE migration, see the [v1 migration docs](https://docs.aave.com/developers/developing-on-aave/the-protocol/aave-token#lend-to-aave-migration).
{% endhint %}

The source code for the AAVE token can be found on [Github here](https://github.com/aave/aave-token).&#x20;

## Deployed Contracts

{% tabs %}
{% tab title="Mainnet" %}
| Proxy Contracts                                                                                                                | Address and ABIs                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| [AAVE token](https://github.com/aave/aave-token/blob/master/contracts/open-zeppelin/InitializableAdminUpgradeabilityProxy.sol) | [0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9](https://etherscan.io/address/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9#code) |
{% endtab %}
{% endtabs %}

## Audits

| Auditor                                                                                                              | Audit Type              |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [Consensys Diligence](https://diligence.consensys.net/audits/private/g6kd633m-aave-token/) (AAVE token)              | Smart Contract          |
| [Certik](https://github.com/aave/aave-token/blob/master/audits/AaveTokenReport\_CertiK.pdf) (AAVE token)             | Smart Contract          |
| [Certora](https://github.com/aave/aave-token/blob/master/audits/AaveTokenVerification\_by\_Certora.pdf) (AAVE token) | Properties Verification |

## Methods

Besides the standard ERC20 token features (`transfer()`, `balanceOf()`, `allowance()`, etc), the following features are also available.

### permit()

**`function permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s ) external`**

Allows a user to permit another account (or contract) to use their funds using a signed message. This enables gas-less transactions and single approval/transfer transactions.

| Parameter  | Type    | Description                                                                            |
| ---------- | ------- | -------------------------------------------------------------------------------------- |
| `owner`    | address | The owner of the funds                                                                 |
| `spender`  | address | The spender for the funds                                                              |
| `value`    | uint256 | The amount the `spender` is permitted to use                                           |
| `deadline` | uint256 | The deadline timestamp that the permit is valid. Use `type(uint).max` for no deadline. |
| `v`        | uint8   | Signature parameter                                                                    |
| `r`        | bytes32 | Signature parameter                                                                    |
| `s`        | bytes32 | Signature parameter                                                                    |

{% tabs %}
{% tab title="Web3.js" %}
```javascript
import { signTypedData_v4 } from 'eth-sig-util'
import { fromRpcSig } from 'ethereumjs-util'

// ... other imports

import AaveTokenAbi from "./AaveTokenAbi.json"

// ... setup your web3 provider

const aaveTokenAddress = "AAVE_TOKEN_ADDRESS"
const aaveTokenContract = new web3.eth.Contract(AaveTokenAbi, aaveTokenAddress)

const privateKey = "YOUR_PRIVATE_KEY_WITHOUT_0x"
const chainId = 1
const owner = "OWNER_ADDRESS"
const spender = "SPENDER_ADDRESS"
const value = 100 // Amount the spender is permitted
const nonce = 1 // The next valid nonce, use `_nonces()`
const deadline = 1600093162

const permitParams = {
  types: {
    EIP712Domain: [
      { name: "name", type: "string" },
      { name: "version", type: "string" },
      { name: "chainId", type: "uint256" },
      { name: "verifyingContract", type: "address" },
    ],
    Permit: [
      { name: "owner", type: "address" },
      { name: "spender", type: "address" },
      { name: "value", type: "uint256" },
      { name: "nonce", type: "uint256" },
      { name: "deadline", type: "uint256" },
    ],
  },
  primaryType: "Permit",
  domain: {
    name: "Aave Token",
    version: "1",
    chainId: chainId,
    verifyingContract: aaveTokenAddress,
  },
  message: {
    owner,
    spender,
    value,
    nonce,
    deadline,
  },
}

const signature = signTypedData_v4(
  Buffer.from(privateKey, "hex"),
  { data: permitParams }
)

const { v, r, s } = fromRpcSig(signature)

await aaveTokenContract.methods
    .permit({
      owner,
      spender,
      value,
      deadline,
      v,
      r,
      s
    })
    .send()
    .catch((e) => {
        throw Error(`Error permitting: ${e.message}`)
    })
```
{% endtab %}
{% endtabs %}

### \_nonces()

**`function _nonces(address owner) public`**

Returns the next valid nonce to submit when calling `permit()`

### event SnapshotDone

**`event SnapshotDone(address owner, uint128 oldValue, uint128 newValue)`**

An event emitted on every `transfer`, `mint` (with a valid `to` address), and `burn` (with a valid `from` address).

The snapshots are used for governance balance tracking.

| Parameter  | Type    | Description                                 |
| ---------- | ------- | ------------------------------------------- |
| `owner`    | address | The owner of the AAVE tokens                |
| `oldValue` | uint128 | The value before the operation was executed |
| `newValue` | uint128 | The value after the operation was executed. |

