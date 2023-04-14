.. _guide-code-style:

==========
Code Style
==========


Vyper Style Guide
=================

This document outlines the Vyper code style, structure and practices followed by the Curve development team.

Note that this guide is still under development. Do not hesitate to ask if anything is missing or unclear.

Project Organization
--------------------

Contracts should be structured so that components are logically grouped together. Maintaining a consistent order makes it easier for the reader to locate code.

Each logical section should be separated by two blank lines. Within each section, multi-line statements should be seperated by one blank line. Single-line statements should have no blank lines between them, except to denote a logical seperation.

Content should be ordered as follows:

1. `Import statements <https://vyper.readthedocs.io/en/stable/interfaces.html#importing-interfaces>`_
2. `Implements statements <https://vyper.readthedocs.io/en/stable/interfaces.html#implementing-an-interface>`_
3. `Inlined interfaces <https://vyper.readthedocs.io/en/stable/interfaces.html#declaring-and-using-interfaces>`_
4. `Events <https://vyper.readthedocs.io/en/stable/event-logging.html#declaring-events>`_
5. `Structs <https://vyper.readthedocs.io/en/stable/types.html#structs>`_
6. `Constants <https://vyper.readthedocs.io/en/stable/constants-and-vars.html#custom-constants>`_
7. `Storage variables <https://vyper.readthedocs.io/en/stable/structure-of-a-contract.html#state-variables>`_
8. `Constructor function <https://vyper.readthedocs.io/en/stable/control-structures.html#the-init-function>`_
9. `Fallback function <https://vyper.readthedocs.io/en/stable/control-structures.html#the-default-function>`_
10. `Regular functions <https://vyper.readthedocs.io/en/stable/control-structures.html#functions>`_

Imports and Interfaces
**********************

Contracts **must** be self contained. Import statements may only be used for built-in interfaces. Other interfaces are always inlined. This aids readability and simplifies the process of source verification on Etherscan.

Inlined interfaces should only include required functions (those that are called within the contract). Interfaces and the functions within should be sorted alphabetically. Each interface should be seperated by one blank line.

Events and Structs
******************

Events and structs should be sorted alphabetically. Each definition should be seperated by one blank line, with two blank lines between the last event and the first struct.

Constants and Storage Variables
*******************************

Constants should always be defined before storage variables, except when there is a logical reason to group them otherwise. Variable definitions should not be seperated by blank lines, but a single blank line can be used to create logical groupings.

Functions
*********

The constructor function must always be first, followed by the fallback function (if the contract includes one). Regular functions should be logically grouped. Each function should be seperated by two blank lines.


Naming Conventions
------------------

Names adhere to `PEP 8 <https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions>`_ naming conventions:

* **Events**, **interfaces** and **structs** use the CapWords convention.
* **Function** names are lowercase, with words separated by underscores when it improves readability. The only exception when adhering to a common interface such as ERC20.
* **Constants** use all capital letters with underscores separating words.
* **Variables** follow the same conventions as functions.

Leading Underscores
*******************

A single leading underscore marks an object as private or immutable.

* For functions, a leading underscore indicates that the function is internal.
* For variables, a leading underscore is used to indicate that the variable exists in calldata.

Booleans
********

* Boolean values **should** be prefixed with ``is_``.
* Booleans **must not** represent *negative* properties, (e.g. ``is_not_set``). This can result in double-negative evaluations which are not intuitive for readers.

Code Style
----------

As Vyper is syntactically similar to Python, all code **should** conform to the `PEP 8 <https://www.python.org/dev/peps/pep-0008>`_ style guide with the following exceptions:

* Maximum line length of 100

In general, we try to mimick the same linting process as would be applied by `black <https://github.com/psf/black/blob/master/docs/the_black_code_style.md>`_ if the code were Python.

Decorators
**********

Function decorators **should** be ordered according to `mutability <https://vyper.readthedocs.io/en/stable/control-structures.html#mutability>`_, `visibility <https://vyper.readthedocs.io/en/stable/control-structures.html#visibility>`_, `re-entrancy <https://vyper.readthedocs.io/en/stable/control-structures.html#re-entrancy-locks>`_:

.. code-block:: python

    @view
    @external
    @nonreentrant('lock')
    def foo():


Function Inputs
***************

All input variables **should** be prepended with a single leading underscore to denote their immutability. The only exception is if the variable name is a single letter (such as `i` and `j` for the swap contract exchange methods).

Where possible, the entire function signature should be kept on a single line:

.. code-block:: python

    def foo(_goo: address, _bar: uint256, _baz: uint256) -> bool:

If this line would exceed 100 characters, each input argument should instead be placed on a new line and indented:

.. code-block:: python

    def multiline_foo(
        _goo: address,
        _bar: uint256,
        _baz: uint256,
    ) -> bool:

Revert Strings
**************

Revert strings **must not** exceed a maximum length of 32 characters. They should only be used in functions that are expected to be frequently called by average users. For other situations you **should** use a `dev revert comment <https://eth-brownie.readthedocs.io/en/stable/tests-pytest-intro.html#developer-revert-comments>`_.


==================
Python Style Guide
==================

This document outlines the Python code style, structure and practices followed by the Curve development team.

Note that this guide is still under development. Do not hesitate to ask if anything is missing or unclear.

Linting and Pre-Commit Hooks
============================

We use `pre-commit <https://pre-commit.com/>`_ hooks to simplify linting and ensure consistent formatting among contributors. Use of ``pre-commit`` is not a requirement, but is highly recommended.

Install ``pre-commit`` locally from the brownie root folder:

.. code-block:: bash

    pip install pre-commit
    pre-commit install

Commiting will now automatically run the local hooks and ensure that your commit passes all lint checks.

Naming Conventions
------------------

Names **must** adhere to `PEP 8 naming conventions <https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions>`_:

* **Modules** have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
* **Class names** use the CapWords convention.
* **Exceptions** follow the same conventions as other classes.
* **Function** names are lowercase, with words separated by underscores when it improves readability.
* **Method** names and **instance** variables follow the same conventions as functions.
* **Constants** use all capital letters with underscores separating words.

Leading Underscores
*******************

A single leading underscore marks an object as private.

* Classes and functions with one leading underscore are only used in the module where they are declared. They **must not** be imported.
* Class attributes and methods with one leading underscore **must** only be accessed by methods within the same class.

Booleans
********

* Boolean values **should** be prefixed with ``is_``.
* Booleans **must not** represent *negative* properties, (e.g. ``is_not_set``). This can result in double-negative evaluations which are not intuitive for readers.
* Methods that return a single boolean **should** use the `@property` decorator.

Methods
*******

The following conventions **should** be used when naming functions or methods. Consistent naming provides logical consistency throughout the codebase and makes it easier for future readers to understand what a method does (and does not) do.

* ``get_``: For simple data retrieval without any side effects.
* ``fetch_``: For retreivals that may have some sort of side effect.
* ``build_``: For creation of a new object that is derived from some other data.
* ``set_``: For adding a new value or modifying an existing one within an object.
* ``add_``: For adding a new attribute or other value to an object. Raises an exception if the value already exists.
* ``replace_``: For mutating an object. Should return ``None`` on success or raise an exception if something is wrong.
* ``compare_``: For comparing values. Returns ``True`` or ``False``, does not raise an exception.
* ``validate_``: Returns ``None`` or raises an exception if something is wrong.
* ``from_``: For class methods that instantiate an object based on the given input data.

For other functionality, choose names that clearly communicate intent without being overly verbose. Focus on *what* the method does, not on *how* the method does it.

Code Style
----------

All code **must** conform to the `PEP 8 style guide <https://www.python.org/dev/peps/pep-0008>`_ with the following exceptions:

* Maximum line length of 100

We handle code formatting with `black <https://github.com/psf/black>`_. This ensures a consistent style across the project and saves time by not having to be opinionated.

Imports
*******

Import sequencing is handled with `isort <https://github.com/timothycrosley/isort>`_. We follow these additional rules:

Standard Library Imports
************************

Standard libraries **should** be imported absolutely and without aliasing. Importing the library aids readability, as other users may be familiar with that library.

.. code-block:: python

    # Good
    import os
    os.stat('.')

    # Bad
    from os import stat
    stat('.')

Strings
*******

Strings substitutions **should** be performed via `formatted string literals <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>`_ rather than the `str.format` method or other techniques.

