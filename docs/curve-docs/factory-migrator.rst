.. _factory-migrator:

====================================
Metapool Factory: Liquidity Migrator
====================================

The ``PoolMigrator`` contract is used for migrating liquidity between Curve factory pools. It is deployed to the mainnet at the following address:

    `0xd6930b7f661257DA36F93160149b031735237594 <https://etherscan.io/address/0xd6930b7f661257DA36F93160149b031735237594>`_

Source code for this contract is may be viewed on `Github <https://github.com/curvefi/curve-factory/blob/master/contracts/PoolMigrator.vy>`_.

Migrating Liquidity between Pools
=================================

.. py:function:: Factory.migrate_to_new_pool(_old_pool: address, _new_pool: address, _amount: uint256) -> uint256:

    Migrate liquidity between two pools.

    Each pool must be deployed by the curve factory (v1 or v2) and contain identical assets. Depending on the imbalance of each pool, the migration may incur slippage or provide a bonus.

    Prior to calling this method, the caller must have given approval for the migrator to transfer up to ``_amount`` LP tokens from ``_old_pool``.


    * ``_old_pool``: Address of the pool to migrate from
    * ``_new_pool``: Address of the pool to migrate into
    * ``_amount``: Number of ``_old_pool`` LP tokens to migrate

    Returns the number of ``_new_pool`` LP tokens received in the migration.

        .. code-block:: python

            >>> migrator = Contract('0xd6930b7f661257DA36F93160149b031735237594')
            >>> old_pool = Contract('0x36F3FD68E7325a35EB768F1AedaAe9EA0689d723')
            >>> new_pool = Contract('0x83D2944d5fC10A064451Dc5852f4F47759F249B6')

            >>> balance = old_pool.balanceOf(alice)

            >>> old_pool.approve(migrator, balance, {'from': alice})
            Transaction sent: 0x8fc0dc0844ccbbed63d9cb7f2820087db5f70b320efea7ef4ce6b4a678e3cd45
              Gas price: 20 gwei   Gas limit: 1100000   Nonce: 9

            >>> migrator.migrate_to_new_pool(old_pool, new_pool, balance, {'from': alice})
            Transaction sent: 0xd65182491c13b2620f84fe2d501ace5c8ab1cda1b9ea54d40f4f2351cccd52b6
              Gas price: 20 gwei   Gas limit: 1100000   Nonce: 10
