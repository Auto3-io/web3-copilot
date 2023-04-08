.. _exchange-pools:

=======================
Curve StableSwap: Pools
=======================

A Curve pool is a smart contract that implements the StableSwap invariant and thereby allows for the exchange of two or more tokens.

More broadly, Curve pools can be split into three categories:

* ``Plain pools``: a pool where two or more stablecoins are paired against one another.
* ``Lending pools``: a pool where two or more *wrapped* tokens (e.g., ``cDAI``) are paired against one another, while the underlying is lent out on some other protocol.
* ``Metapools``: a pool where a stablecoin is paired against the LP token from another pool.

Source code for Curve pools may be viewed on `GitHub <https://github.com/curvefi/curve-contract/tree/master/contracts>`_.

.. warning::
    The API for plain, lending and metapools applies to all pools that are implemented based on `pool templates <https://github.com/curvefi/curve-contract/tree/master/contracts/pool-templates>`_. When interacting with older Curve pools, there may be differences in terms of visibility, gas efficiency and/or variable naming. Furthermore, note that older contracts use ``vyper 0.1.x...`` and that the getters generated for public arrays changed between ``0.1.x`` and ``0.2.x`` to accept ``uint256`` instead of ``int128`` in order to handle the lookups.


    Please **do not** assume for a Curve pool to implement the API outlined in this section but verify this before interacting with a pool contract.

For information on code style please refer to the official :ref:`style guide <guide-code-style>`.


.. _exchange-pools-plain:

Plain Pools
===========

The simplest Curve pool is a plain pool, which is an implementation of the StableSwap invariant for two or more tokens. The key characteristic of a plain pool is that the pool contract holds **all** deposited assets at all times.

An example of a Curve plain pool is `3Pool <https://github.com/curvefi/curve-contract/tree/master/contracts/pools/3pool>`_, which contains the tokens ``DAI``, ``USDC`` and ``USDT``.

.. note::
    The API of plain pools is also implemented by lending and metapools.

The following Brownie console interaction examples are using `EURS Pool <https://etherscan.io/address/0x0Ce6a5fF5217e38315f87032CF90686C96627CAA>`_. The template source code for plain pools may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/base/SwapTemplateBase.vy>`_.

.. note::
    Every pool has the constant private attribute ``N_COINS``, which is the number of coins in the pool. This is referred to by several pool methods in the API.

Getting Pool Info
-----------------

.. py:function:: StableSwap.coins(i: uint256) -> address: view

    Getter for the array of swappable coins within the pool.

    .. code-block:: python

        >>> pool.coins(0)
        '0xdB25f211AB05b1c97D595516F45794528a807ad8'

.. py:function:: StableSwap.balances(i: uint256) -> uint256: view

    Getter for the pool balances array.

    .. code-block:: python

        >>> pool.balances(0)
        2918187395

.. py:function:: StableSwap.owner() -> address: view

    Getter for the admin/owner of the pool.

    .. code-block:: python

        >>> pool.owner()
        '0xeCb456EA5365865EbAb8a2661B0c503410e9B347'

.. py:function:: StableSwap.lp_token() -> address: view

    Getter for the :ref:`LP token <exchange-lp-tokens>` of the pool.

    .. code-block:: python

        >>> pool.lp_token()
        '0x194eBd173F6cDacE046C53eACcE9B953F28411d1'

    .. note::
        In older Curve pools ``lp_token`` may **not** be ``public`` and thus not visible.

.. py:function:: StableSwap.A() -> uint256: view

    The :ref:`amplification coefficient <exchange-pools-A>` for the pool.

    .. code-block:: python

        >>> pool.A()
        100

.. py:function:: StableSwap.A_precise() -> uint256: view

    The :ref:`amplification coefficient <exchange-pools-A>` for the pool not scaled by ``A_PRECISION`` (``100``).

    .. code-block:: python

        >>> pool.A_precise()
        10000

.. py:function:: StableSwap.get_virtual_price() -> uint256: view

    The current price of the pool LP token relative to the underlying pool assets. Given as an integer with 1e18 precision.

    .. code-block:: python

        >>> pool.get_virtual_price()
        1001692838188850782

.. py:function:: StableSwap.fee() -> uint256: view

    The pool swap fee, as an integer with 1e10 precision.

    .. code-block:: python

        >>> pool.fee()
        4000000

.. py:function:: StableSwap.admin_fee() -> uint256: view

    The percentage of the swap fee that is taken as an admin fee, as an integer with with 1e10 precision.

    Admin fee is set at 50% (``5000000000``) and is paid out to veCRV holders (see :ref:`Fee Collection and Distribution <dao-fees>`).

    .. code-block:: python

        >>> pool.admin_fee()
        5000000000


Making Exchanges
----------------

.. py:function:: StableSwap.get_dy(i: int128, j: int128, _dx: uint256) -> uint256: view

    Get the amount of coin ``j`` one would receive for swapping ``_dx`` of coin ``i``.

    .. code-block:: python

        >>> pool.get_dy(0, 1, 100)
        996307731416690125

    *Note*: In the ``EURS Pool``, the decimals for ``coins(0)`` and ``coins(1)`` are 2 and 18, respectively.

.. py:function:: StableSwap.exchange(i: int128, j: int128, _dx: uint256, _min_dy: uint256) -> uint256

    Perform an exchange between two coins.

    * ``i``: Index value for the coin to send
    * ``j``: Index value of the coin to receive
    * ``_dx``: Amount of ``i`` being exchanged
    * ``_min_dy``: Minimum amount of ``j`` to receive

    Returns the actual amount of coin ``j`` received. Index values can be found via the ``coins`` public getter method.

    .. code-block:: python

        >>> expected = pool.get_dy(0, 1, 10**2) * 0.99
        >>> pool.exchange(0, 1, 10**2, expected, {"from": alice})


.. _liquidity-plain-pools:

Adding/Removing Liquidity
-------------------------

.. py:function:: StableSwap.calc_token_amount(_amounts: uint256[N_COINS], _is_deposit: bool) -> uint256: view

Calculate addition or reduction in token supply from a deposit or withdrawal.

* ``_amounts``: Amount of each coin being deposited
* ``_is_deposit``: Set True for deposits, False for withdrawals

Returns the expected amount of LP tokens received. This calculation accounts for slippage, but not fees.

.. code-block:: python

    >>> pool.calc_token_amount([10**2, 10**18], True)
    1996887509167925969


.. py:function:: StableSwap.add_liquidity(_amounts: uint256[N_COINS], _min_mint_amount: uint256) -> uint256

    Deposit coins into the pool.

    * ``_amounts``: List of amounts of coins to deposit
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit

    Returns the amount of LP tokens received in exchange for the deposited tokens.


.. py:function:: StableSwap.remove_liquidity(_amount: uint256, _min_amounts: uint256[N_COINS]) -> uint256[N_COINS]

    Withdraw coins from the pool.

    * ``_amount``: Quantity of LP tokens to burn in the withdrawal
    * ``_min_amounts``: Minimum amounts of underlying coins to receive

    Returns a list of the amounts for each coin that was withdrawn.

.. py:function:: StableSwap.remove_liquidity_imbalance(_amounts: uint256[N_COINS], _max_burn_amount: uint256) -> uint256

    Withdraw coins from the pool in an imbalanced amount.

    * ``_amounts``: List of amounts of underlying coins to withdraw
    * ``_max_burn_amount``: Maximum amount of LP token to burn in the withdrawal

    Returns actual amount of the LP tokens burned in the withdrawal.

.. py:function:: StableSwap.calc_withdraw_one_coin(_token_amount: uint256, i: int128) -> uint256

    Calculate the amount received when withdrawing a single coin.

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw

.. py:function:: StableSwap.remove_liquidity_one_coin(_token_amount: uint256, i: int128, _min_amount: uint256) -> uint256

    Withdraw a single coin from the pool.

    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw
    * ``_min_amount``: Minimum amount of coin to receive

    Returns the amount of coin ``i`` received.


.. _exchange-pools-lending:

Lending Pools
=============

Curve pools may contain lending functionality, whereby the underlying tokens are lent out on other protocols (e.g., Compound or Yearn). Hence, the main difference to a plain pool is that a lending pool does **not** hold the underlying token itself, but a **wrapped** representation of it.

Currently, Curve supports the following lending pools:

    * ``aave``: `Aave pool <https://www.curve.fi/aave>`_, with lending on `Aave <https://www.aave.com/>`_
    * ``busd``: `BUSD pool <https://www.curve.fi/busd>`_, with lending on `yearn.finance <https://yearn.finance/>`_
    * ``compound``: `Compound pool <https://www.curve.fi/compound>`_, with lending on `Compound <https://compound.finance/>`_
    * ``ib``: `Iron Bank pool <https://www.curve.fi/ib>`_, with lending on `Cream <https://v1.yearn.finance/lending>`_
    * ``pax``: `PAX pool <https://www.curve.fi/pax>`_, with lending on `yearn.finance <https://yearn.finance/>`_
    * ``usdt``: `USDT pool <https://www.curve.fi/usdt>`_, with lending on `Compound <https://compound.finance/>`_
    * ``y``: `Y pool <https://www.curve.fi/y>`_, with lending on `yearn.finance <https://yearn.finance/>`_

An example of a Curve lending pool is `Compound Pool <https://github.com/curvefi/curve-contract/tree/master/contracts/pools/compound>`_, which contains the wrapped tokens ``cDAI`` and ``cUSDC``, while the underlying tokens ``DAI`` and ``USDC`` are lent out on Compound. Liquidity providers of the Compound Pool therefore receive interest generated on Compound in addition to fees from token swaps in the pool.

Implementation of lending pools may differ with respect to how wrapped tokens accrue interest. There are two main types of wrapped tokens that are used by lending pools:

    * ``cToken-style tokens``: These are tokens, such as interest-bearing cTokens on Compound (e.g., ``cDAI``) or on yTokens on Yearn, where interest accrues as the rate of the token increases.
    * ``aToken-style tokens``: These are tokens, such as aTokens on AAVE (e.g., ``aDAI``), where interest accrues as the balance of the token increases.

The template source code for lending pools may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/y/SwapTemplateY.vy>`_.


.. note::
    Lending pools also implement the API from :ref:`plain pools<exchange-pools-plain>`.

Getting Pool Info
-----------------

.. py:function:: StableSwap.underlying_coins(i: uint256) -> address: view

    Getter for the array of **underlying** coins within the pool.

    .. code-block:: python

        >>> lending_pool.coins(0)
        '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643'
        >>> lending_pool.coins(1)
        '0x39AA39c021dfbaE8faC545936693aC917d5E7563'


Making Exchanges
----------------

Like plain pools, lending pools have the ``exchange`` method. However, in the case of lending pools, calling ``exchange`` performs a swap between two **wrapped** tokens in the pool.

For example, calling ``exchange`` on the Compound Pool, would result in a swap between the wrapped tokens ``cDAI`` and ``cUSDC``.

.. py:function:: StableSwap.exchange_underlying(i: int128, j: int128, dx: uint256, min_dy: uint256) -> uint256

    Perform an exchange between two **underlying** tokens. Index values can be found via the ``underlying_coins`` public getter method.

    * ``i``: Index value for the underlying coin to send
    * ``j``: Index value of the underlying coin to receive
    * ``_dx``: Amount of `i` being exchanged
    * ``_min_dy``: Minimum amount of `j` to receive

    Returns the actual amount of coin ``j`` received.

.. note::
    Older Curve lending pools may not implement the same signature for ``exchange_underlying``. For instance, `Compound pool <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/compound/StableSwapCompound.vy#L474>`_ does not return anything for ``exchange_underlying`` and therefore costs more in terms of gas.

Adding/Removing Liquidity
-------------------------

The function signatures for adding and removing liquidity to a lending pool are *mostly* the same as for a :ref:`plain pool <liquidity-plain-pools>`. However, for lending pools, liquidity is added and removed in the **wrapped** token, not the underlying.

In order to be able to add and remove liquidity in the underlying token (e.g., remove DAI from Compound Pool instead of cDAI) there exists a ``Deposit<POOL>.vy`` contract (e.g., (`DepositCompound.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/compound/DepositCompound.vy>`_).

.. warning::
    Older Curve lending pools (e.g., Compound Pool) **do not** implement all plain pool methods for :ref:`adding and removing liquidity <liquidity-plain-pools>`. For instance, ``remove_liquidity_one_coin`` is not implemented by Compound Pool).

Some newer pools (e.g., `IB <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/ib/StableSwapIB.vy>`_) have a modified signature for ``add_liquidity`` and allow the caller to specify whether the deposited liquidity is in the wrapped *or* underlying token.

.. py:function:: StableSwap.add_liquidity(_amounts: uint256[N_COINS], _min_mint_amount: uint256, _use_underlying: bool = False) -> uint256

    Deposit coins into the pool.

    * ``_amounts``: List of amounts of coins to deposit
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit
    * ``_use_underlying`` If ``True``, deposit underlying assets instead of wrapped assets.

    Returns amount of LP tokens received in exchange for the deposited tokens.



.. _exchange-pools-meta:

Metapools
=========

A metapool is a pool where a stablecoin is paired against the LP token from another pool, a so-called *base pool*.

For example, a liquidity provider may deposit ``DAI`` into `3Pool <https://etherscan.io/address/0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7#code>`_ and in exchange receive the pool's LP token ``3CRV``. The ``3CRV`` LP token may then be deposited into the `GUSD metapool <https://etherscan.io/address/0x4f062658EaAF2C1ccf8C8e36D6824CDf41167956>`_, which contains the coins ``GUSD`` and ``3CRV``, in exchange for the metapool's LP token ``gusd3CRV``. The obtained LP token may then be staked in the metapool's liquidity gauge for ``CRV`` rewards.

Metapools provide an opportunity for the base pool liquidity providers to earn additional trading fees by depositing their LP tokens into the metapool. Note that the ``CRV`` rewards received for staking LP tokens into the pool's liquidity gauge may differ for the base pool's liquidity gauge and the metapool's liquidity gauge. For details on liquidity gauges and protocol rewards, please refer to :ref:`Liquidity Gauges and Minting CRV <dao-gauges>`.

.. note::
    Metapools also implement the API from :ref:`plain pools<exchange-pools-plain>`.

Getting Pool Information
------------------------

.. py:function:: StableSwap.base_coins(i: uint256) -> address: view

Get the coins of the base pool.

    .. code-block:: python

        >>> metapool.base_coins(0)
        '0x6B175474E89094C44Da98b954EedeAC495271d0F'
        >>> metapool.base_coins(1)
        '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
        >>> metapool.base_coins(2)
        '0xdAC17F958D2ee523a2206206994597C13D831ec7'


.. py:function:: StableSwap.coins(i: uint256) -> address: view

    Get the coins of the metapool.

    .. code-block:: python

        >>> metapool.coins(0)
        '0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd'
        >>> metapool.coins(1)
        '0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490'

    In this console example, ``coins(0)`` is the metapool's coin (``GUSD``) and ``coins(1)`` is the LP token of the base pool (``3CRV``).


.. py:function:: StableSwap.base_pool() -> address: view

    Get the address of the base pool.

    .. code-block:: python

        >>> metapool.base_pool()
        '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'


.. py:function:: StableSwap.base_virtual_price() -> uint256: view

    Get the current price of the base pool LP token relative to the underlying base pool assets.

    Note that the base pool's virtual price is only fetched from the base pool *if* the cached price has expired. A fetched based pool virtual price is cached for 10 minutes (``BASE_CACHE_EXPIRES: constant(int128) = 10 * 60``).


    .. code-block:: python

        >>> metapool.base_virtual_price()
        1014750545929625438

.. py:function:: StableSwap.base_cache_update() -> uint256: view

    Get the timestamp at which the base pool virtual price was last cached.

    .. code-block:: python

        >>> metapool.base_cache_updated()
        1616583340



Making Exchanges
----------------

Similar to lending pools, on metapools exchanges can be made either between the coins the metapool actually holds (another pool's LP token and some other coin) *or* between the metapool's underlying coins. In the context of a metapool, **underlying** coins refers to the metapool's coin and any of the base pool's coins. The base pool's LP token is **not** included as an underlying coin.

For example, the GUSD metapool would have the following:

    * Coins: ``GUSD``, ``3CRV`` (3Pool LP)
    * Underlying coins: ``GUSD``, ``DAI``, ``USDC``, ``USDT``

.. note::
    While metapools contain public getters for ``coins`` and ``base_coins``, there exists **no** getter for obtaining a list of all underlying coins.

.. py:function:: StableSwap.exchange(i: int128, j: int128, _dx: uint256, _min_dy: uint256) -> uint256

    Perform an exchange between two (non-underlying) coins in the metapool. Index values can be found via the ``coins`` public getter method.

    * ``i``: Index value for the coin to send
    * ``j``: Index valie of the coin to receive
    * ``_dx``: Amount of ``i`` being exchanged
    * ``_min_dy``: Minimum amount of ``j`` to receive

    Returns the actual amount of coin ``j`` received.


.. py:function:: StableSwap.exchange_underlying(i: int128, j: int128, _dx: uint256, _min_dy: uint256) -> uint256

    Perform an exchange between two underlying coins. Index values are the ``coins`` followed by the ``base_coins``, where the base pool LP token is **not** included as a value.

    * ``i``: Index value for the underlying coin to send
    * ``j``: Index valie of the underlying coin to recieve
    * ``_dx``: Amount of ``i`` being exchanged
    * ``_min_dy``: Minimum amount of underlying coin ``j`` to receive

    Returns the actual amount of underlying coin ``j`` received.



The template source code for metapools may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/pool-templates/meta/SwapTemplateMeta.vy>`_.


Admin Pool Settings
===================

The following are methods that may only be called by the pool admin (``owner``).

Additionally, some admin methods require a two-phase transaction process, whereby changes are committed in a first transaction and after a forced delay applied via a second transaction. The minimum delay after which a committed action can be applied is given by the constant pool attribute ``admin_actions_delay``, which is set to 3 days.

Pool Ownership
--------------

.. py:function:: StableSwap.commit_transfer_ownership(_owner: address)

    Initiate an ownership transfer of pool to ``_owner``.

    Callable only by the ownership admin. The ownership can not be transferred before ``transfer_ownership_deadline``, which is the timestamp of the current block delayed by ``admin_actions_delay``.

.. py:function:: StableSwap.apply_transfer_ownership()

    Transfers ownership of the pool from current owner to the owner previously set via ``commit_transfer_ownership``.

    .. warning::
        Pool ownership can only be transferred once.


.. py:function:: StableSwap.revert_transfer_ownership()

    Reverts any previously committed transfer of ownership. This method resets the ``transfer_ownership_deadline`` to ``0``.

.. _exchange-pools-A:

Amplification Coefficient
-------------------------

The amplification co-efficient (“A”) determines a pool’s tolerance for imbalance between the assets within it. A higher value means that trades will incur slippage sooner as the assets within the pool become imbalanced.

.. note::
     Within the pools, ``A`` is in fact implemented as ``1 / A`` and therefore a higher value implies that the pool will be **more** tolerant to slippage when imbalanced.

The appropriate value for A is dependent upon the type of coin being used within the pool.

It is possible to modify the amplification coefficient for a pool after it has been deployed. However, it requires a vote within the Curve DAO and must reach a 15% quorum.

.. py:function:: StableSwap.ramp_A(_future_A: uint256, _future_time: uint256)

    Ramp ``A`` up or down by setting a new ``A`` to take effect at a future point in time.

    * ``_future_A``: New future value of ``A``
    * ``_future_time``: Timestamp at which new ``A`` should take effect

.. py:function:: StableSwap.stop_ramp_A()

    Stop ramping ``A`` up or down and sets ``A`` to current ``A``.


Trade Fees
----------

Curve pools charge fees on token swaps, where the fee may differ between pools. An admin fee is charged on the pool fee. For an overview of how fees are distributed, please refer to :ref:`Fee Collection and Distribution <dao-fees>`.

.. py:function:: StableSwap.commit_new_fee(_new_fee: uint256, _new_admin_fee: uint256)

    Commit new pool and admin fees for the pool. These fees do not take immediate effect.

    * ``_new_fee``: New pool fee
    * ``_new_admin_fee``: New admin fee (expressed as a percentage of the pool fee)

.. note::
    Both the pool ``fee`` and the ``admin_fee`` are capped by the constants ``MAX_FEE`` and ``MAX_ADMIN_FEE``, respectively. By default ``MAX_FEE`` is set at 50% and ``MAX_ADMIN_FEE`` at 100% (which is charged on the ``MAX_FEE`` amount).

.. py:function:: StableSwap.apply_new_fee()

    Apply the previously committed new pool and admin fees for the pool.

    .. note::
        Unlike ownership transfers, pool and admin fees may be set more than once.

.. py:function:: StableSwap.revert_new_parameters()

    Resets any previously committed new fees.

.. py:function:: StableSwap.admin_balances(i: uint256) -> uint256

    Get the admin balance for a single coin in the pool.

    * ``i``: Index of the coin to get admin balance for

    Returns the admin balance for coin ``i``.

.. py:function:: StableSwap.withdraw_admin_fees()

    Withdraws and transfers admin fees of the pool to the pool owner.

.. py:function:: StableSwap.donate_admin_fees()

    Donate all admin fees to the pool's liquidity providers.

    .. note::
        Older Curve pools do not implement this method.

Kill a Pool
-----------

.. py:function:: StableSwap.kill_me()

    Pause a pool by setting the ``is_killed`` boolean flag to ``True``.

    This disables the following pool functionality:
    * ``add_liquidity``
    * ``exchange``
    * ``remove_liquidity_imbalance``
    * ``remove_liquidity_one_coin``

    Hence, when paused, it is only possible for existing LPs to remove liquidity via ``remove_liquidity``.

    .. note::
        Pools can only be killed within the first 30 days after deployment.

.. py:function:: StableSwap.unkill_me()

    Unpause a pool that was previously paused, re-enabling exchanges.
