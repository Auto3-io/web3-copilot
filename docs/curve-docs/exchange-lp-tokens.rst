.. _exchange-lp-tokens:

====================================
Curve StableSwap Exchange: LP Tokens
====================================

In exchange for depositing coins into a Curve pool (see :ref:`Curve Pools <exchange-pools>`), liquidity providers receive pool LP tokens. A Curve pool LP token is an ERC20 contract specific to the Curve pool. Hence, LP tokens are transferrable. Holders of pool LP tokens may stake the token into a pool's :ref:`liquidity gauge <dao-gauges>` in order to receive ``CRV`` token rewards. Alternatively, if the LP token is supported by a metapool, the token may be deposited into the respective metapool in exchange for the metapool's LP token (see :ref:`here <exchange-pools-meta>`).

The following versions of Curve pool LP tokens exist:

* `CurveTokenV1 <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_: LP token targetting Vyper `^0.1.0-beta.16 <https://vyper.readthedocs.io/en/stable/release-notes.html#v0-1-0-beta-16>`_
* `CurveTokenV2 <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_: LP token targetting Vyper `^0.2.0 <https://vyper.readthedocs.io/en/stable/release-notes.html#v0-2-1>`_
* `CurveTokenV3 <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_: LP token targetting Vyper `^0.2.0 <https://vyper.readthedocs.io/en/stable/release-notes.html#v0-2-1>`_ with gas optimizations

The version of each pool's LP token can be found in the :ref:`Deployment Addresses <addresses-overview>`.

.. note::
    For older Curve pools the ``token`` attribute is not always ``public`` and a getter has not been explicitly implemented.


Curve Token V1
==============

The implementation for a Curve Token V1 may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_.

.. py:function:: CurveToken.name() -> string[64]: view

    Get the name of the token.

    .. code-block:: python

        >>> lp_token.name()
        'Curve.fi yDAI/yUSDC/yUSDT/yBUSD'


.. py:function:: CurveToken.symbol() -> string[32]: view

    Get the token symbol.

    .. code-block:: python

        >>> lp_token.symbol()
        'yDAI+yUSDC+yUSDT+yBUSD'

.. py:function:: CurveToken.decimals() -> uint256: view

    Get the number of decimals for the token.

    .. code-block:: python

        >>> lp_token.decimals()
        18

.. py:function:: CurveToken.balanceOf(account: address) -> uint256: view

    Get the token balance for an account.

    * ``account``: Address to get the token balance for

    .. code-block:: python

        >>> lp_token.balanceOf("0x69fb7c45726cfe2badee8317005d3f94be838840")
        72372801850459006740117197


.. py:function:: CurveToken.totalSupply() -> uint256: view

    Get the total token supply.

    .. code-block:: python

        >>> lp_token.totalSupply()
        73112516629065063732935484


.. py:function:: CurveToken.allowance(_owner : address, _spender : address) -> uint256: view

    Get the allowance of an account to spend on behalf of some other account.

    * ``_owner``: Account that is paying when ``_spender`` spends the allowance
    * ``_spender``: Account that can spend up to the allowance

    Returns the allowance of ``_spender`` for ``_owner``.


.. py:function:: CurveToken.transfer(_to : address, _value : uint256) -> bool

    Transfer tokens to a specified address.

    * ``_to``: Receiver of the tokens
    * ``_value``: Amount of tokens to transfer

    Returns ``True`` if the transfer succeeded.


.. py:function:: CurveToken.transferFrom(_from : address, _to : address, _value : uint256) -> bool

    Transfer tokens from one address to another. Note that while this function emits a Transfer event, this is not required as per the specification, and other compliant implementations may not emit the event.

    * ``_from``: Address which you want to send tokens from
    * ``_to``: Address which you want to transfer to
    * ``_value``: Amount of tokens to be transferred

    Returns ``True`` if transfer succeeded.


.. py:function:: CurveToken.approve(_spender : address, _value : uint256) -> bool

    Approve the passed address to spend the specified amount of tokens on behalf of ``msg.sender``.

    Beware that changing an allowance with this method brings the risk that someone may use both the old and the new allowance by unfortunate transaction ordering. One possible solution to mitigate this race condition is to first reduce the spender's allowance to 0 and set the desired value afterwards (see this `GitHub issue <https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729>`_).

    * ``_spender``: Address which will spend the funds.
    * ``_value``: Amount of tokens to be spent.

    Returns ``True`` if approval succeeded.

    .. warning::
        For Curve LP Tokens V1 and V2, **non-zero to non-zero approvals are prohibited**. Instead, after every non-zero approval, the allowance for the spender **must** be reset to ``0``.


Minter Methods
--------------

The following methods are only callable by the ``minter`` (private attribute).

.. note::
    For Curve Token V1, the ``minter`` attribute is not ``public``.

.. py:function:: CurveToken.mint(_to: address, _value: uint256)

    Mint an amount of the token and assign it to an account. This encapsulates the modification of balances such that the proper events are emitted.

    * ``_to``: Address that will receive the created tokens
    * ``_value``: Amount that will be created


.. py:function:: CurveToken.burn(_value: uint256)

    Burn an amount of the token of ``msg.sender``.

    * ``_value``: Token amount that will be burned


.. py:function:: CurveToken.burnFrom(_to: address, _value: uint256)

    Burn an amount of the token from a given account.

    * ``_to``: Account whose tokens will be burned
    * ``_value``: Amount that will be burned


.. py:function:: CurveToken.set_minter(_minter: address)

    Set a new minter for the token.

    * ``_minter``: Address of the new minter


Curve Token V2
==============

The implementation for a Curve Token V2 may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_.

.. note::
    Compared to Curve Token v1, the following changes have been made to the API:

        * ``minter`` attribute is ``public`` and therefore a minter getter has been generated
        * ``name`` and ``symbol`` attributes can be set via ``set_name``
        * ``mint`` method returns ``bool``
        * ``burnFrom`` method returns ``bool``
        * ``burn`` method has been removed

.. warning::
    For Curve LP Tokens V1 and V2, **non-zero to non-zero approvals are prohibited**. Instead, after every non-zero approval, the allowance for the spender **must** be reset to ``0``.


.. py:function:: CurveToken.minter() -> address: view

    Getter for the address of the ``minter`` of the token.


.. py:function:: CurveToken.set_name(_name: String[64], _symbol: String[32])

    Set the name and symbol of the token.

    * ``_name``: New name of token
    * ``_symbol``: New symbol of token

    This method can only be called by ``minter``.


.. py:function:: CurveToken.mint(_to: address, _value: uint256) -> bool

    Mint an amount of the token and assign it to an account. This encapsulates the modification of balances such that the proper events are emitted.

    Returns ``True`` if not reverted.


.. py:function:: CurveToken.burnFrom(_to: address, _value: uint256) -> bool

    Burn an amount of the token from a given account.

    * ``_to``: Account whose tokens will be burned
    * ``_value``: Amount that will be burned

    Returns ``True`` if not reverted.


Curve Token V3
==============

The Curve Token V3 is more gas efficient than versions 1 and 2.

.. note::
    Compared to the Curve Token V2 API, there have been the following changes:

    * ``increaseAllowance`` and ``decreaseAllowance`` methods added to mitigate race conditions

The implementation for a Curve Token V3 may be viewed on `GitHub <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_.


.. py:function:: CurveToken.increaseAllowance(_spender: address, _added_value: uint256) -> bool

    Increase the allowance granted to ``_spender`` by the ``msg.sender``.

    This is alternative to ``approve`` that can be used as a mitigation for the potential race condition.

    * ``_spender``: Address which will transfer the funds
    * ``_added_value``: Amount of to increase the allowance

    Returns ``True`` if success.


.. py:function:: CurveToken.decreaseAllowance(_spender: address, _subtracted_value: uint256) -> bool

    Decrease the allowance granted to ``_spender`` by the ``msg.sender``.

    This is alternative to {approve} that can be used as a mitigation for the potential race condition.

    * ``_spender``: Address which will transfer the funds
    * ``_subtracted_value``: Amount of to decrease the allowance

    Returns ``True`` if success.
