# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_resource_type = Path.dir_here(__file__).joinpath("resource_type")
resource_type_icon_mapper = dict()
for p in dir_resource_type.select_by_ext(".png"):
    resource_type_icon_mapper[p.fname] = p.abspath
