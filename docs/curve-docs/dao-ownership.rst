.. _dao-ownership:

=============================
Curve DAO: Protocol Ownership
=============================

The Curve DAO controls admin functionality throughout the protocol. Performing calls to to owner/admin-level functions is only possible via a successful DAO vote.

Ownership is handled via a series of proxy contracts. At a high level, the flow of ownership is:

    ``DAO -> Aragon Agent -> Ownership Proxy -> Contracts``

At the ownership proxy level there are two main contracts:

    * ``PoolProxy``: Admin functionality for :ref:`exchange contracts<exchange-pools>`
    * ``GaugeProxy``: Admin functionality for :ref:`liquidity gauges<dao-gauges>`

The DAO is capable of replacing the ownership proxies via a vote. Deployment addresses for the current contracts can be found in the :ref:`addresses reference<addresses-dao>` section of the documentation.

.. _dao-ownership-agents:

Agents
======

The Curve DAO has a total of three `Aragon Agent <https://hack.aragon.org/docs/guides-use-agent>`_ ownership addresses, which are governed by two independent DAOs:

1. The **Community DAO** (or just "the DAO") governs the day-to-day operation of the protocol.

    Voting is based on a user's holdings of "Vote Escrowed CRV" (veCRV). veCRV is obtained by locking CRV for up to 4 years, with 1 veCRV equal to 1 CRV locked for 4 years. As the lock time decreases, An account's veCRV balance decreases linearly as the time remaining until unlock decreases. veCRV is non-transferrable.

    An account must have a minimum balance of 2500 veCRV to make a DAO vote. Each vote lasts for one week. Votes cannot be executed until the entire week has passed.

    The DAO has ownership of two admin accounts:

    * The **ownership admin** controls most functionality within the protocol. Performing an action via the ownership admin requires a 30% quorum with 51% support.
    * The **parameter admin** has authority to modify parameters on pools, such as adjusting the amplification co-efficient. Performing an action via the paramater admin requries a 15% quorum with 51% support.

2. The **Emergency DAO** has limited authority to kill pools and gauges during extraordinary circumstances.

    The emergency DAO consists of `nine members <https://dao.curve.fi/emergencymembers>`_, comprised of a mix of the Curve team and prominent figures within the DeFi community. Each member has one vote. Any member may propose a vote.

    All members of the emergency DAO may propose new votes. A vote lasts for 24 hours and can be executed immediately once it receives 66% support.

.. _dao-ownership-pool-proxy:

PoolProxy
=========

``PoolProxy`` is used for indirect ownership of :ref:`exchange contracts<exchange-pools>`.

Source code for this contract is available on `Github <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/PoolProxy.vy>`_.

Configuring Fee Burners
-----------------------

.. py:function:: PoolProxy.burners(coin: address) -> address: view

    Getter for the burner contract address for ``coin``.

.. py:function:: PoolProxy.set_burner(coin: address, burner: address): nonpayable

    Set burner of ``coin`` to ``burner`` address.

    Callable only by the ownership admin.

.. py:function:: PoolProxy.set_many_burners(coins: address[20], burners: address[20]): nonpayable

    Set burner contracts for many coins at once.

    * ``coins``: Array of coin addresses. If you wish to set less than 20 burners, fill the remaining array slots with ``ZERO_ADDRESS``.
    * ``burners``: Array of burner addresses. The address as index ``n`` within this list corresponds to the address at index ``n`` within ``coins``.

    Callable only by the ownership admin.

.. py:function:: PoolProxy.set_donate_approval(pool: address, caller: address, is_approved: bool): nonpayable

    Set approval for an address to call ``donate_admin_fees`` on a specific pool.

    * ``pool``: Pool address
    * ``caller``: Adddress to set approval for
    * ``is_approved``: Approval status

    Callable only by the ownership admin.

.. py:function:: PoolProxy.set_burner_kill(_is_killed: bool): nonpayable

    Disable or enable the process of fee burning.

    Callable by the emergency and ownership admins.

Withdraing and Burning Fees
---------------------------

.. py:function:: PoolProxy.withdraw_admin_fees(pool: address): nonpayable

    Withdraw admin fees from ``pool`` into this contract.

    This is the first step in fee burning. This function is unguarded - it may be called by any address.

.. py:function:: PoolProxy.withdraw_many(pools: address[20]): nonpayable

    Withdraw fees from multiple pools in a single call.

    This function is unguarded.

.. py:function:: PoolProxy.burn(coin: address): nonpayable

    Transfer the contract's balance of ``coin`` into the preset burner and execute the burn process.

    Only callable via an externally owned account; a check that ``tx.origin == msg.sender`` is performed to prevent potential flashloan exploits.

.. py:function:: PoolProxy.burn_many(coins: address[20]): nonpayable

    Execute the burn process on many coins at once.

    Note that burning can be very gas intensive. In some cases burning 20 coins at once is not possible due to the block gas limit.

.. py:function:: PoolProxy.donate_admin_fees(_pool: address): nonpayable

    Donate a pool's current admin fees to the pool LPs.

    Callable by the ownership admin, or any address given explicit permission to do so via :func:`set_donate_approval<PoolProxy.set_donate_approval>`

Killing Pools
-------------

.. py:function:: PoolProxy.kill_me(_pool: address): nonpayable

    Pauses the pool.

    When paused, it is only possible for existing LPs to remove liquidity via ``remove_liquidity``.  Exchanges and adding or removing liquidity in other ways are blocked.

    Callable only by the emergency admin.

.. py:function:: PoolProxy.unkill_me(_pool: address): nonpayable

    Unpause a pool that was previously paused, re-enabling exchanges.

    Callable by the emergency and ownership admins.

Pool Ownership
--------------

.. py:function:: PoolProxy.commit_transfer_ownership(pool: address, new_owner: address): nonpayable

    Initiate an ownership transfer of ``pool`` to ``new_owner``.

    Callable only by the ownership admin.

.. py:function:: PoolProxy.accept_transfer_ownership(pool: address): nonpayable

    Accept ending ownership transfer for ``pool``.

    This function is unguarded.

.. py:function:: PoolProxy.revert_transfer_ownership(pool: address): nonpayable

    Cancel a pending ownership transfer for ``pool``.

    Callable by the emergency and ownership admins.

Modifying Pool Parameters
-------------------------

.. py:function:: PoolProxy.commit_new_parameters(pool: address, amplification: uint256, new_fee: uint256, new_admin_fee: uint256, min_asymmetry: uint256): nonpayable

    Initiate a change of parameters for a pool.

    * ``pool``: Pool address
    * ``amplification`` New Amplification coefficient
    * ``new_fee`` New fee
    * ``new_admin_fee`` New admin fee
    * ``min_asymmetry`` Minimal asymmetry factor allowed.

    Asymmetry factor is: ``Prod(balances) / (Sum(balances) / N) ** N``

    Callable only by the parameter admin.

.. py:function:: PoolProxy.apply_new_parameters(_pool: address): nonpayable

    Apply a parameter change on a pool.

    This function is unguarded, however it can only be called via an EOA to minimize the likelihood of a flashloan exploit.

.. py:function:: PoolProxy.revert_new_parameters(_pool: address): nonpayable

    Revert comitted new parameters for ``pool``

    Callable by the emergency and ownership admins.

.. py:function:: PoolProxy.ramp_A(_pool: address, _future_A: uint256, _future_time: uint256): nonpayable

    Start a gradual increase of the amplification coefficient for a pool.

    * ``_pool``: Pool address
    * ``future_A``: New amplification coefficient to ramp to
    * ``future_time``: Epoch time to complete the ramping at

    Callable only by the parameter admin.

.. py:function:: PoolProxy.stop_ramp_A(pool: address): nonpayable

    Stop the gradual ramping of pool's amplification coefficient.

    Callable by the emergency and parameter admins.

.. py:function:: PoolProxy.commit_new_fee(pool: address, new_fee: uint256, new_admin_fee: uint256):

    Initiate change in the fees for a pool.

    * ``pool`:` Pool address
    * ``new_fee``: New fee
    * ``new_admin_fee``: New admin fee

    Callable only by the parameter admin.

.. py:function:: PoolProxy.apply_new_fee(_pool: address): nonpayable

    Apply a fee change to a pool.

    This function is unguarded.

GaugeProxy
==========

``GaugeProxy`` is used for indirect ownership of :ref:`liquidity gauges<dao-gauges>`.

Source code for this contract is available on `Github <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/GaugeProxy.vy>`_.

.. py:function:: GaugeProxy.set_rewards(gauge: address, reward_contract: address, sigs: bytes32, reward_tokens: address[8]): nonpayable

    Set the active reward contract for a ``LiquidityGaugeV2`` deployment.

    See the :ref:`gauge documentation<LiquidityGaugeV2.set_rewards>` for details on how this function works.

    * ``gauge`` Gauge address
    * ``reward_contract``: Address of the staking contract. Set to ``ZERO_ADDRESS`` if staking rewards are being removed.
    * ``sigs``: A concatenation of three four-byte function signatures: ``stake``, ``withdraw`` and ``getReward``. The signatures are then right padded with empty bytes. See the example below for more information on how to prepare this data.
    * ``reward_tokens``: Array of rewards tokens received from the staking contract.

    Callable by the ownership admin.

.. py:function:: GaugeProxy.set_killed(gauge: address, is_killed: bool): nonpayable

    Set the killed status for a gauge.

    * ``gauge`` Gauge address
    * ``is_killed`` Killed status to set

    Once killed, a gauge always yields a rate of 0 and so cannot mint CRV. Any vote-weight given to a killed gauge effectively burns CRV.

    Callable by the ownership admin or the emergency admin.

.. py:function:: GaugeProxy.commit_transfer_ownership(gauge: address, new_owner: address): nonpayable

    Initiate the transfer of ownership of a gauge.

    * ``gauge``: Address of the gauge to transfer ownership of
    * ``new_owner``: New owner address

    Callable only by the ownership admin.

.. py:function:: GaugeProxy.accept_transfer_ownership(gauge: address): nonpayable

    Apply ownership transfer of a gauge.

    This function is unguarded. After ``commit_transfer_ownership`` has been called by the current owner, anyone can call into ``GaugeProxy`` to trigger the acceptance.
