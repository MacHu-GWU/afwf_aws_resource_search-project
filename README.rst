
.. image:: https://readthedocs.org/projects/afwf-aws-resource-search/badge/?version=latest
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/afwf_aws_resource_search-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/afwf_aws_resource_search-project

.. image:: https://img.shields.io/pypi/v/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. image:: https://img.shields.io/pypi/l/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. image:: https://img.shields.io/pypi/pyversions/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/afwf-aws-resource-search#files


Welcome to ``afwf_aws_resource_search`` Documentation
==============================================================================
📔 See `Full Documentation HERE <https://afwf-aws-resource-search.readthedocs.io/index.html>`_.

Alfred Workflow that search AWS Resources and Open it in AWS Console.

This project is based on `aws_resource_search <https://github.com/MacHu-GWU/aws_resource_search-project>`_, A terminal application that enables interactive searches for AWS resources. It is a mini AWS console in your terminal or shell environment. It integrate Alfred Workflow with ``aws_resource_search``.

How to install it locally:

.. code-block:: bash

    $ git clone https://github.com/MacHu-GWU/afwf_aws_resource_search-project -b ${version} --depth 1
    $ cd awsfw_aws_resource_search-project
    $ pyops venv-create
    $ pyops install-all
    $ make build-wf
