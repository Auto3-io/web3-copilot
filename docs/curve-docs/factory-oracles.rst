.. _factory-oracles:

===================================
Metapool Factory: Oracles
===================================

Factory contracts include Time-Weighted Average Price oracles. To understand these a bit better, you need to understand how Curve calculates price.

A curve pool is an array of ``balances`` of the tokens it holds. To provide a price, it calculates how much of ``x`` you can receive given amount ``y``.


Time-Weighted Average Price oracles
===================================

.. py:function:: MetaPool.get_price_cumulative_last() -> uint256[N_COINS]:

    Returns the current time-weighted average price (TWAP). This will represent the underlying balances of the pool.

    The value returned is the cumulative pool shifting balances over time

.. py:function:: MetaPool.block_timestamp_last() -> uint256:

    Returns the last timestamp that a TWAP reading was taken in unix time.

.. py:function:: MetaPool.get_twap_balances(_first_balances: uint256[N_COINS], _last_balances: uint256[N_COINS], _time_elapsed: uint256) -> uint256[N_COINS]:

    Calculate the current effective TWAP balances given two snapshots over time, and the time elapsed between the two snapshots.

    * ``_first_balances``: First ``price_cumulative_last`` array that was snapshot via ``get_price_cumulative_last``
    * ``_last_balances``: Second ``price_cumulative_last`` array that was snapshot via ``get_price_cumulative_last``
    * ``_time_elapsed``: The elapsed time in seconds between ``_first_balances`` and ``_last_balances``

    Returns the ``balances`` of the TWAP value.

.. py:function:: MetaPool.get_dy(i: int128, j: int128, dx: uint256, _balances: uint256[N_COINS] = [0,0]) -> uint256:

    Calculate the price for exchanging a token with index ``i`` to token with index ``j`` and amount ``dx`` given the ``_balances`` provided.

    * ``i``: The index of the coin being sent to the pool, as it related to the metapool
    * ``j``: The index of the coin being received from the pool, as it relates to the metapool
    * ``dx``: The amount of ``i`` being sent to the pool
    * ``_balances``: The array of balances to be used for purposes of calculating the output amount / exchange rate, this is the value returned in :func:`get_twap_balances <MetaPool.get_twap_balances>`

    Returns the quote / price as ``dy`` given ``dx``.

Security
========

The Curve TWAP is greatly inspired by `Uniswap TWAP architecture <https://uniswap.org/docs/v2/core-concepts/oracles/>`_, in that the price is a cumulative value over time, which reduces balance shifts due to flash loans, but also records the balances based on the previous block, to avoid recording flashloan data.
