.. _cross-asset-swaps:

=================
Cross Asset Swaps
=================

Curve integrates with Synthetix to allow large scale swaps between different asset classes with minimal slippage. Utilizing Synthetix' zero-slippage synth conversions and Curve's deep liquidity and low fees, we can perform fully on-chain cross asset swaps at scale with a 0.38% fee and minimal slippage.

Cross asset swaps are performed using the ``SynthSwap`` contract, deployed to the mainnet at the following address:

    `0x58A3c68e2D3aAf316239c003779F71aCb870Ee47 <https://etherscan.io/address/0x58A3c68e2D3aAf316239c003779F71aCb870Ee47#code>`_

Source code and information on the technical implementation are available on `Github <https://github.com/curvefi/curve-cross-asset-swaps>`_.

How it Works
============

As an example, suppose we have asset ``A`` and wish to exchange it for asset ``D``. For this swap to be possible, ``A`` and ``D`` must meet the following requirements:

* Must be of different asset classes (e.g. USD, EUR, BTC, ETH)
* Must be exchangeable for a Synthetic asset within one of Curve's pools (e.g. sUSD, sBTC)

The swap can be visualized as ``A -> B -> C | C -> D``:

    1. The initial asset ``A`` is exchanged on Curve for ``B``, a synth of the same asset class.
    2. ``B`` is converted to ``C``, a synth of the same asset class as ``D``.
    3. A `settlement period <https://docs.synthetix.io/integrations/settlement/>`_ passes to account for sudden price movements between ``B`` and ``C``.
    4. Once the settlement period has passed, ``C`` is exchanged on Curve for the desired asset ``D``.

Settler NFTs
------------

Swaps cannot occur atomically due to the Synthetix settlement period. Each unsettled swap is represented by an :ref:`ERC721 <https://eips.ethereum.org/EIPS/eip-721>` non-fungible token.

* Each NFT has a unique token ID. Token IDs are never re-used. The NFT is minted upon initiating the swap and burned when the swap is completed.
* The NFT, and associated right to claim, is fully transferable. It is not possible to transfer the rights to a partial claim. The approved operator for an NFT also has the right to complete the swap with the underlying asset.
* Token IDs are not sequential. This contract does not support the enumerable ERC721 extension. This decision is based on gas efficiency.

Front-running Considerations
----------------------------

The benefits from these swaps are most apparent when the exchange amount is greater than $1m USD equivalent. As such, the initiation of a swap gives a strong indicator other market participants that a 2nd post-settlement swap will be coming. We attempt to minimize the risks from this in several ways:

* ``C -> D`` is not declared on-chain when performing the swap from ``A -> C``.
* It is possible to perform a partial swap from ``C -> D``, and to swap into multiple final assets. The NFT persists until it has no remaining underlying balance of ``C``.
* There is no fixed time frame for the second swap. A user can perform it immediately or wait until market conditions are more favorable.
* It is possible to withdraw ``C`` without performing a second swap.
* It is possible to perform additional ``A -> B -> C`` swaps to increase the balance of an already existing NFT.

The range of available actions and time frames make it significantly more difficult to predict the outcome of a swap and trade against it.

.. _cross-asset-swaps-api:

Exchange API
============

Finding Swappable Assets
------------------------

In general, any asset that is within a Curve pool also containing a Synth may be used in a cross asset swap. You can use the following view methods to confirm whether or not an asset is supported:

.. py:function:: StableSwap.synth_pools(_synth: address) -> address: view

    Get the address of the Curve pool used to swap a synthetic asset.

    If this function returns ``ZERO_ADDRESS``, the given synth cannot be used within cross-asset swaps.

.. py:function:: StableSwap.swappable_synth(_token: address) -> address: view

    Get the address of the synthetic asset that ``_token`` may be directly swapped for.

    If this function returns ``ZERO_ADDRESS``, the given token cannot be used within a cross-asset swap.

        .. code-block:: python

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> dai = Contract('0x6b175474e89094c44da98b954eedeac495271d0f')

            >>> synth_swap.swappable_synth(dai)  # returns sUSD
            '0x57Ab1ec28D129707052df4dF418D58a2D46d5f51'

            >>> synth_swap.synth_pools('0x57ab1ec28d129707052df4df418d58a2d46d5f51')  # returns Curve sUSD pool
            '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD'

Estimating Swap Amounts
-----------------------

.. py:function:: StableSwap.get_swap_into_synth_amount(_from: address, _synth: address, _amount: uint256) -> uint256: view

    Return the amount received when performing a cross-asset swap.

    This method is used to calculate ``_expected`` when calling :func:`swap_into_synth<StableSwap.swap_into_synth>`. You should reduce the value slightly to account for market movement prior to the transaction confirming.

    * ``_from``: Address of the initial asset being exchanged.
    * ``_synth``: Address of the synth being swapped into.
    * ``_amount``: Amount of `_from` to swap.

    Returns the expected amount of ``_synth`` received in the swap.

        .. code-block:: python

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> dai = Contract('0x6b175474e89094c44da98b954eedeac495271d0f')
            >>> sbtc = Contract('0xfe18be6b3bd88a2d2a7f928d00292e7a9963cfc6')

            >>> synthswap.get_swap_into_synth_amount(dai, sbtc, 100000 * 1e18)
            2720559215249173192

.. py:function:: StableSwap.get_swap_from_synth_amount(_synth: address, _to: address, _amount: uint256) -> uint256: view

    Return the amount received when swapping out of a settled synth.

    This method is used to calculate ``_expected`` when calling :func:`swap_from_synth<StableSwap.swap_from_synth>`. You should reduce the value slightly to account for market movement prior to the transaction confirming.

    * ``_synth``: Address of the synth being swapped out of.
    * ``_to``: Address of the asset to swap into.
    * ``_amount``: Amount of ``_synth`` being exchanged.

    Returns the expected amount of `_to` received in the swap.

        .. code-block:: python

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> sbtc = Contract('0xfe18be6b3bd88a2d2a7f928d00292e7a9963cfc6')
            >>> wbtc = Contract('0x2260fac5e5542a773aa44fbcfedf7c193bc2c599')

            >>> synthswap.get_swap_from_synth_amount(sbtc, wbtc, 2720559215249173192)
            273663013

.. py:function:: StableSwap.get_estimated_swap_amount(_from: address, _to: address, _amount: uint256) -> uint256: view

    Estimate the final amount received when swapping between ``_from`` and ``_to``.

    Note that the actual received amount may be different due to rate changes during the settlement period.

    * ``_from``: Address of the initial asset being exchanged.
    * ``_to``: Address of the asset to swap into.
    * ``_amount``: Amount of `_from` being exchanged.

    Returns the estimated amount of `_to` received.

        .. code-block:: python

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> dai = Contract('0x6b175474e89094c44da98b954eedeac495271d0f')
            >>> wbtc = Contract('0x2260fac5e5542a773aa44fbcfedf7c193bc2c599')

            >>> synthswap.get_estimated_swap_amount(dai, wbtc, 100000 * 1e18)
            273663013

    .. note::

        This method is for estimating the received amount from a complete swap over two transactions. If ``_to`` is a Synth, you should use :func:`get_swap_into_synth_amount<StableSwap.get_swap_from_synth_amount>` instead.

Initiating a Swap
-----------------

All cross asset swaps are initiated with the following method:

.. py:function:: StableSwap.swap_into_synth(_from: address, _synth: address, _amount: uint256, _expected: uint256, _receiver: address = msg.sender, _existing_token_id: uint256 = 0) -> uint256: payable

    Perform a cross-asset swap between ``_from`` and ``_synth``.

    Synth swaps require a `settlement time <https://docs.synthetix.io/integrations/settlement/>`_ to complete and so the newly generated synth cannot immediately be transferred onward. Calling this function mints an NFT representing ownership of the unsettled synth.

    * ``_from``: Address of the initial asset being exchanged. For Ether swaps, use ``0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE``.
    * ``_synth``: Address of the synth being swapped into.
    * ``_amount``: Amount of ``_from`` to swap. If you are swapping from Ether, you must also send exactly this much Ether with the transaction. If you are swapping any other asset, you must have given approval to the swap contract to transfer at least this amount.
    * ``_expected``: Minimum amount of ``_synth`` to receive.
    * ``_receiver``: Address of the recipient of ``_synth``, if not given, defaults to the caller.
    * ``_existing_token_id``: Token ID to deposit ``_synth`` into. If not given, a new NFT is minted for the generated synth. When set as non-zero, the token ID must be owned by the caller and must already represent the same synth as is being swapped into.

    Returns the ``uint256`` token ID of the NFT representing the unsettled swap. The token ID is also available from the emitted ``TokenUpdate`` event.

        .. code-block:: python

            >>> alice = accounts[0]

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> dai = Contract('0x6b175474e89094c44da98b954eedeac495271d0f')
            >>> sbtc = Contract('0xfe18be6b3bd88a2d2a7f928d00292e7a9963cfc6')

            >>> expected = synth_swap.get_swap_into_synth_amount(dai, sbtc, dai.balanceOf(alice)) * 0.99

            >>> tx = synth_swap.swap_into_synth(dai, sbtc, expected, {'from': alice})
            Transaction sent: 0x83b311af19be08b8ec6241c3e834ccdf3b22586971de82a76a641e43bdf2b3ee
              Gas price: 20 gwei   Gas limit: 1200000   Nonce: 5

            >>> tx.events['TokenUpdate']['token_id']
            2423994707895209386239865227163451060473904619065

Getting Info about an Unsettled Swap
------------------------------------

.. py:function:: StableSwap.token_info(_token_id: uint256) -> address, address, uint256, uint256: view

    Get information about the underlying synth represented by an NFT.

    * ``_token_id``: NFT token ID to query info about. Reverts if the token ID does not exist.

    Returns the owner of the NFT, the address of the underlying synth, the balance of the underlying synth, and the current maximum number of seconds until the synth may be settled.

        .. code-block:: python

            >>> synth_swap = Contract('0x58A3c68e2D3aAf316239c003779F71aCb870Ee47')
            >>> synthswap.token_info(2423994707895209386239865227163451060473904619065).dict()
            {
                'owner': "0xEF422dBBF46120dE627fFb913C9AFaD44c735618",
                'synth': "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51",
                'time_to_settle': 0,
                'underlying_balance': 1155647333395694644849
            }

Completing a Swap
-----------------

Once the settlement period on a swap has finished, any of the following methods may be used to complete the swap.

.. py:function:: StableSwap.swap_from_synth(_token_id: uint256, _to: address, _amount: uint256, _expected: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Swap the underlying synth represented by an NFT into another asset.

    Callable by the owner or operator of ``_token_id`` after the synth settlement period has passed. If ``_amount`` is equal to the total remaining balance of the synth represented by the NFT, the NFT is burned.

    * ``_token_id``: The identifier for an NFT.
    * ``_to``: Address of the asset to swap into.
    * ``_amount``: Amount of the underlying synth to swap.
    * ``_expected``: Minimum amount of ``_to`` to receive.
    * ``_receiver``: Address to send the final received asset to. If not given, defaults to the caller.

    Returns the remaining balance of the underlying synth within the active NFT.

        .. code-block:: python

            >>> wbtc = Contract('0x2260fac5e5542a773aa44fbcfedf7c193bc2c599')

            >>> amount = synth_swap.token_info(token_id)['underlying_balance']
            >>> expected = swynth_swap.get_swap_from_synth_amount(sbtc, wbtc, amount) * 0.99

            >>> synth_swap.swap_from_synth(token_id, wbtc, amount, expected, {'from': alice})
            Transaction sent: 0x83b311af19be08b8ec6241c3e834ccdf3b22586971de82a76a641e43bdf2b3ee
              Gas price: 20 gwei   Gas limit: 800000   Nonce: 6

.. py:function:: StableSwap.withdraw(_token_id: uint256, _amount: uint256, _receiver: address = msg.sender) -> uint256: nonpayable

    Withdraw the underlying synth represented by an NFT.

    Callable by the owner or operator of ``_token_id`` after the synth settlement period has passed. If ``_amount`` is equal to the total remaining balance of the synth represented by the NFT, the NFT is burned.

    * ``_token_id``: The identifier for an NFT.
    * ``_amount``: Amount of the underlying synth to withdraw.
    * ``_receiver``: Address of the recipient of the withdrawn synth. If not given, defaults to the caller.

    Returns the remaining balance of the underlying synth within the active NFT.

        .. code-block:: python

            >>> amount = synth_swap.token_info(token_id)['underlying_balance']

            >>> synth_swap.withdraw(token_id, amount, {'from': alice})
            Transaction sent: 0x83b311af19be08b8ec6241c3e834ccdf3b22586971de82a76a641e43bdf2b3ee
              Gas price: 20 gwei   Gas limit: 800000   Nonce: 6

.. py:function:: StableSwap.settle(_token_id: uint256) -> bool: nonpayable

    Settle the synth represented in an NFT. Note that settlement is performed when swapping or withdrawing, there is no requirement to call this function separately.

    * ``_token_id`` The identifier for an NFT.

    Returns ``True``.
