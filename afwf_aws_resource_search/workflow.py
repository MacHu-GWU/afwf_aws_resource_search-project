# -*- coding: utf-8 -*-

import afwf

from .handlers import (
    search,
)

wf = afwf.Workflow()
wf.register(search.handler)
