# -*- coding: utf-8 -*-

from afwf_aws_resource_search.workflow import wf
from afwf_aws_resource_search.handlers import (
    search,
)
from rich import print as rprint


def test():
    sf = wf._run(arg=f"{search.handler.id} s3")


if __name__ == "__main__":
    from afwf_aws_resource_search.tests import run_cov_test

    run_cov_test(__file__, "afwf_aws_resource_search.workflow", preview=False)
