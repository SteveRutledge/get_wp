The get_wp Project
==============================

.. toctree::
    :hidden:
    :maxdepth: 1

    license
    reference

The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the get_wp project,
run this command in your terminal:

.. code-block:: console

   $ pip install get_wp


Usage
-----

get_wp's usage looks like:

.. code-block:: console

   $ get_wp [OPTIONS]

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
