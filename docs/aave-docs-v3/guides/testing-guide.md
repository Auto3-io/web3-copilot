# Testing Guide

* Test Markets
* Tenderly: Debugging from browser
* Tenderly Fork: Connect custom contracts to Aave Frontend

## Test Markets

The simplest way to interact with Aave V3 in a test environment is to connect your wallet and use the app with fauceted funds on a test network. All test markets can be accessed from the [app](https://app.aave.com) or from cloning/forking the [Aave frontend](https://github.com/aave/interface).

{% hint style="info" %}
To interact with test markets make sure you toggle the **Testnet mode** _on_. The testnet option is available on [app](https://app.aave.com) in top right ⚙️ drop-down-menu.
{% endhint %}

First, you’ll need to add the test network to your wallet. You can directly add networks to your browser wallet with [Chainlist](https://chainlist.org).

Next, you’ll need to faucet some base currency for the test network to pay gas for transactions. Here are links to available faucets (not operated or affiliated with Aave):

* Kovan: [Paradigm](https://faucet.paradigm.xyz), [Chainlink](https://faucets.chain.link), [Buni](https://faucet.buni.finance)
* Mumbai: [Polygon](https://faucet.polygon.technology), [Paradigm](https://faucet.paradigm.xyz)
* Fuji: [Avalanche](https://faucet.avax-test.network), [Paradigm](https://faucet.paradigm.xyz), [Kyte](https://faucet.kyte.one)
* Arbitrum Rinkeby: [Arbitrum](https://faucet.rinkeby.io)

Each testnet market has a custom set of assets which can be fauceted from the Aave faucet. To access the faucet interface: switch to the market which you want to test, be sure your wallet is connected to the correct network and *testnet mode* is on. The faucet link is available at bottom of the supply column in _Dashboard_ or you can manually update url to `https://app.aave.com/faucet/`.

Once you have test assets, you can supply, borrow, repay, withdraw, and test V3 features:

### E-Mode

E-Mode enables users to access a higher borrowing power when supplying and borrowing assets in the same category (stablecoins, ETH, etc.). E-Mode can be enabled and disabled from the Dashboard screen. Once in E-Mode, collateral and debt is limited to a single asset class and the LTV for supplying assets in this category is increased.

### Isolation Mode

One of the new features of V3 is isolation mode which allows the listing of assets with restricted borrowing capacity. Isolated assets are usually newly listed assets that you can only borrow up to a certain debt ceiling.

### Supply and Repay With Permit

To enable Pool spending of user assets in the supply and repay functions in V2, an approval transaction was required. In V3, assets which implement EIP 2612 can be approved for spending with a signature which does not incur any gas cost.

### Multi-Incentives

Each aToken or debtToken can support multiple incentives. After supplying or borrowing a supported asset, incentives can be viewed and claimed individually or all at once from the Dashboard.

## Tenderly

Tenderly is a tool for interacting and debugging smart contracts in a browser interface. It can be used to run simulations against live contracts or deploy/test contracts on a network fork with no coding experience required.

### Simulation

To run simulations you will need two things, a contract address and contract abi.

The contract addresses for each official and testnet market of the Aave Protocol can be found [here](https://docs.aave.com/developers/deployed-contracts/deployed-contracts).

The abi for each contract can obtained from a block explorer or compiling contract code directly.

From a block explorer (etherscan, polygonscan, etc.), if the contract source code is verified you can find the abi by clicking Contract → Read As Proxy → Click the implementation address → Toward the bottom of the page will be an abi that can be copied. Most Aave contracts are deployed as a governance upgradeable proxy which is why the Read As Proxy step is required.

To compile the abi from contract code, from the deployed contracts page, click the link to source code on GitHub and take note of the repo and branch name. You will need to clone the protocol contracts repo and checkout the branch corresponding to the market deployment. Then run `npm i` and `npm run compile` to compile the contracts and generate abis in the `artifacts` folder.

### Forks

A fork can be created from the Tenderly website which will allow you to deploy your own contracts to a fork of almost any EVM network.

### Connect To Aave UI

A Tenderly fork can also be created with simplified steps for connecting to the Aave frontend by cloning this [repo](https://github.com/sakulstra/tenderly-fork). Once cloned, you can input your Tenderly API credentials and wallet address into the .env file, then run the commands from the `README` to start a fork on a specified network.

With the output from running the start command you can add fork network to your browser wallet with the chainId and rpc URL provided, then paste the three commands into the browser console of an open tab of the Aave Frontend. Once you reload the page, a new market will be created with an f indicator.
