.. _dao-vecrv:

============================
Curve DAO: Vote-Escrowed CRV
============================

Participating in Curve DAO governance requires that an account have a balance of vote-escrowed CRV (veCRV). veCRV is a non-standard ERC20 implementation, used within the Aragon DAO to determine each account's voting power.

veCRV is represented by the ``VotingEscrow`` contract, deployed to the Ethereum mainnet at:

    `0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2 <https://etherscan.io/address/0x5f3b5dfeb7b28cdbd7faba78963ee202a494e2a2>`_

veCRV cannot be transferred. The only way to obtain veCRV is by locking CRV. The maximum lock time is four years. One CRV locked for four years provides an initial balance of one veCRV.

A user's veCRV balance decays linearly as the remaining time until the CRV unlock decreases. For example, a balance of 4000 CRV locked for one year provides the same amount of veCRV as 2000 CRV locked for two years, or 1000 CRV locked for four years.

Implementation Details
======================

User voting power :math:`w_i` is linearly decreasing since the moment of lock. So does the total voting power :math:`W`. In order to avoid periodic check-ins, every time the user deposits, or withdraws, or changes the locktime, we record user's slope and bias for the linear function :math:`w_i(t)` in the public mapping ``user_point_history``. We also change slope and bias for the total voting power :math:`W(t)` and record it in ``point_history``. In addition, when a user's lock is scheduled to end, we schedule change of slopes of :math:`W(t)` in the future in ``slope_changes``. Every change involves increasing the ``epoch`` by 1.

This way we don't have to iterate over all users to figure out, how much should :math:`W(t)` change by, neither we require users to check in periodically. However, we limit the end of user locks to times rounded off by whole weeks.

Slopes and biases change both when a user deposits and locks governance tokens, and when the locktime expires. All the possible expiration times are rounded to whole weeks to make number of reads from blockchain proportional to number of missed weeks at most, not number of users (which is potentially large).

Querying Balances, Locks and Supply
===================================

.. py:function:: VotingEscrow.balanceOf(addr: address, _t: uint256 = block.timestamp) -> uint256

    Get the current voting power for an address.

    * ``addr``: User wallet address

        .. code-block:: python

            >>> vote_escrow = Contract('0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2')

            >>> vote_escrow.balanceOf('0xF89501B77b2FA6329F94F5A05FE84cEbb5c8b1a0')
            5464191329389144503333564

.. py:function:: VotingEscrow.balanceOfAt(addr: address, _block: uint256) -> uint256

    Measure the voting power of an address at a historic block height.

    This function is taken from the `MiniMe <https://github.com/Giveth/minime>`_ ERC20 implementation and is required for compatibility with Aragon.

    * ``addr``: User wallet address
    * ``_block``: Block to calculate the voting power at

        .. code-block:: python

            >>> height = len(chain) - 10000  # ten thousand blocks prior to the current block
            >>> vote_escrow.balanceOfAt('0xF89501B77b2FA6329F94F5A05FE84cEbb5c8b1a0', height)
            5470188311017698310628752

.. py:function:: VotingEscrow.totalSupply() -> uint256

    Calculate the current total voting power.

        .. code-block:: python

            >>> vote_escrow.totalSupply()
            102535077684041114817306735

.. py:function:: VotingEscrow.totalSupplyAt(_block: uint256) -> uint256

    Calculate the total voting power at a historic block height.

    * ``_block`` Block to calculate the total voting power at.

        .. code-block:: python

            >>> height = len(chain) - 10000  # ten thousand blocks prior to the current block
            >>> vote_escrow.totalSupplyAt(height)
            101809514082846807874928588

.. py:function:: VotingEscrow.locked(_user: address) -> (int128, uint256)

    Get information about the current CRV lock for an address.

    * ``_user``: Address to query.

    Returns amount of CRV currently locked, and the epoch time that the lock expires.

        .. code-block:: python

            >>> vote_escrow.locked('0xF89501B77b2FA6329F94F5A05FE84cEbb5c8b1a0').dict()
            {
                'amount': 5664716612269392397633736,
                'end': 1736985600
            }

Working with Vote-Locks
=======================

.. py:function:: VotingEscrow.create_lock(_value: uint256, _unlock_time: uint256)

    Deposit CRV into the contract and create a new lock.

    Prior to calling this function, the contract must be approved to transfer at least ``_value`` CRV. A new lock cannot be created when an existing lock already exists.

    * ``_value``: The amount of CRV to deposit.
    * ``_unlock_time`` Epoch time when tokens unlock. This value is rounded down to the nearest whole week. The maximum duration for a lock is four years.

        .. code-block:: python

            >>> import time
            >>> crv = Contract('0xd533a949740bb3306d119cc777fa900ba034cd52')
            >>> vote_escrow = Contract('0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2')

            >>> crv.approve(vote_escrow, 2**256-1, {'from': alice})
            Transaction sent: 0xa7978a8d7fc185d9194bd3c2fa1801ccc57ad4edcfcaff7b5dab1c9101b78cf9
              Gas price: 20.0 gwei   Gas limit: 56299   Nonce: 23


            >>> amount = crv.balanceOf(alice)
            >>> unlock_time = int(time.time() + 86400 * 365 * 4)
            >>> vote_escrow.create_lock(amount, unlock_time, {'from': alice})
            Transaction sent: 0xa7978a8d7fc185d9194bd3c2fa1801ccc57ad4edcfcaff283958329291b78cf1
              Gas price: 20.0 gwei   Gas limit: 307234   Nonce: 24

.. py:function:: VotingEscrow.increase_amount(_value: uint256)

    Deposit additional CRV into an existing lock.

    * ``_value``: The amount of CRV to deposit.

        .. code-block:: python

            >>> amount = crv.balanceOf(alice)
            >>> vote_escrow.increase_amount(amount, {'from': alice})
            Transaction sent: 0xa7978a8d7fc185d9194bd3c2fa1801ccc57ad4edcfcaff7b5dab1c9101b78cf9
              Gas price: 20.0 gwei   Gas limit: 156299   Nonce: 24

.. py:function:: VotingEscrow.increase_unlock_time(_unlock_time: uint256)

    Extend the unlock time on a lock that already exists.

    * ``_unlock_time`` New epoch time for unlocking. This value is rounded down to the nearest whole week. The maximum duration for a lock is four years.

        .. code-block:: python

            >>> unlock_time = int(time.time() + 86400 * 365 * 4)
            >>> vote_escrow.increase_unlock_time(unlock_time, {'from': alice})
            Transaction sent: 0xa7978a8d7fc185d9194bd3c2fa1801ccc57ad4edcfcaff7b5dab1c9101b78cf9
              Gas price: 20.0 gwei   Gas limit: 282041   Nonce: 24

.. py:function:: VotingEscrow.withdraw()

    Withdraw deposited CRV tokens once a lock has expired.

        .. code-block:: python

            >>> vote_escrow.withdraw({'from': alice})
            Transaction sent: 0xa7978a8d7fc185d9194bd3c2fa1801ccc57ad4edcfcaff7b5dab1c9101b78cf9
              Gas price: 20.0 gwei   Gas limit: 178629   Nonce: 24
