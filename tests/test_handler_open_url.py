# -*- coding: utf-8 -*-

from afwf_aws_resource_search.handlers.open_url import handler


def test():
    sf = handler.handler("")
    assert len(sf.items) == 3


if __name__ == "__main__":
    from afwf_aws_resource_search.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_resource_search.handlers.open_url", preview=False)
