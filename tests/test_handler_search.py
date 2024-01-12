# -*- coding: utf-8 -*-

from afwf_aws_resource_search.handlers.search import handler
from rich import print as rprint


def _test_search_resource_type_no_query():
    sf = handler.handler("")
    assert len(sf.items) >= 20


def _test_search_resource_type_good_query():
    sf = handler.handler("sfn")
    for item in sf.items:
        assert "sfn" in item.arg


def _test_search_resource_type_bad_query():
    sf = handler.handler("zyx")
    # for item in sf.items:
    #     assert "sfn" in item.arg


def _test_search_resource():
    # sf = handler.handler("ec2-security-group: ")
    sf = handler.handler("sfn-state-machine: ")
    # sf = handler.handler("dynamodb-table: ")
    # assert len(sf.items) >= 20


def test():
    # _test_search_resource_type_no_query()
    # _test_search_resource_type_good_query()
    # _test_search_resource_type_bad_query()

    _test_search_resource()


if __name__ == "__main__":
    from afwf_aws_resource_search.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_resource_search.handlers.search", preview=False)
