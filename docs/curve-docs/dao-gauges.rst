.. _dao-gauges:

===============================================
The Curve DAO: Liquidity Gauges and Minting CRV
===============================================

Curve incentivizes liquidity providers with the CRV, the protocol governance token. Allocation, distribution and minting of CRV are managed via several related DAO contracts:

* ``LiquidityGauge``: Measures liquidity provided by users over time, in order to distribute CRV and other rewards
* ``GaugeController``: Central controller that maintains a list of gauges, weights and type weights, and coordinates the rate of CRV production for each gauge
* ``Minter``: CRV minting contract, generates new CRV according to liquidity gauges

Implementation Details
======================

CRV Inflation
-------------

CRV follows a piecewise linear inflation schedule. The inflation is reduced by :math:`2^{1/4}` each year. Each time the inflation reduces, a new mining epoch starts.

.. image:: inflation.svg
    :width: 400px
    :alt: Inflation Schedule
    :align: center

The initial supply of CRV is :math:`1.273` billion tokens, which is :math:`42\%` of the eventual :math:`t\rightarrow\infty"` supply of :math:`\approx 3.03` billion tokens. All of these initial tokens are gradually vested (with every block). The initial inflation rate which supports the above inflation schedule is
:math:`r=22.0\%` (279.6 millions per year). All of the inflation is distributed to Curve liquidity providers, according to measurements taken by the gauges. During the first year, the approximate inflow into circulating supply is 2 million CRV per day. The initial circulating supply is 0.

Liquidity Gauges
----------------

Inflation is directed to users who provide liquidity within the protocol. This usage is measured via "Liquidity Gauge" contracts. Each pool has an individual liquidity gauge. The :ref:`Gauge Controller<dao-gauges-controller>` maintains a list of gauges and their types, with the weights of each gauge and type.

To measure liquidity over time, the user deposits their LP tokens into the liquidity gauge. Coin rates which the gauge is getting depends on current inflation rate, gauge weight, and gauge type weights. Each user receives a share of newly minted CRV proportional to the amount of LP tokens locked. Additionally, rewards may be boosted by up to factor of 2.5 if the user vote-locks tokens for Curve governance in the :ref:`Voting Escrow<dao-vecrv>` contract.

Suppose we have the inflation rate :math:`r` changing with every epoch (1 year), gauge weight :math:`w_g` and gauge type weight :math:`w_t`. Then, all the gauge handles the stream of inflation with the rate :math:`r^{\prime} = w_g w_t r` which it can update every time :math:`w_g, w_t`, or mining epoch changes.

To calculate a user's share of :math:`r^{\prime}`, we must calculate the integral: :math:`$I_u = \int \frac{r^{\prime}(t)\, b_u(t)}{S(t)}\,dt,` where :math:`b_u(t)` is the balance supplied by the user (measured in LP tokens) and :math:`S(t)` is total liquidity supplied by users, depending on the time :math:`t`; the value :math:`I_u` gives the amount of tokens which the user has to have minted to them. The user's balance :math:`b_u` changes every time the user :math:`$u` makes a deposit or withdrawal, and :math:`S` changes every time _any_ user makes a deposit or withdrawal (so :math:`$S` can change many times in between two events for the user :math:`u"`. In the liquidity gauge contract, the vaule of :math:`I_u` is recorded per-user in the public ``integrate_fraction`` mapping.

To avoid requiring that all users to checkpoint periodically, we keep recording values of the following integral (named ``integrate_inv_supply`` in the contract):

    :math:`$I_{is}(t) = \int_0^{t} \frac{r^{\prime}(t)}{S(t)}dt.`

The value of :math:`I_{is}` is recorded at any point any user deposits or withdraws, as well as every time the rate :math:`r^{\prime}` changes (either due to weight change or change of mining epoch).

When a user deposits or withdraws, the change in :math:`I_u` can be calculated as the current (before user's action) value of :math:`I_{is}` multiplied by the pre-action user's balance, and sumed up across the user's balances: :math:`$I_u(t_k) =\sum_k b_u(t_k) \left[I_{is}(t_k) - I_{is}(t_{k-1})\right].` The per-user integral is possible to repalce with this sum because :math:`b_u(t)` changed for all times between :math:`t_{k-1}` and :math:`t_k`.

.. _dao-gauges-boost:

Boosting
--------

In order to incentivize users to participate in governance, and additionally create stickiness for liquidity, we implement the following mechanism. A user's balance, counted in the liquidity gauge, gets boosted by users locking CRV tokens in :ref:`Voting Escrow<dao-vecrv>` contract, depending on their vote weight :math:`w_i`: :math:`b_u^* = \min\left( 0.4\,b_u + 0.6\,S\frac{w_i}{W},\, b_u \right).` The value of :math:`w_i` is taken at the time the user performs any action (deposit, withdrawal, withdrawal of minted CRV tokens) and is applied until the next action this user performs.

If no users vote-lock any CRV (or simply don't have any), the inflation will simply be distributed proportionally to the liquidity :math:`b_u` each one of them provided. However, if a user stakes enough CRV, they are able to boost their stream of CRV by up to factor of 2.5 (reducing it slightly for all users who are not doing that).

Implementation details are such that a user gets the boost at the time of the last action or checkpoint. Since the voting power decreases with time, it is favorable for users to apply a boost and do no further actions until they vote-lock more tokens. However, once the vote-lock expires, everyone can "kick" the user by creating a checkpoint for that user and, essentially, resetting the user to no boost if they have no voting power at that point already.

Finally, the gauge is supposed to not miss a full year of inflation (e.g. if there were no interactions with the guage for the full year). If that ever happens, the abandoned gauge gets less CRV.

Gauge Weight Voting
-------------------

Users can allocate their veCRV towards one or more liquidity gauges. Gauges receive a fraction of newly minted CRV tokens proportional to how much veCRV the gauge is allocated. Each user with a veCRV balance can change their preference at any time.

When a user applies a new weight vote, it gets applied at the start of the next epoch week. The weight vote for any one gauge cannot be changed more often than once in 10 days.

.. _dao-gauges-controller:

The Gauge Controller
--------------------

The "Gauge Controller" maintains a list of gauges and their types, with the weights of each gauge and type. In order to implement weight voting, ``GaugeController`` has to include parameters handling linear character of voting power each user has.

``GaugeController`` records points (bias + slope) per gauge in ``vote_points``, and _scheduled_ changes in biases and slopes for those points in ``vote_bias_changes`` and ``vote_slope_changes``. New changes are applied at the start of each epoch week.

Per-user, per-gauge slopes are stored in ``vote_user_slopes``, along with the power the user has used and the time their vote-lock ends.

The totals for slopes and biases for vote weight per gauge, and sums of those
per type, are scheduled / recorded for the next week, as well as the points
when voting power gets to 0 at lock expiration for some of users.

When a user changes their gauge weight vote, the change is scheduled for the next epoch week, not immediately. This reduces the number of reads from storage which must to be performed by each user: it is proportional to the number of weeks since the last change rather than the number of interactions from other users.

Gauge Types
===========

Each liquidity gauge is assigned a type within the gauge controller. Grouping gauges by type allows the DAO to adjust the emissions according to type, making it possible to e.g. end all emissions for a single type.

Currently active gauge types are as follows:

   * Ethereum (stableswap pools): ``0``
   * Fantom: ``1``
   * Polygon (Matic): ``2``
   * xDai: ``4``
   * Ethereum (crypto pools): ``5``
   * Arbitrum ``7``
   * Avalanche ``8``
   * Harmony ``9``
   * Fundraising ``10`` 

Types ``3`` and ``6`` have been deprecated.


.. _dao-gauges-liquidity-gauge:

LiquidityGauge
==============

Each pool has a unique liquidity gauge. Deployment addresses can be found in the :ref:`addresses reference<addresses-gauges>` section of the documentation.

There are several versions of liquidity gauge contracts in use. Source code for these contracts is available on `Github <https://github.com/curvefi/curve-dao-contracts/tree/master/contracts/gauges>`_.

Querying Gauge Information
--------------------------

.. py:function:: LiquidityGauge.lp_token() -> address: view

    The address of the LP token that may be deposited into the gauge.

.. py:function:: LiquidityGauge.totalSupply -> uint256: view

    The total amount of LP tokens that are currently deposited into the gauge.

.. py:function:: LiquidityGauge.working_supply() -> uint256: view

    The "working supply" of the gauge - the effective total LP token amount after all deposits have been :ref:`boosted<dao-gauges-boost>`.

Querying User Information
-------------------------

.. py:function:: LiquidityGauge.balanceOf(addr: address) -> uint256: view

    The current amount of LP tokens that ``addr`` has deposited into the gauge.

.. py:function:: LiquidityGauge.working_balances(addr: address) -> uint256: view

    The "working balance" of a user - their effective balance after :ref:`boost<dao-gauges-boost>` has been applied.

.. py:function:: LiquidityGauge.claimable_tokens(addr: address) -> uint256: nonpayable

    The amount of currently mintable CRV for ``addr`` from this gauge.

    .. note::

        Calling this function `modifies the state <https://vyper.readthedocs.io/en/stable/control-structures.html#mutability>`_. Off-chain integrators can call it as though it were a ``view`` function, however on-chain integrators **must** use it as ``nonpayable`` or the call will revert.

    .. code-block:: python

        >>> gauge.claimable_tokens.call(alice)
        3849184923983248t5273

.. py:function:: LiquidityGauge.integrate_fraction(addr: address) -> uint256: view

    The total amount of CRV, both mintable and already minted, that has been allocated to ``addr`` from this gauge.

Checkpoints
-----------

.. py:function:: LiquidityGauge.user_checkpoint(addr: address) -> bool: nonpayable

    Record a checkpoint for ``addr``, updating their boost.

    Only callable by ``addr`` or ``Minter`` - you cannot trigger a checkpoint for another user.

.. py:function:: LiquidityGauge.kick(addr: address): nonpayable

    Trigger a checkpoint for ``addr``. Only callable when the current boost for ``addr`` is greater than it should be, due to an expired veCRV lock.

Deposits and Withdrawals
------------------------

.. py:function:: LiquidityGauge.deposit(amount: uint256, receiver: address = msg.sender): nonpayable

    Deposit LP tokens into the gauge.

    Prior to depositing, ensure that the gauge has been approved to transfer ``amount`` LP tokens on behalf of the caller.

    * ``amount``: Amount of tokens to deposit
    * ``receiver``: Address to deposit for. If not given, defaults to the caller. If specified, the caller must have been previous approved via :func:`approved_to_deposit<LiquidityGauge.approved_to_deposit>`

        .. code-block:: python

            >>> lp_token = Contract(gauge.lp_token())
            >>> balance = lp_token.balanceOf(alice)

            >>> lp_token.approve(gauge, balance, {'from': alice})
            Transaction sent: 0xa791801ccc57ad4edcfcaff7b5dab1c9101b78cf978a8d7fc185d9194bd3c2fa
              Gas price: 20.0 gwei   Gas limit: 56299   Nonce: 23

            >>> gauge.deposit(balance, {'from': alice})
            Transaction sent: 0xd4edcfcaff7b5dab1c9101b78cf978a8d7fc185d9194bd3c2faa791801ccc57a
              Gas price: 20.0 gwei   Gas limit: 187495   Nonce: 24

.. py:function:: LiquidityGauge.withdraw(amount: uint256): nonpayable

    Withdraw LP tokens from the gauge.

    * ``amount``: Amount of tokens to withdraw

        .. code-block:: python

            >>> balance = gauge.balanceOf(alice)
            >>> gauge.withdraw(balance, {'from': alice})
            Transaction sent: 0x1b78cf978a8d7fc185d9194bd3c2faa791801ccc57ad4edcfcaff7b5dab1c910
              Gas price: 20.0 gwei   Gas limit: 217442   Nonce: 25


.. py:function:: LiquidityGauge.approved_to_deposit(caller: address, receiver: address) -> bool: view

Return the approval status for ``caller`` to deposit LP tokens into the gauge on behalf of ``receiver``.

.. py:function:: LiquidityGauge.set_approve_deposit(depositor: address, can_deposit: bool): nonpayable

    Approval or revoke approval for another address to deposit into the gauge on behalf of the caller.

    * ``depositor``: Address to set approval for
    * ``can_deposit``: Boolean - can this address deposit on behalf of the caller?

        .. code-block:: python

            >>> gauge.approved_to_deposit(bob, alice)
            False

            >>> gauge.set_approve_deposit(bob, True, {'from': alice})
            Transaction sent: 0xc185d9194bd3c2faa791801ccc57ad4edcfcaff7b5dab1c9101b78cf978a8d7f
              Gas price: 20.0 gwei   Gas limit: 47442   Nonce: 26

            >>> gauge.approved_to_deposit(bob, alice)
            True

Killing the Gauge
-----------------

.. py:function:: LiquidityGauge.kill_me(): nonpayable

    Toggle the killed status of the gauge.

    This function may only be called by the :ref:`ownership or emergency admins<dao-ownership-agents>` within the DAO.

    A gauge that has been killed is unable to mint CRV. Any gauge weight given to a killed gauge effectively burns CRV. This should only be done in a case where a pool had to be killed due to a security risk, but the gauge was already voted in.

.. py:function:: LiquidityGauge.is_killed() -> bool: view

    The current killed status of the gauge.

LiquidityGaugeReward
====================

Along with measuring liquidity for CRV distribution, ``LiquidityGaugeReward`` stakes LP tokens into an SNX `staking rewards <https://github.com/Synthetixio/synthetix/blob/master/contracts/StakingRewards.sol>`_ contract and handles distribution of an the additional rewards token. Rewards gauges include the full API of :ref:`LiquidityGauge<dao-gauges-liquidity-gauge>`, with the following additional methods:

Querying Reward Information
---------------------------

.. py:function:: LiquidityGaugeReward.reward_contract() -> address: view

    The address of the `staking rewards <https://github.com/Synthetixio/synthetix/blob/master/contracts/StakingRewards.sol>`_ contract that LP tokens are staked into.

.. py:function:: LiquidityGaugeReward.rewarded_token() -> address: view

    The address of the reward token being received from :func:`reward_contract<LiquidityGaugeReward.reward_contract>`.

.. py:function:: LiquidityGaugeReward.is_claiming_rewards() -> bool: view

    Boolean indicating if rewards are currently being claimed by this gauge.

Calculating Claimable Rewards
-----------------------------

.. note::

    There is no single function that returns the currently claimable reward amount. To calculate:

    .. code-block:: python

        >>> gauge.claimable_reward(alice) - gauge.claimed_rewards_for(alice)
        97924174626247611803

.. py:function:: LiquidityGaugeReward.claimable_reward(addr: address) -> uint256: view

    The total earned reward tokens, both claimed and unclaimed, for ``addr``.

.. py:function:: LiquidityGaugeReward.claimed_rewards_for(addr: address) -> uint256: view

    The number of reward tokens already claimed for ``addr``.

Claiming Rewards
----------------

.. py:function:: LiquidityGaugeReward.claim_rewards(addr: address = msg.sender): nonpayable

    Claim reward tokens for an address.  If ``addr`` is not specified, defaults to the caller.

LiquidityGaugeV2
================

The v2 liquidity gauge adds a full ERC20 interface to the gauge, tokenizing deposits so they can be directly transferred between accounts without having to withdraw and redeposit. It also improves flexibility for onward staking, allowing staking to be enabled or disabled at any time and handling up to eight reward tokens at once.

Querying Reward Information
---------------------------

.. py:function:: LiquidityGaugeV2.reward_contract() -> address: view

    The address of the `staking rewards <https://github.com/Synthetixio/synthetix/blob/master/contracts/StakingRewards.sol>`_ contract that LP tokens are staked into.

.. py:function:: LiquidityGaugeV2.rewarded_tokens(idx: uint256) -> address: view

    Getter for an array of rewarded tokens currently being received by :func:`reward_contract<LiquidityGaugeV2.reward_contract>`.

    The contract is capable of handling up to eight reward tokens at once - if there are less than eight currently active, some values will return as ``ZERO_ADDRESS``.

Approvals and Transfers
-----------------------

.. py:function:: LiquidityGaugeV2.transfer(_to : address, _value : uint256) -> bool:

    Transfers gauge deposit from the caller to ``_to``.

    This is the equivalent of calling :func:`withdraw(_value) <LiquidityGauge.withdraw>` followed by :func:`deposit(_value, _to) <LiquidityGauge.deposit>`. Pending reward tokens for both the sender and receiver are also claimed during the transfer.

    Returns ``True`` on success. Reverts on failure.

.. py:function:: LiquidityGaugeV2.transferFrom(_from : address, _to : address, _value : uint256) -> bool:

    Transfers a gauge deposit between ``_from`` and ``_to``.

    The caller must have previously been approved to transfer at least ``_value`` tokens on behalf of ``_from``. Pending reward tokens for both the sender and receiver are also claimed during the transfer.

    Returns ``True`` on success. Reverts on failure.

.. py:function:: LiquidityGaugeV2.approve(_spender : address, _value : uint256) -> bool:

    Approve the passed address to transfer the specified amount of tokens on behalf of the caller.

    Returns ``True`` on success. Reverts on failure.

Checking and Claiming Rewards
-----------------------------

.. note::

    Rewards are claimed automatically each time a user deposits or withdraws from the gauge, and on gauge token transfers.

.. py:function:: LiquidityGaugeV2.claimable_reward(_addr: address, _token: address) -> uint256: nonpayable

    Get the number of claimable reward tokens for a user.

    .. note::

        This function determines the claimable reward by actually claiming and then returning the received amount. As such, it is state changing and only of use to off-chain integrators. The `mutability <https://vyper.readthedocs.io/en/stable/control-structures.html#mutability>`_ should be manually changed to ``view`` within the ABI.

    * ``_addr`` Account to get reward amount for
    * ``_token`` Token to get reward amount for

    Returns the number of tokens currently claimable for the given address.

.. py:function:: LiquidityGaugeV2.claim_rewards(_addr: address = msg.sender): nonpayable

    Claim all available reward tokens for ``_addr``. If no address is given, defaults to the caller.

.. py:function:: LiquidityGaugeV2.claim_historic_rewards(_reward_tokens: address[8], _addr: address = msg.sender): nonpayable

    Claim reward tokens available from a previously-set staking contract.

    * ``_reward_tokens``: Array of reward token addresses to claim
    * ``_addr``: Address to claim for. If none is given, defaults to the caller.


Setting the Rewards Contract
----------------------------

.. py:function:: LiquidityGaugeV2.set_rewards(_reward_contract: address, _sigs: bytes32, _reward_tokens: address[8]): nonpayable

    Set the active reward contract.

    * ``_reward_contract``: Address of the staking contract. Set to ``ZERO_ADDRESS`` if staking rewards are being removed.
    * ``_sigs``: A concatenation of three four-byte function signatures: ``stake``, ``withdraw`` and ``getReward``. The signatures are then right padded with empty bytes. See the example below for more information on how to prepare this data.
    * ``_reward_tokens``: Array of rewards tokens received from the staking contract.

    This action is only possible via the contract admin. It cannot be called when the gauge has no deposits. As a safety precaution, this call validates all the signatures with the following sequence of actions:

        1. LP tokens are deposited into the new staking contract, verifying that the deposit signature is correct.
        2. ``balanceOf`` is called on the LP token to confirm that the gauge's token balance is now zero.
        3. The LP tokens are withdrawn, verifying that the withdraw function signature is correct.
        4. ``balanceOf`` is called on the LP token again, to confirm that the gauge has successfully withdrawn it's entire balance.
        5. A call to claim rewards is made to confirm that it does not revert.

    These checks are required to protect against an incorrectly designed staking contract or incorrectly structured input arguments.

    It is also possible to claim from a reward contract that does not require onward staking. In this case, use ``00000000`` for the function selectors for both staking and withdrawing.

    An example of generating the signatures input and enabling a vanilla SNX rewards contract:

        .. code:: python

            >>> Rewards = Contract("0x99ac10631f69c753ddb595d074422a0922d9056b")

            # first, we get the signatures for depositing, withdrawing and claiming
            >>> sigs = [rewards.stake.signature, rewards.withdraw.signature, rewards.getReward.signature]
            >>> sigs
            ["0xa694fc3a", "0x2e1a7d4d", "0x3d18b912"]

            # now we remove the leading 0x and concatentate them
            >>> sigs = "".join(i[2:] for i in sigs)
            >>> sigs
            "a694fc3a2e1a7d4d3d18b912"

            # finally, we add the leading 0x and trailing 00 bytes
            >>> sigs = "0x" + sigs + ("00" * 20)
            >>> sigs
            "0xa694fc3a2e1a7d4d3d18b9120000000000000000000000000000000000000000"

            # now we are ready to set the rewards contract
            >>> gauge.set_rewards(rewards, sigs, [reward_token] + [ZERO_ADDRESS] * 7, {'from': alice})

LiquidityGaugeV3
================

``LiquidityGaugeV3`` is the current iteration of liquidity gauge used for curve pools on Ethereum mainnet. It retains a majority of ``LiquidityGaugeV2``'s functionality such as tokenized deposits, and flexible onward staking with up to 8 reward tokens with some modifications.

Outline of modified functionality:

    1. Ability to redirect claimed rewards to an alternative account.
    2. Opt-in claiming of rewards on interactions with the gauge, instead of auto-claiming.
    3. Retrieving rewards from the reward contract happens at a minimum of once an hour, for reduced gas costs.
    4. Expose the amount of claimed and claimable rewards for users.
    5. Removal of ``claim_historic_rewards`` function.
    6. Modify ``claimable_reward`` to be a slightly less accurate view function.
    7. Reward tokens can no longer be removed once set, adding more tokens requires providing the array of reward_tokens with any new tokens appended.
    8. :func:`deposit(_value, _to) <LiquidityGauge.deposit>` and :func:`withdraw(_value, _to) <LiquidityGauge.deposit>` functions have an additional optional argument ``_claim_rewards``, which when set to ``True`` will claim any pending rewards.

As this gauge maintains a similar API to ``LiquidityGaugeV2``, the documentation only covers functions that were added or modified since the previous version.

Querying Reward Information
---------------------------

.. py:function:: LiquidityGaugeV3.rewards_receiver(addr: address) -> address: view

    This gauge implementation allows for the redirection of claimed rewards to alternative accounts. If an account has enabled a default rewards receiver this function will return that default account, otherwise it'll return ``ZERO_ADDRESS``.

.. py:function:: LiquidityGaugeV3.last_claim() -> uint256: view

    The epoch timestamp of the last call to claim from :func:`reward_contract<LiquidityGaugeV3.reward_contract>`.

Checking and Claiming Rewards
-----------------------------

.. note::

    Unlike ``LiquidityGaugeV2``, rewards are **not** automatically claimed each time a user performs an action on the gauge.

.. py:function:: LiquidityGaugeV3.claim_rewards(_addr: address = msg.sender, _receiver: address = ZERO_ADDRESS): nonpayable

    Claim all available reward tokens for ``_addr``. If no address is given, defaults to the caller. If the ``_receiver`` argument is provided rewards will be distributed to the address specified (caller must be ``_addr`` in this case). If the ``_receiver`` argument is not provided, rewards are sent to the default receiver for the account if one is set.

.. py:function:: LiquidityGaugeV3.claimed_reward(_addr: address, _token: address) -> uint256: view

    Get the number of already claimed reward tokens for a user.

.. py:function:: LiquidityGaugeV3.claimable_reward(_addr: address, _token: address) -> uint256: view

    Get the number of claimable reward tokens for a user

    .. note:: This call does not consider pending claimable amount in ``reward_contract``. Off-chain callers should instead use :func:`claimable_reward_write<LiquidityGaugeV3.claimable_reward_write>` as a view method.

.. py:function:: LiquidityGaugeV3.claimable_reward_write(_addr: address, _token: address) -> uint256: nonpayable

    Get the number of claimable reward tokens for a user. This function should be manually changed to "view" in the ABI. Calling it via a transaction will checkpoint a user's rewards updating the value of :func:`claimable_reward<LiquidityGaugeV3.claimable_reward>`. This function does not claim/distribute pending rewards for a user.

GaugeController
===============

``GaugeController`` is deployed to the Ethereum mainnet at:

    `0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB <https://etherscan.io/address/0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB>`_.

This is a fixed address, the contract cannot be swapped out or upgraded.

Source code for this contract is available on `Github <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/GaugeController.vy>`_.

Querying Gauge and Type Weights
-------------------------------

.. py:function:: GaugeController.gauge_types(gauge_addr: address) -> int128: view

    The gauge type for a given address, as an integer.

    Reverts if ``gauge_addr`` is not a gauge.

.. py:function:: GaugeController.get_gauge_weight(gauge_addr: address) -> uint256: view

    The current gauge weight for ``gauge_addr``.

.. py:function:: GaugeController.get_type_weight(type_id: int128) -> uint256: view

    The current type weight for ``type_id`` as an integer normalized to 1e18.

.. py:function:: GaugeController.get_total_weight() -> uint256: view

    The current total (type-weighted) weight for all gauges.

.. py:function:: GaugeController.get_weights_sum_per_type(type_id: int128) -> uint256: view

    The sum of all gauge weights for ``type_id``.

Vote-Weighting
--------------

Vote weight power is expressed as an integer in bps (units of 0.01%).  ``10000`` is equivalent to a 100% vote weight.

.. py:function:: GaugeController.vote_user_power(user: address) -> uint256: view

    The total vote weight power allocated by ``user``.

.. py:function:: GaugeController.last_user_vote(user: address, gauge: address) -> uint256: view

    Epoch time of the last vote by ``user`` for ``gauge``. A gauge weight vote may only be modified once every 10 days.

.. py:function:: GaugeController.vote_user_slopes(user: address, gauge: address) -> (uint256, uint256, uint256)

    Information about ``user``'s current vote weight for ``gauge``.

    Returns the current slope, allocated voting power, and the veCRV locktime end.

        .. code-block:: python

            >>> slope = gauge_controller.vote_user_slopes(alice, gauge)

            >>> slope['power']  # the current vote weight for this gauge
            4200

.. py:function:: GaugeController.vote_for_gauge_weights(_gauge_addr: address, _user_weight: uint256): nonpayable

    Allocate voting power for changing pool weights.

    * _gauge_addr Gauge which `msg.sender` votes for
    * _user_weight Weight for a gauge in bps (units of 0.01%). Minimal is 0.01%. Ignored if 0

        .. code-block:: python

            >>> gauge_controller = Contract("0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB")

            >>> gauge_controller.vote_for_gauge_weights(my_favorite_gauge, 10000, {'from': alice})
            Transaction sent: 0xc185d9194bd3c2faa791801ccc57ad4edcfcaff7b5dab1c9101b78cf978a8d7f
              Gas price: 20.0 gwei   Gas limit: 47442   Nonce: 26


Adding New Gauges and Types
---------------------------

All of the following methods are only be callable by the DAO :ref:`ownership admin<dao-ownership-agents>` as the result of a successful :ref:`vote<dao-voting>`.

.. py:function:: GaugeController.add_gauge(addr: address, gauge_type: int128): nonpayable

    Add a new gauge.

    * ``addr``: Address of the new gauge being added
    * ``gauge_type``: Gauge type

    .. note::

        Once a gauge has been added it cannot be removed. New gauges should be very carefully verified prior to adding them to the gauge controller.

.. py:function:: GaugeController.gauge_relative_weight(addr: address, time: uint256 = block.timestamp) -> uint256: view

    Get the relative the weight of a gauge  normalized to 1e18 (e.g. 1.0 == 1e18).

    Inflation which will be received by this gauge is calculated as ``inflation_rate * relative_weight / 1e18``.
    * ``addr``: Gauge address
    * ``time``: Epoch time to return a gauge weight for. If not given, defaults to the current block time.

.. py:function:: GaugeController.add_type(_name: String[64], weight: uint256 = 0): nonpayable

    Add a new gauge type.

    * ``_name``: Name of gauge type
    * ``weight``: Weight of gauge type

.. py:function:: GaugeController.change_type_weight(type_id: int128, weight: uint256)

    Change the weight for a given gauge type.

    Only callable by the DAO :ref:`ownership admin<dao-ownership-agents>`.

    * ``type_id`` Gauge type id
    * ``weight`` New Gauge weight

Minter
======

``Minter`` is deployed to the Ethereum mainnet at:

    `0xd061D61a4d941c39E5453435B6345Dc261C2fcE0 <https://etherscan.io/address/0xd061D61a4d941c39E5453435B6345Dc261C2fcE0>`_.

This is a fixed address, the contract cannot be swapped out or upgraded.

Source code for this contract is available on `Github <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/Minter.vy>`_.

Minting CRV
-----------

.. py:function:: Minter.mint(gauge_addr: address): nonpayable

    Mint allocated tokens for the caller based on a single gauge.

    * ``gauge_addr``: ``LiquidityGauge`` address to get mintable amount from

.. py:function:: Minter.mint_many(gauge_addrs: address[8]): nonpayable

    Mint CRV for the caller from several gauges.

    * ``gauge_addr``: A list of ``LiquidityGauge`` addresses to mint from. If you wish to mint from less than eight gauges, leave the remaining array entries as ``ZERO_ADDRESS``.

.. py:function:: Minter.mint_for(gauge_addr: address, for: address): nonpayable

    Mint tokens for a different address.

    In order to call this function, the caller must have been previously approved by ``for`` using :func:`toggle_approve_mint<Minter.toggle_approve_mint>`.

    * ``gauge_addr``: ``LiquidityGauge`` address to get mintable amount from
    * ``for``: address to mint for. The minted tokens are sent to this address, not the caller.

.. py:function:: Minter.toggle_approve_mint(minting_user: address): nonpayable

    Toggle approval for ``minting_user`` to mint CRV on behalf of the caller.

.. py:function:: Minter.allowed_to_mint_for(minter: address, for: address) -> bool: view

    Getter method to check if ``minter`` has been approved to call :ref:`mint_for<Minter.mint_for>` on behalf of ``for``.
