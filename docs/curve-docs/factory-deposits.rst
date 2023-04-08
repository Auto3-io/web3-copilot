.. _factory-deposits:

===================================
Metapool Factory: Deposit Contracts
===================================

Deposit contracts (also known as "zaps") allow users to add and remove liquidity from a pool using the pool's underlying tokens.

Deployment Addresses
====================

A single zap is used for all factory metapools targetting one base pool. The zaps are deployed to mainnet at the following addresses:

* 3pool: `0xA79828DF1850E8a3A3064576f380D90aECDD3359 <https://etherscan.io/address/0xa79828df1850e8a3a3064576f380d90aecdd3359>`_
* sBTC: `0x7AbDBAf29929e7F8621B757D2a7c04d78d633834  <https://etherscan.io/address/0x7abdbaf29929e7f8621b757d2a7c04d78d633834>`_


Calculating Expected Amounts
============================

.. py:function:: DepositZap.calc_withdraw_one_coin(_pool: address, _token_amount: uint256, i: int128) -> uint256: view

    Calculate the amount received when withdrawing and unwrapping in a single coin. Useful for setting ``_max_burn_amount`` when calling :func:`remove_liquidity_one_coin<DepositZap.remove_liquidity_one_coin>`.

    * ``_pool``: Address of the pool to deposit into.
    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal.
    * ``i``: Index value of the underlying coin to withdraw.

    Returns the expected amount of coin received.

.. py:function:: DepositZap.calc_token_amount(_pool: address, _amounts: uint256[4], _is_deposit: bool) -> uint256: view

    Calculate addition or reduction in token supply from a deposit or withdrawal.

    This calculation accounts for slippage, but not fees. It should be used as a basis for determining expected amounts when calling :func:`add_liquidity<DepositZap.add_liquidity>` or :func:`remove_liquidity_imbalance<DepositZap.remove_liquidity_imbalance>`, but should not be considered to be precise!

    * ``_pool``: Address of the pool to deposit into.
    * ``_amounts``: Amount of each underlying coin being deposited or withdrawn. Amounts correspond to the tokens at the same index locations within :func:`Factory.get_underlying_coins<Factory.get_underlying_coins>`.
    * ``_is_deposit``: set ``True`` for deposits, ``False`` for withdrawals.

    Returns the expected amount of LP tokens received.

Adding Liquidity
================

.. py:function:: DepositZap.add_liquidity(_pool: address, _deposit_amounts: uint256[4], _min_mint_amount: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Wraps underlying coins and deposit them into ``_pool``.

    * ``_pool``: Address of the pool to deposit into.
    * ``_deposit_amounts``: List of amounts of underlying coins to deposit. Amounts correspond to the tokens at the same index locations within :func:`Factory.get_underlying_coins<Factory.get_underlying_coins>`.
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit.
    * ``_receiver``: Optional address that receives the LP tokens. If not specified, they are sent to the caller.

    Returns the amount of LP tokens that were minted in the deposit.

        .. code-block:: python

            >>> zap = Contract('0x7AbDBAf29929e7F8621B757D2a7c04d78d633834')
            >>> pool = Contract('0xFD9f9784ac00432794c8D370d4910D2a3782324C')

            >>> amounts = [1e18, 1e18, 1e6, 1e6]
            >>> expected = zap.calc_token_amount(pool, amounts, True) * 0.99
            >>> zap.add_liquidity(pool, amounts, expected, {'from': alice})

Removing Liquidity
==================

.. py:function:: DepositZap.remove_liquidity(_pool: address, _burn_amount: uint256, _min_amounts: uint256[4], _receiver: address = msg.sender) -> uint256[4]: nonpayable

    Withdraw underlying coins from ``_pool``.

    Withdrawal amounts are based on current deposit ratios. Withdrawals using this method do not incur a fee.

    * ``_pool``: Address of the pool to withdraw from.
    * ``_burn_amount``: Quantity of LP tokens to burn in the withdrawal. Amounts correspond to the tokens at the same index locations within :func:`Factory.get_underlying_coins<Factory.get_underlying_coins>`.
    * ``_min_amounts``: Minimum amounts of underlying coins to receive.
    * ``_receiver``: Optional address that receives the withdrawn coins. If not specified, the coins are sent to the caller.

    Returns a list of the amounts of underlying coins that were withdrawn.

        .. code-block:: python

            >>> zap = Contract('0x7AbDBAf29929e7F8621B757D2a7c04d78d633834')
            >>> pool = Contract('0xFD9f9784ac00432794c8D370d4910D2a3782324C')

            >>> amount = pool.balanceOf(alice)
            >>> zap.remove_liquidity(pool, amount, 0, {'from': alice})

.. py:function:: DepositZap.remove_liquidity_one_coin(_pool: address, _burn_amount: uint256, i: int128, _min_amount: uint256, _receiver: address=msg.sender) -> uint256: nonpayable

    Withdraw from ``_pool`` in a single coin.

    * ``_pool``: Address of the pool to withdraw from.
    * ``_burn_amount``: Amount of LP tokens to burn in the withdrawal
    * ``i``: Index value of the coin to withdraw. Can be found using :func:`Factory.get_underlying_coins<Factory.get_underlying_coins>`.
    * ``_min_amount``: Minimum amount of underlying coin to receive
    * ``_receiver``: Optional address that receives the withdrawn coin. If not specified, the coin is sent to the caller.

    Returns the amount of the underlying coin received in the withdrawal.

        .. code-block:: python

            >>> zap = Contract('0x7AbDBAf29929e7F8621B757D2a7c04d78d633834')
            >>> pool = Contract('0xFD9f9784ac00432794c8D370d4910D2a3782324C')

            >>> amount = pool.balanceOf(alice)
            >>> expected = zap.calc_withdraw_one_coin(pool, amount, 2) * 1.01
            >>> zap.remove_liquidity_one_coin(pool, amount, expected, 2, {'from': alice})

.. py:function:: DepositZap.remove_liquidity_imbalance(_pool: address, _amounts: uint256[N_ALL_COINS], _max_burn_amount: uint256, _receiver: address=msg.sender) -> uint256: nonpayable

    Withdraw coins from ``_pool`` in an imbalanced amount.

    * ``_pool``: Address of the pool to withdraw from.
    * ``_amounts``: List of amounts of underlying coins to withdraw. Amounts correspond to the tokens at the same index locations within :func:`Factory.get_underlying_coins<Factory.get_underlying_coins>`.
    * ``_max_burn_amount``: Maximum number of LP token to burn in the withdrawal.
    * ``_receiver``: Optional address that receives the withdrawn coins. If not specified, the coins are sent to the caller.

    Returns the amount of the LP tokens burned in the withdrawal.

        .. code-block:: python

            >>> zap = Contract('0x7AbDBAf29929e7F8621B757D2a7c04d78d633834')
            >>> pool = Contract('0xFD9f9784ac00432794c8D370d4910D2a3782324C')

            >>> amounts = [1e18, 1e18, 1e6, 1e6]
            >>> expected = zap.calc_token_amount(pool, amounts, False) * 1.01
            >>> zap.remove_liquidity_imbalance(pool, amounts, expected, {'from': alice})

    .. note::

        The deposit contract must be approved to transfer ``_max_burn_amount`` LP tokens from the caller or the transaction will fail.
