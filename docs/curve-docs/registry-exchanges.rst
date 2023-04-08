.. _registry-exchanges:

===================
Registry: Exchanges
===================

The registry exchange contract is used to find pools and query exchange rates for token swaps. It also provides a unified exchange API that can be useful for on-chain integrators.

Source code for this contract is available on `Github <https://github.com/curvefi/curve-pool-registry/blob/master/contracts/Swaps.vy>`_.

Deployment Address
==================

The exchange contract is registered in the address provider with ID ``2``. To get the current address:

    .. code-block:: python

        >>> provider = Contract('0x0000000022D53366457F9d5E68Ec105046FC4383')
        >>> provider.get_address(2)
        '0xD1602F68CC7C4c7B59D686243EA35a9C73B0c6a2'

Finding Pools and Swap Rates
============================

.. py:function:: Swaps.get_best_rate(_from: address, _to: address, _amount: uint256, _exclude_pools: address[8]) -> (address, uint256): view

    Find the pool offering the best rate for a given swap.

    * ``_from``: Address of coin being sent.
    * ``_to``: Address of coin being received.
    * ``_amount``: Quantity of `_from` being sent.
    * ``_exclude_pools``: [optional] A list of up to 8 addresses which should be excluded from the query.

    Returns the address of the pool offering the best rate, and the expected amount received in the swap.

.. py:function:: Swaps.get_exchange_amount(_pool: address, _from: address, _to: address, _amount: uint256) -> uint256: view

    Get the current number of coins received in an exchange.

    * ``_pool``: Pool address.
    * ``_from``: Address of coin to be sent.
    * ``_to``: Address of coin to be received.
    * ``_amount``: Quantity of ``_from`` to be sent.

    Returns the quantity of ``_to`` to be received in the exchange.

Swapping Tokens
================

.. py:function:: Swaps.exchange( _pool: address, _from: address, _to: address, _amount: uint256, _expected: uint256, _receiver: address = msg.sender) -> uint256: payable

    Perform an token exchange using a specific pool.

    * ``_pool``: Address of the pool to use for the swap.
    * ``_from``: Address of coin being sent.
    * ``_to``: Address of coin being received.
    * ``_amount``: Quantity of ``_from`` being sent.
    * ``_expected``: Minimum quantity of ``_to`` received in order for the transaction to succeed.
    * ``_receiver``: Optional address to transfer the received tokens to. If not specified, defaults to the caller.

    Returns the amount of ``_to`` received in the exchange.

.. py:function:: Swaps.exchange_with_best_rate(_from: address,  _to: address, _amount: uint256, _expected: uint256, _receiver: address = msg.sender) -> uint256: payable

    Perform an exchange using the pool that offers the best rate.

    * ``_from``: Address of coin being sent.
    * ``_to``: Address of coin being received.
    * ``_amount``: Quantity of `_from` being sent.
    * ``_expected``: Minimum quantity of ``_to`` received in order for the transaction to succeed.
    * ``_receiver``: Optional address to transfer the received tokens to. If not specified, defaults to the caller.

    Returns the amount of ``_to`` received in the exchange.

    .. warning::

        This function queries the exchange rate for every pool where a swap between ``_to`` and ``_from`` is possible. For pairs that can be swapped in many pools this will result in very significant gas costs!
