.. _guide-testing.rst:

=======
Testing
=======

Curve development follows a strong testing methodology. While testing Ethereum-based protocols can be challenging, the Curve test suite is a powerful tool that shall be used by contributors to help facilitate this task. While the repositories ``curve-contract``, ``curve-dao-contracts`` and ``curve-pool-registry`` are all stand alone repositories where each repo employs its own test suite, the test suite designs are very similar.

This section outlines how the test suite should be used most effectively for the ``curve-contracts`` repository.

Curve Contracts
===============

Test cases for Curve pools are organized across the following `subdirectories <https://github.com/curvefi/curve-contract/tree/master/tests>`_:

    * ``forked``: Tests designed for use in a forked mainnet
    * ``fixtures``: `Pytest fixtures <https://docs.pytest.org/en/latest/fixture.html>`_
    * ``pools``: Tests for pool contracts
    * ``token``: Tests for LP token contracts
    * ``zaps``: Tests for deposit contracts

Other files:

* `conftest.py <https://github.com/curvefi/curve-contract/blob/master/tests/conftest.py>`_: Base configuration file for the test suite.
* `simulation.py <https://github.com/curvefi/curve-contract/blob/master/tests/simulation.py>`_: A python model of the math used within Curve's contracts. Used for testing expected outcomes with actual results.

Organization
------------

    * Tests are organized by general category, then split between unitary and integration tests.
    * Common tests for all pools are located in ``tests/pools/common``, for zaps in ``tests/zaps/common``.
    * Common metapool tests are located at ``tests/pools/meta``, for zaps in ``tests/zaps/meta``.
    * Valid pool names are the names of the subdirectories within ``contracts/pools``.
    * For pool templates, prepend ``template-`` to the subdirectory names within ``contracts/pool-templates``. For example, the base template is ``template-base``.

Pool Type Tests
***************

Note that the test suite targets tests also on a *pool type* basis. A Curve pool may be of one or more types. The supported pool types are:

* ``arate``: These are ``aToken``-style pools (interest accrues as balance increases)
* ``crate``: These are ``cToken``-style pools (interest accrues as rate increases)
* ``eth``: These are pools that have ``ETH`` as one of their tokens
* ``meta``: These are metapools

An example of a pool of a single type would be the ``aave`` pool, which is of type ``arate``.

An example of a pool of multiple types would be the ``steth`` pool, which is of the types ``eth`` and ``arate``.


The type of a pool is given by the key value pair ``"pool_types": [<POOL_TYPE>, ...]`` in a pool's ``pooldata.json`` file. If no type is specified, the pool is by default a ``template-base``-style pool.When running tests, the test suit targets pool type-specific tests if they exist. To add a pool type-specific test, place the new test into the *pool type subdirectory* (e.g., `meta` for metapool tests).

Pool-specific Tests
*******************

There may be pools for which it is required to write multiple tests, which are not applicable to other pools. Rather than using decorators to *skip* (see below) other pools on an individual or type basis, a new subdirectory **named after the pool** can be created to contain the pool-specific tests.

When the test suite is started, for a given pool, all tests for the pool's type get run, as well as any existing pool-specific tests.

For example, assuming there exists a new metapool called ``foo``, specifying ``"pool_types": ["meta"]`` in the pool's ``pooldata.json`` would ensure that all metapool tests get run. Let's assume there is a token in the pool, which has behavior that is currently not captured by any of the ``meta`` or ``common`` tests that get currently run for the ``foo`` pool. To ensure we test the ``foo`` pool's behavior thoroughly, new tests should be created and added in a newly created ``tests/pools/foo/`` subdirectory.


Running the tests
-----------------

To run the entire suite:

.. code-block:: bash

    brownie test

Note that this executes over 10,000 tests and may take a significant amount of time to finish.

Test Collection Filters
***********************

The test suite is divided into several logical categories. Tests may be filtered using one or more flags:

* ``--pool <POOL NAME>``: only run tests against a specific pool
* ``--integration``: only run integration tests (tests within an ``integration/`` subdirectory)
* ``--unitary``: only run unit tests (tests NOT found in an ``integration/`` subdirectory)

For example, to only run the unit tests for 3pool:

.. code-block:: bash

    brownie test --pool 3pool --unitary

Testing against a forked mainnet
********************************

To run the test suite against a forked mainnet:

.. code-block:: bash

    brownie test --network mainnet-fork

In this mode, the actual underlying and wrapped coins are used for testing. Note that forked mode can be *very slow*, especially if you are running against a public node.

Fixtures
--------

Test fixtures are located within the `tests/fixture <https://github.com/curvefi/curve-contract/tree/master/tests/fixtures>`_ subdirectory. New fixtures should be added here instead of within the base `conftest.py <https://github.com/curvefi/curve-contract/blob/master/tests/conftest.py>`_.

All fixtures are [documented](fixtures/README.md) within the fixtures subdirectory readme.

Markers
-------

We use the following custom `markers <https://docs.pytest.org/en/stable/example/markers.html>`_ to parametrize common tests across different pools:

``skip_pool(*pools)``
*********************

Exclude one or more pools from the given test.

.. code-block:: python

    @pytest.mark.skip_pool("compound", "usdt", "y")
    def test_only_some_pools(swap):
        ...


``skip_pool_type(*pool_types)``
*******************************

Exclude specific pool types from the given test.

.. code-block:: python

    @pytest.mark.skip_pool_type("meta", "eth")
    def test_not_metapools(swap):
        ...


``target_pool(*pools)``
***********************

Only run the given test against one or more pools specified in the marker.

.. code-block:: python

    @pytest.mark.target_pool("ren", "sbtc")
    def test_btc_pools(swap):
        ...


``skip_meta``
*************

Exclude metapools from the given test.

.. code-block:: python

    @pytest.mark.skip_meta
    def test_not_metapools(swap):
        ...

``lending``
***********

Only run the given test against pools that involve lending.

.. code-block:: python

    @pytest.mark.lending
    def test_underlying(swap):
        ...

``zap``
*******

Only run the given test against pools that use a deposit contract.

.. code-block:: python

    @pytest.mark.zap
    def test_deposits(zap):
        ...

``itercoins(*arg, underlying=False)``
*************************************

Parametrizes each of the given arguments with a range of numbers equal to the total number of coins for the given pool. When multiple arguments are given, each argument has a unique value for every generated test.

For example, ``itercoins("send", "recv")`` with a pool of 3 coins will parametrize with the sequence ``[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]``.

If ``underlying`` is set as ``True``, the upper bound of iteration corresponds to the true number of underlying coins. This is useful when testing metapools.

.. code-block:: python

    @pytest.mark.itercoins("send", "recv"):
    def test_swap(accounts, swap, send, recv):
        swap.exchange(send, recv, 0, 0, {'from': accounts[0]})
