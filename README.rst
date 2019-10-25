Docker-prepare
==============

Docker-prepare is a tool for generating Dockerfile from a combinaisons of templates

Note
----

This project is currently in development.

A better documentation and testing scripts will be added in the next release.

Quick start
-----------

.. code:: python

    # Installation
    pip install -U docker-prepare

.. code:: bash

    # Usage
    docker-prepare --input Dockertemplate --output Dockerfile
    docker-prepare --input Dockertemplate --output Dockerfile --env_file .env --env_file .env.local

::

    # Dockertemplate
    {% include "Dockertemplate.base" %}
    {% include "Dockertemplate.core" %}

Contributors
------------

-  `Javid Mougamadou <https://github.com/Javidjms>`__
