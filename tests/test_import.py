# -*- coding: utf-8 -*-

import os
import pytest
import afwf_aws_resource_search


def test_import():
    _ = afwf_aws_resource_search.wf


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
