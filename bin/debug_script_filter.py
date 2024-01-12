# -*- coding: utf-8 -*-

import json
from automation.ops import path_bin_python, dir_workflow
from afwf_aws_resource_search.handlers import (
    search,
)
from rich import print as rprint

verbose = True
# verbose = False

handler = search.handler
query = ""

res = handler.run_script_command(path_bin_python, dir_workflow, query, verbose=verbose)
if res is None:
    print(f"res = {res}")
else:
    rprint(json.loads(res))
