.. _glossary:

=================
Glossary of Terms
=================

This glossary of terms contains definitions of commonly used terms within the Curve documentation.

This section is a work in progress - if a term is missing, feel free to `open a pull request <https://github.com/curvefi/curve-docs>`_ to add it.

.. _glossary-amm:

Automated Market Maker (AMM)
    A decentralized asset trading pool that allows participants to buy or sell cryptocurrencies.

Base Pool
    The pool issuing the LP token that is used by a metapool.

Burning
    The process of withdrawing admin fees from the excahange contracts and distributing them to veCRV holders.

ERC20
    A technical standard for implementing tokens within Ethereum. Often used interchangeably with the term token. The standard is viewable `here <https://eips.ethereum.org/EIPS/eip-20>`_.

LP Token
    Short for Liquidity Provider token. An ER20 token which represents a deposit into a Curve exchange contract, or other :ref:`AMM<glossary-amm>`.

.. _glossary-metapool:

Metapool
    A Curve pool where one of the tradeable assets is the :ref:`LP token<glossary-metapool>` for another pool (base pool). Metapools are used to prevent liquidity fragmentation.

.. _glossary-underlying-coin:

Pool
    See :ref:`automated market maker<glossary-amm>`.

Synth
    Short for "synthetic asset" - a derivative which tracks the price of another asset, offering exposure to price movements without requiring the user to hold the actual asset.

Underlying Coin
    An ERC20 token that has been deposited into a protocol and where the deposit is represented by another token. The other token (the ":ref:`wrapped coin<glossary-wrapped-coin>`") may be used to claim back this original token.

veCRV
    Short for "vote-escrowed CRV". CRV that has been locked in the :ref:`voting contract<dao-voting>`.

.. _glossary-wrapped-coin:

Wrapped Coin
    An ERC20 token used to represent the deposit of another token within a protocol. The original token has been "wrapped" in this new token. The originial token is referred to as the ":ref:`underlying coin<glossary-underlying-coin>`".
