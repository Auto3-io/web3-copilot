.. image:: logo.svg
    :width: 480px
    :alt: Curve
    :align: center

|

`Curve <www.curve.fi>`_ is an exchange liquidity pool on Ethereum. Curve is designed for extremely efficient stablecoin trading and low risk, supplemental fee income for liquidity providers, without an opportunity cost.

This documentation outlines the technical implementation of the core Curve protocol and related smart contracts. It may be useful for contributors to the Curve codebase, third party integrators, or technically proficient users of the protocol.

Non-technical users may prefer the `Resources <https://resources.curve.fi/>`_ section of the main Curve website.

.. note::

    All code starting with ``$`` is meant to be run on your terminal. Code starting with ``>>>`` is meant to run inside the Brownie console.

.. note::

    This project relies heavily upon ``brownie`` and the documentation assumes a basic familiarity with it. You may wish to view the `Brownie documentation <https://eth-brownie.readthedocs.io/en/stable/>`_ if you have not used it previously.

Procotol Overview
=================

Curve can be broadly separated into the following categories:

* :ref:`StableSwap<exchange-overview>`: Exchange contracts and core functionality of the protocol
* The :ref:`DAO<dao-overview>`: Protocol governance and value accrual
* The :ref:`Factory<factory-overview>`: Permissionless deployment of Curve metapools
* The :ref:`Registry<registry-overview>`: Standardized API and on-chain resources to aid 3rd party integrations
