.. _exchange-deposits:

============================================
Curve StableSwap Exchange: Deposit Contracts
============================================

Curve pools may rely on a different contract, called a *deposit zap* for the addition and removal of underlying coins. This is particularly useful for lending pools, which may only support the addition/removal of wrapped coins. Furthermore, deposit zaps are also useful for metapools, which do not support the addition/removal of base pool coins.

Lending Pool Deposits
=====================

While Curve lending pools support swaps in both the wrapped *and* underlying coins, not all lending pools allow liquidity providers to deposit or withdraw the underlying coin.

For example, the Compound Pool allows swaps between ``cDai`` and ``cUSDC`` (wrapped coins), as well as swaps between ``DAI`` and ``USDC`` (underlying coins). However, liquidity providers are not able to deposit ``DAI`` or ``USDC`` to the pool directly. The main reason for why this is not supported by all Curve lending pools lies in the `size limit of contracts <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-170.md>`_. Lending pools may differ in complexity and can end up being very close to the contract byte code size limit. In order to overcome this restriction, liquidity can be added and removed to and from a lending pool in the underlying coins via a different contract, called a *deposit zap*, tailored to lending pools.

For an overview of the Curve lending pool implementation, please refer to the :ref:`Lending Pool <exchange-pools-lending>` section.

The template source code for a lending pool deposit zap may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/y/DepositTemplateY.vy>`_.


.. note::
    Lending pool deposit zaps may differ in their API. Older pools do not implement the newer `API template <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/y/DepositTemplateY.vy>`_.


Deposit Zap API (OLD)
--------------------

Older Curve lending pool deposit zaps do not implement the `template API <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/y/DepositTemplateY.vy>`_. The deposit zaps which employ an older API are:

    * ``DepositBUSD``: `BUSD pool deposit zap <https://etherscan.io/address/0xb6c057591e073249f2d9d88ba59a46cfc9b59edb#code>`_
    * ``DepositCompound``: `Compound pool deposit zap <https://etherscan.io/address/0xeb21209ae4c2c9ff2a86aca31e123764a3b6bc06#code>`_
    * ``DepositPAX``: `PAX pool deposit zap <https://etherscan.io/address/0xa50ccc70b6a011cffddf45057e39679379187287#code>`_
    * ``DepositUSDT``: `USDT pool deposit zap <https://etherscan.io/address/0xac795d2c97e60df6a99ff1c814727302fd747a80#code>`_
    * ``DepositY``: `Y pool deposit zap <https://etherscan.io/address/0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3#readContract>`_

While not a lending pool, note that the following contract also implements the newer deposit zap API:

    * ``DepositSUSD``: `SUSD pool deposit zap <https://etherscan.io/address/0xfcba3e75865d2d561be8d220616520c171f12851#code>`_


Get Deposit Zap Information
***************************

.. note::
    Getters generated for public arrays changed between Vyper ``0.1.x`` and ``0.2.x`` to accept ``uint256`` instead of ``int128`` in order to handle the lookups. Older deposit zap contracts (v1) use ``vyper 0.1.x...``, while newer zaps (v2) use ``vyper 0.2.x...``.

The following Brownie console interaction examples are using the `Compound Pool Deposit Zap <https://etherscan.io/address/0xeb21209ae4c2c9ff2a86aca31e123764a3b6bc06>`_.

.. py:function:: DepositZap.curve() -> address: view

    Getter for the pool associated with this deposit contract.

    .. code-block:: python

        >>> zap.curve()
        '0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56'

.. py:function:: DepositZap.underlying_coins(i: int128) -> address: view

    Getter for the array of **underlying** coins within the associated pool.

    * ``i``: Index of the underlying coin for which to get the address

    .. code-block:: python

        >>> zap.underlying_coins(0)
        '0x6B175474E89094C44Da98b954EedeAC495271d0F'
        >>> zap.underlying_coins(1)
        '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'

.. py:function:: DepositZap.coins(i: int128) -> address: view

    Getter for the array of **wrapped** coins within the associated pool.

    * ``i``: Index of the coin for which to get the address

    .. code-block:: python

        >>> zap.coins(0)
        '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643'
        >>> zap.coins(1)
        '0x39AA39c021dfbaE8faC545936693aC917d5E7563'

.. py:function:: DepositZap.token() -> address: view

    Getter for the LP token of the associated pool.

    .. code-block:: python

        >>> zap.token()
        '0x845838DF265Dcd2c412A1Dc9e959c7d08537f8a2'


Adding/Removing Liquidity
*************************

.. py:function:: DepositZap.add_liquidity(uamounts: uint256[N_COINS], min_mint_amount: uint256)

    Wrap underlying coins and deposit them in the pool

    * ``uamounts``: List of amounts of underlying coins to deposit
    * ``min_mint_amount``: Minimum amount of LP token to mint from the deposit

.. py:function:: DepositZap.remove_liquidity(_amount: uint256, min_uamounts: uint256[N_COINS])

    Withdraw and unwrap coins from the pool.

    * ``_amount``: Quantity of LP tokens to burn in the withdrawal
    * ``min_uamounts``: Minimum amounts of underlying coins to receive

.. py:function:: DepositZap.remove_liquidity_imbalance(uamounts: uint256[N_COINS], max_burn_amount: uint256)

    Withdraw and unwrap coins from the pool in an imbalanced amount.

    * ``uamounts``: List of amounts of underlying coins to withdraw
    * ``max_burn_amount``: Maximum amount of LP token to burn in the withdrawal

.. py:function:: DepositZap.remove_liquidity_one_coin(_token_amount: uint256, i: int128, min_uamount: uint256, donate_dust: bool = False)

    Withdraw and unwrap a single coin from the pool

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw
    * ``min_uamount``: Minimum amount of underlying coin to receive

.. py:function:: DepositZap.calc_withdraw_one_coin(_token_amount: uint256, i: int128) -> uint256

    Calculate the amount received when withdrawing a single underlying coin.

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw

.. py:function:: DepositZap.withdraw_donated_dust()

    Donates any LP tokens of the associated pool held by this contract to the contract owner.


Deposit Zap API (NEW)
--------------------

Compared to the older deposit zaps, the newer zaps mainly optimize for gas efficiency. The API is only modified in part, specifically with regards to ``return`` values and variable naming.

Get Deposit Zap Information
***************************

.. py:function:: DepositZap.curve() -> address: view

    Getter for the pool associated with this deposit contract.

.. py:function:: DepositZap.underlying_coins(i: uint256) -> address: view

    Getter for the array of **underlying** coins within the associated pool.

    * ``i``: Index of the underlying coin for which to get the address

.. py:function:: DepositZap.coins(i: uint256) -> address: view

    Getter for the array of **wrapped** coins within the associated pool.

    * ``i``: Index of the coin for which to get the address

.. py:function:: DepositZap.lp_token() -> address: view

    Getter for the LP token of the associated pool.


Adding/Removing Liquidity
*************************

.. py:function:: DepositZap.add_liquidity(_underlying_amounts: uint256[N_COINS], _min_mint_amount: uint256) -> uint256

    Wrap underlying coins and deposit them in the pool

    * ``_underlying_amounts``: List of amounts of underlying coins to deposit
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit

    Returns the amount of LP token received in exchange for the deposited amounts.

.. py:function:: DepositZap.remove_liquidity(_amount: uint256, _min_underlying_amounts: uint256[N_COINS]) -> uint256[N_COINS]

    Withdraw and unwrap coins from the pool.

    * ``_amount``: Quantity of LP tokens to burn in the withdrawal
    * ``_min_underlying_amounts``: Minimum amounts of underlying coins to receive

    Returns list of amounts of underlying coins that were withdrawn.


.. py:function:: DepositZap.remove_liquidity_imbalance(_underlying_amounts: uint256[N_COINS], _max_burn_amount: uint256) -> uint256[N_COINS]

    Withdraw and unwrap coins from the pool in an imbalanced amount. Amounts in `_underlying_amounts` correspond to withdrawn amounts before any fees charge for unwrapping.

    * ``_underlying_amounts``: List of amounts of underlying coins to withdraw
    * ``_max_burn_amount``: Maximum amount of LP token to burn in the withdrawal

    Returns list of amounts of underlying coins that were withdrawn.


.. py:function:: DepositZap.remove_liquidity_one_coin(_amount: uint256, i: int128, _min_underlying_amount: uint256) -> uint256

    Withdraw and unwrap a single coin from the pool

    * ``_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw
    * ``_min_underlying_amount``: Minimum amount of underlying coin to receive

    Returns amount of underlying coin received.


Metapool Deposits
=================

While Curve metapools support swaps between base pool coins, the base pool LP token and metapool coins, they do not allow liquidity providers to deposit and/or withdraw base pool coins.

For example, the GUSD metapool is a pool consisting of ``GUSD`` and ``3CRV`` (the LP token of the 3Pool) and allows for swaps between ``GUSD``, ``DAI``, ``USDC``, ``USDT`` and ``3CRV``. However, liquidity providers are not able to deposit ``DAI``, ``USDC`` or ``USDT`` to the pool directly. The main reason why this is not possible lies in the maximum byte code size of contracts. Metapools are complex and can therefore end up being very close to the contract byte code size limit. In order to overcome this restriction, liquidity can be added and removed to and from a metapool in the base pool's coins through a metapool deposit zap.

For an overview of the Curve metapool implementation, please refer to the :ref:`Metapool <exchange-pools-meta>` section.

The template source code for a metapool deposit "zap" may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/meta/DepositTemplateMeta.vy>`_.

A list of all deployed metapool deposit zaps can be found :ref:`here <addresses-metapools>`.

.. note::
    Metapool deposit zaps contain the following private and hardcoded constants:

    * ``N_COINS``: Number of coins in the metapool (excluding base pool coins)
    * ``BASE_N_COINS``: Number of coins in the base pool
    * ``N_ALL_COINS``: All coins in the metapool, excluding the base pool LP token (``N_COINS + BASE_N_COINS - 1``)


Get Deposit Zap Information
---------------------------

.. py:function:: DepositZap.pool() -> address: view

    Getter for the metapool associated with this deposit contract.

.. py:function:: DepositZap.base_pool() -> address: view

    Getter for the base pool of the metapool associated with this deposit contract.

.. py:function:: DepositZap.base_coins(i: uint256) -> address: view

    Getter for the array of the coins of the metapool's base pool.

    * ``i``: Index of the underlying coin for which to get the address

.. py:function:: DepositZap.coins(i: uint256) -> address: view

    Getter for the array of metapool's coins.

    * ``i``: Index of the coin for which to get the address

.. py:function:: DepositZap.token() -> address: view

    Getter for the LP token of the associated metapool.


Adding/Removing Liquidity
-------------------------

.. note::
    For methods taking the index argument ``i``, a number in the range from ``0`` to ``N_ALL_COINS - 1`` is valid. This refers to all coins apart from the base pool LP token.

.. py:function:: DepositZap.add_liquidity(_amounts: uint256[N_ALL_COINS], _min_mint_amount: uint256) -> uint256

    Wrap underlying coins and deposit them in the pool.

    * ``_amounts``: List of amounts of underlying coins to deposit
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit

    Returns the amount of LP token received in exchange for depositing.

.. py:function:: DepositZap.remove_liquidity(_amount: uint256, _min_amounts: uint256[N_ALL_COINS]) -> uint256[N_ALL_COINS]

    Withdraw and unwrap coins from the pool.

    * ``_amount``: Quantity of LP tokens to burn in the withdrawal
    * ``_min_amounts``: Minimum amounts of underlying coins to receive

    Returns a list of amounts of underlying coins that were withdrawn.

.. py:function:: DepositZap.remove_liquidity_one_coin(_token_amount: uint256, i: int128, _min_amount: uint256) -> uint256

    Withdraw and unwrap a single coin from the metapool.

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw
    * ``_min_amount``: Minimum amount of underlying coin to receive

    Returns the amount of the underlying coin received.

.. py:function:: DepositZap.remove_liquidity_imbalance(_amounts: uint256[N_ALL_COINS], _max_burn_amount: uint256) -> uint256

    Withdraw coins from the pool in an imbalanced amount

    * ``_amounts``: List of amounts of underlying coins to withdraw
    * ``_max_burn_amount``: Maximum amount of LP token to burn in the withdrawal

    Returns the actual amount of the LP token burned in the withdrawal.

.. py:function:: DepositZap.calc_withdraw_one_coin(_token_amount: uint256, i: int128) -> uint256

    Calculate the amount received when withdrawing and unwrapping a single coin

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw (``i`` should be in the range from ``0`` to ``N_ALL_COINS - 1``, where the LP token of the base pool is removed).

    Returns the amount of coin ``i`` received.

.. py:function:: DepositZap.calc_token_amount(_amounts: uint256[N_ALL_COINS], _is_deposit: bool) -> uint256

    Calculate addition or reduction in token supply from a deposit or withdrawal.

    * ``_amounts``: Amount of each underlying coin being deposited
    * ``_is_deposit``: Set True for deposits, False for withdrawals

    Returns the expected amount of LP tokens received.

