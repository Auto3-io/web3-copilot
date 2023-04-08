.. _factory-pools:

=======================
Metapool Factory: Pools
=======================

Factory pools are permissionless metapools that can be deployed by anyone. New pools are deployed using :func:`Factory.deploy_metapool<Factory.deploy_metapool>`.

Source code for the implementation contracts may be viewed on `Github <https://github.com/iamdefinitelyahuman/curve-factory/blob/master/contracts>`_.

Implementation Contracts
========================

Each pool deployed by the factory is a thin proxy contract created with Vyper's ``create_forwarder_to``. The implementation contract targetted by the proxy is determined based on the base pool used. This is the same technique that was used to create pools in Uniswap V1.

The implementation contracts used for pools are deployed to the mainnet at the following addresses:

* 3pool: `0x5F890841f657d90E081bAbdB532A05996Af79Fe6 <https://etherscan.io/address/0x5F890841f657d90E081bAbdB532A05996Af79Fe6>`_
* sBTC: `0x2f956eee002b0debd468cf2e0490d1aec65e027f <https://etherscan.io/address/0x2f956eee002b0debd468cf2e0490d1aec65e027f>`_

When interacting with a factory pool you should use the ABI at the corresponding implementation address:

    .. code-block:: python

        >>> implementation = Contract("0x5F890841f657d90E081bAbdB532A05996Af79Fe6")
        >>> abi = implementation.abi
        >>> pool = Contract.from_abi("ESD Pool", "0xFD9f9784ac00432794c8D370d4910D2a3782324C", abi)

Getting Pool Info
=================

.. py:function:: StableSwap.coins(i: uint256) -> address: view

    Getter for the array of swappable coins within the pool. The last coin will always be the LP token of the base pool.

        .. code-block:: python

            >>> pool.coins(0)
            '0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723'

.. py:function:: StableSwap.balances(i: uint256) -> uint256: view

    Getter for the pool balances array.

        .. code-block:: python

            >>> pool.balances(0)
            4898975297808622168122

.. py:function:: StableSwap.A() -> uint256: view

    The :ref:`amplification coefficient <factory-deployer-A>` for the pool.

        .. code-block:: python

            >>> pool.A()
            10

.. py:function:: StableSwap.get_virtual_price() -> uint256: view

    The current price of the pool LP token relative to the underlying pool assets. Given as an integer with 1e18 precision.

        .. code-block:: python

            >>> pool.get_virtual_price()
            1006391979770742306

.. py:function:: StableSwap.fee() -> uint256: view

    The pool swap fee, as an integer with 1e10 precision.

        .. code-block:: python

            >>> pool.fee()
            4000000

.. py:function:: StableSwap.admin_fee() -> uint256: view

    The percentage of the swap fee that is taken as an admin fee, as an integer with with 1e10 precision.

    For factory pools this is hardcoded at 50% (``5000000000``).

    .. code-block:: python

            >>> pool.admin_fee()
            5000000000

Making Exchanges
================

.. py:function:: StableSwap.get_dy(i: int128, j: int128, dx: uint256) -> uint256: view

    Get the amount received ("dy") when performing a swap between two assets within the pool.

    Index values can be found using the :func:`coins<StableSwap.coins>` public getter method, or :func:`get_coins<Factory.get_coins>` within the factory contract.

    * ``i``: Index value of the coin to send.
    * ``j``: Index value of the coin to receive.
    * ``dx``: The amount of ``i`` being exchanged.

    Returns the amount of ``j`` received.

        .. code-block:: python

            >>> pool.get_dy(0, 1, 10**18)
            460306318211728896


.. py:function:: StableSwap.get_dy_underlying(i: int128, j: int128, dx: uint256) -> uint256: view

    Get the amount received ("dy") when swapping between two underlying assets within the pool.

    Index values can be found using :func:`get_underlying_coins<Factory.get_underlying_coins>` within the factory contract.

    * ``i``: Index value of the token to send.
    * ``j``: Index value of the token to receive.
    * ``dx``: The amount of ``i`` being exchanged.

    Returns the amount of ``j`` received.

        .. code-block:: python

            >>> pool.get_dy_underlying(0, 1, 10**18)
            463415003137589177

.. py:function:: StableSwap.exchange(i: int128, j: int128, dx: uint256, min_dy: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Performs an exchange between two tokens.

    Index values can be found using the :func:`coins<StableSwap.coins>` public getter method, or :func:`get_coins<Factory.get_coins>` within the factory contract.

    * ``i``: Index value of the token to send.
    * ``j``: Index value of the token to receive.
    * ``dx``: The amount of ``i`` being exchanged.
    * ``min_dy``: The minimum amount of ``j`` to receive. If the swap would result in less, the transaction will revert.
    * ``_receiver``: An optional address that will receive ``j``. If not given, defaults to the caller.

    Returns the amount of ``j`` received in the exchange.

        .. code-block:: python

            >>> expected = pool.get_dy(0, 1, 10**18) * 0.99
            >>> pool.exchange(0, 1, 10**18, expected, {'from': alice})

.. py:function:: StableSwap.exchange_underlying(i: int128, j: int128, dx: uint256, min_dy: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Perform an exchange between two underlying coins.

    Index values can be found using :func:`get_underlying_coins<Factory.get_underlying_coins>` within the factory contract.

    * ``i``: Index value of the underlying token to send.
    * ``j``: Index value of the underlying token to receive.
    * ``dx``: The amount of ``i`` being exchanged.
    * ``min_dy``: The minimum amount of ``j`` to receive. If the swap would result in less, the transaction will revert.
    * ``_receiver``: An optional address that will receive ``j``. If not given, defaults to the caller.

    Returns the amount of ``j`` received in the exchange.

        .. code-block:: python

            >>> expected = pool.get_dy_underlying(0, 3, 10**18) * 0.99
            >>> pool.exchange_underlying(0, 3, 10**18, expected, {'from': alice})

Adding and Removing Liquidity
=============================

Note that if you wish to add or remove liqudity using the underlying assets within the base pool, you must use a :ref:`depositor contract <factory-deposits>`.

.. py:function:: StableSwap.calc_token_amount(_amounts: uint256[2], _is_deposit: bool) -> uint256: view

    Estimate the amount of LP tokens minted or burned based on a deposit or withdrawal.

    This calculation accounts for slippage, but not fees. It should be used as a basis for determining expected amounts when calling :func:`add_liquidity<StableSwap.add_liquidity>` or :func:`remove_liquidity_imbalance<StableSwap.remove_liquidity_imbalance>`, but should not be considered to be precise!

    * ``_amounts``: Amount of each coin being deposited. Amounts correspond to the tokens at the same index locations within :func:`coins<StableSwap.coins>`.
    * ``_is_deposit``: set ``True`` for deposits, ``False`` for withdrawals.

    Returns the expected amount of LP tokens minted or burned.

.. py:function:: StableSwap.calc_withdraw_one_coin(_burn_amount: uint256, i: int128) -> uint256: view

    Calculate the amount received when withdrawing and unwrapping in a single coin. Useful for setting ``_max_burn_amount`` when calling :func:`remove_liquidity_one_coin<StableSwap.remove_liquidity_one_coin>`.

    * ``_pool``: Address of the pool to deposit into.
    * ``_token_amount``: Amount of LP tokens to burn in the withdrawal.
    * ``i``: Index value of the underlying coin to withdraw. Can be found using the :func:`coins<StableSwap.coins>` getter method.

    Returns the expected amount of coin received.

.. _factory-pools-add-liquidity:

.. py:function:: StableSwap.add_liquidity(_deposit_amounts: uint256[2], _min_mint_amount: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Deposits coins into to the pool and mints new LP tokens.

    * ``_deposit_amounts``: List of amounts of underlying coins to deposit. Amounts correspond to the tokens at the same index locations within :func:`coins<StableSwap.coins>`.
    * ``_min_mint_amount``: Minimum amount of LP tokens to mint from the deposit.
    * ``_receiver``: Optional address that receives the LP tokens. If not specified, they are sent to the caller.

    Returns the amount of LP tokens that were minted in the deposit.

        .. code-block:: python

            >>> amounts = [1e18, 1e18]
            >>> expected = pool.calc_token_amount(amounts, True) * 0.99
            >>> pool.add_liquidity(amounts, expected, {'from': alice})

.. py:function:: StableSwap.remove_liquidity(_burn_amount: uint256, _min_amounts: uint256[2], _receiver: address = msg.sender) -> uint256[2]: nonpayable

    Withdraws coins from the pool and burns LP tokens.

    Withdrawal amounts are based on current deposit ratios. Withdrawals using this method do not incur a fee.

    * ``_burn_amount``: Quantity of LP tokens to burn in the withdrawal. Amounts correspond to the tokens at the same index locations within :func:`coins<StableSwap.coins>`.
    * ``_min_amounts``: Minimum amounts of coins to receive.
    * ``_receiver``: Optional address that receives the withdrawn coins. If not specified, the coins are sent to the caller.

    Returns a list of the amounts of coins that were withdrawn.

        .. code-block:: python

            >>> amount = pool.balanceOf(alice)
            >>> pool.remove_liquidity(pool, amount, 0, {'from': alice})

.. py:function:: StableSwap.remove_liquidity_imbalance(_amounts: uint256[2], _max_burn_amount: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Withdraw coins in an imbalanced amount.

    * ``_amounts``: List of amounts of underlying coins to withdraw. Amounts correspond to the tokens at the same index locations within :func:`coins<StableSwap.coins>`.
    * ``_max_burn_amount``: Maximum number of LP token to burn in the withdrawal.
    * ``_receiver``: Optional address that receives the withdrawn coins. If not specified, the coins are sent to the caller.

    Returns the amount of the LP tokens burned in the withdrawal.

        .. code-block:: python

            >>> amounts = [1e18, 1e18]
            >>> expected = pool.calc_token_amount(amounts, False) * 1.01
            >>> pool.remove_liquidity_imbalance(pool, amounts, expected, {'from': alice})

.. py:function:: StableSwap.remove_liquidity_one_coin(_burn_amount: uint256, i: int128, _min_received: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Withdraw a single asset from the pool.

    * ``_burn_amount``: Amount of LP tokens to burn in the withdrawal.
    * ``i``: Index value of the coin to withdraw. Can be found using the :func:`coins<StableSwap.coins>` getter method.
    * ``_min_amount``: Minimum amount of the coin to receive
    * ``_receiver``: Optional address that receives the withdrawn coin. If not specified, the coin is sent to the caller.

    Returns the amount of the coin received in the withdrawal.

        .. code-block:: python

            >>> amount = pool.balanceOf(alice)
            >>> expected = pool.calc_withdraw_one_coin(pool, amount, 0) * 1.01
            >>> pool.remove_liquidity_one_coin(amount, expected, 0, {'from': alice})


Claiming Admin Fees
===================

.. py:function:: StableSwap.withdraw_admin_fees(): nonpayable

    Transfer admin fees to the fee distributor, allowing the fees to be claimed by veCRV holders.

    Anyone can call this method. The destination address for the fees is hardcoded. To simplify fee distribution, this method swaps the admin balance of the non-base pool LP token into the base pool LP token.

LP Tokens
=========

Factory pools differ from traditional Curve pools in that the pool contract is also the LP token. This improves gas efficiency and simplifies the factory :ref:`deployment process <factory-deployer-deployment>`.

Pool contracts adhere to the `ERC-20 standard <https://eips.ethereum.org/EIPS/eip-20>`_. As such, the following methods are available:

Token Info
----------

.. py:function:: StableSwap.name() -> String[64]: view

    The name of the pool / LP token.

.. py:function:: StableSwap.symbol() -> String[32]: view

    The token symbol.

.. py:function:: StableSwap.decimals() -> uint256: view

    The number of decimals for the token. Curve pool tokens always use 18 decimals.

.. py:function:: StableSwap.totalSupply() -> uint256: view

Balances and Allowances
-----------------------

.. py:function:: StableSwap.balanceOf(_addr: address) -> uint256: view

    Getter for the current balance of an account.

.. py:function:: StableSwap.allowance(_owner: address, _spender: address) -> uint256: view

    Getter for the number of tokens ``_owner`` has approve ``_spender`` to transfer on their behalf.

    ``2**256-1`` it is considered infinite approval. The approval amount will not decrease when tokens are transferred.

Transfers and Approvals
-----------------------

.. py:function:: StableSwap.approve(_spender : address, _value : uint256) -> bool: nonpayable

    Approve ``_spender`` to transfer up to ``_value`` tokens on behalf of the caller.

    If an approval is given for ``2**256-1`` it is considered infinite. The approval amount will not decrease when tokens are transferred, reducing gas costs.

    * ``_spender`` Address to set the approval for
    * ``_value`` Amount of the caller's tokens that ``_spender`` is permitted to transfer

    Returns ``True`` on success. Reverts on failure.

.. py:function:: StableSwap.transfer(_to : address, _value : uint256) -> bool: nonpayable

    Transfer tokens from the caller to the given address.

    * ``_to``: Address receiving the tokens.
    * ``_value``: Amount of tokens to be transferred.

    Returns ``True`` on a successful call. Reverts on failure.

.. py:function:: StableSwap.transferFrom(_from : address, _to : address, _value : uint256) -> bool: nonpayable

    Transfer tokens between two addresses. The caller must have been given approval to transfer tokens on behalf of ``_from`` or the call will revert.

    * ``_from``: The address to transfer the tokens from.
    * ``_to``: Address receiving the tokens.
    * ``_value``: mount of tokens to be transferred.

     Returns ``True`` on a successful call. Reverts on failure.
