
.. .. image:: https://readthedocs.org/projects/afwf-aws-resource-search/badge/?version=latest
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/
    :alt: Documentation Status

.. .. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/actions?query=workflow:CI

.. .. image:: https://codecov.io/gh/MacHu-GWU/afwf_aws_resource_search-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/afwf_aws_resource_search-project

.. .. image:: https://img.shields.io/pypi/v/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. .. image:: https://img.shields.io/pypi/l/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. .. image:: https://img.shields.io/pypi/pyversions/afwf-aws-resource-search.svg
    :target: https://pypi.python.org/pypi/afwf-aws-resource-search

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project

------

.. .. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/

.. .. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://afwf-aws-resource-search.readthedocs.io/en/latest/py-modindex.html

.. .. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/issues

.. .. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/afwf-aws-resource-search#files


Welcome to ``afwf_aws_resource_search`` Documentation
==============================================================================
🌟 Alfred Workflow that search AWS Resources and Open it in AWS Console.

This project is based on `aws_resource_search <https://github.com/MacHu-GWU/aws_resource_search-project>`_, A terminal application that enables interactive searches for AWS resources. It is a mini AWS console in your terminal or shell environment. This project is just a wrapper to integrate ``aws_resource_search`` with Alfred Workflow.

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/1ca2e31f-2cf5-418c-bd07-7cf36b004307

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/6646f037-5dfc-4d3d-b4ec-469f7e7b984b

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/0c758626-3660-4b42-b88b-8ca532b5d66b


Installation
------------------------------------------------------------------------------
Go to `afwf_aws_resource_search Release <https://github.com/MacHu-GWU/afwf_aws_resource_search-project/releases>`_, download the latest version and double click to install. Then update the path to your Python interpreter in the workflow settings.

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/18021673-dc49-47db-a191-4c9df655bd48

**You can also build the workflow from source**

First, double click the downloaded workflow release to install it.

Then Run the following Command in sequence:

.. code-block:: bash

    # Clone the source code
    $ git clone https://github.com/MacHu-GWU/afwf_aws_resource_search-project -b ${version} --depth 1

    $ cd awsfw_aws_resource_search-project

    # Install dependencies in Virtualenv
    $ pyops venv-create
    $ pyops install-all

Then Go to your Alfred Workflow, Right Click on ``afwf_aws_resource_search`` Workflow, click ``Open in Finder``, copy the path of the workflow folder. Then go to the `bin/automation/ops.py <https://github.com/MacHu-GWU/afwf_aws_resource_search-project/blob/main/bin/automation/ops.py#L10>`_ file, update this line accordingly. So that the build system knows that where to build the workflow.

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/a55c0fa2-2454-40ef-8c22-fa43d5b5ca50

Then you can do:

.. code-block:: bash

    $ make build-wf

At the end, don't forget to update the path to your Python interpreter in the workflow settings.

.. image:: https://github.com/MacHu-GWU/afwf_aws_resource_search-project/assets/6800411/18021673-dc49-47db-a191-4c9df655bd48
