# -*- coding: utf-8 -*-

"""
"""

import typing as T
import attrs
import afwf.api as afwf

from aws_resource_search.res_lib import (
    preprocess_query,
    Searcher,
    DetailItem,
    InfoItem,
    OpenUrlItem,
    OpenFileItem,
)
from aws_resource_search.ui.boto_ses import bsm, ars
from aws_resource_search.ui.search_resource_type import (
    AwsResourceTypeItem,
    search_resource_type_and_return_items,
)
from aws_resource_search.ui.search_resource import (
    AwsResourceItem,
    search_resource_and_return_items,
)
from aws_resource_search.ui.main import terminal, UI, handler as ui_handler

from ..icons import resource_type_icon_mapper

try:
    from rich import print as rprint
except ImportError:
    pass


def get_icon_by_key(mapper: dict, key: str) -> T.Optional[afwf.Icon]:
    if key in mapper:
        return afwf.Icon.from_image_file(mapper[key])
    else:
        return None


ui = UI(
    handler=ui_handler,
    capture_error=False,
    terminal=terminal,
)

T_ARS_ITEM = T.Union[
    AwsResourceTypeItem,
    AwsResourceItem,
    DetailItem,
    InfoItem,
    OpenUrlItem,
    OpenFileItem,
]


@attrs.define
class Item(afwf.Item):
    def copy_arn(self, arn: str):
        self.variables["copy_arn"] = "y"
        self.variables["copy_arn_arg"] = arn
        return self

    def copy_id(self, id: str):
        self.variables["copy_id"] = "y"
        self.variables["copy_id_arg"] = id
        return self

    def copy_name(self, name: str):
        self.variables["copy_name"] = "y"
        self.variables["copy_name_arg"] = name
        return self

    @classmethod
    def from_aws_resource_type_item(cls, item: AwsResourceTypeItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            arg=item.arg,
            autocomplete=item.autocomplete,
            icon=get_icon_by_key(
                resource_type_icon_mapper, item.variables["resource_type"]
            ),
        )

    @classmethod
    def from_aws_resource_item(cls, item: AwsResourceItem):
        """
        .. note::

            The aws_resource_search cli allow user to use F1 to see detail,
            but we don't want to add this feature in alfred workflow.
            The zelfred framework allows us to use shortcut key to enter
            a sub-session, but sub-session in alfred is another script filter,
            which greatly increase the complexity.
        """
        return (
            cls(
                title=item.title,
                subtitle=item.subtitle,
                uid=item.uid,
                arg=item.variables["doc"].get_console_url(ars.aws_console),
                autocomplete=item.autocomplete,
                icon=get_icon_by_key(
                    resource_type_icon_mapper, item.variables["resource_type"]
                ),
            )
            .open_url(item.variables["doc"].get_console_url(ars.aws_console))
            .copy_arn(item.get_arn())
            .copy_id(item.get_id())
            .copy_name(item.get_name())
        )

    @classmethod
    def from_info_item(cls, item: InfoItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        )

    @classmethod
    def from_open_url_item(cls, item: OpenUrlItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        ).open_url(item.arg)

    @classmethod
    def from_open_file_item(cls, item: OpenFileItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        ).open_file(item.arg)

    @classmethod
    def from_detail_item(cls, item: DetailItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        ).open_file(item.arg)

    @classmethod
    def from_ars_item(cls, item: T_ARS_ITEM):
        if isinstance(item, AwsResourceTypeItem):
            return cls.from_aws_resource_type_item(item)
        elif isinstance(item, AwsResourceItem):
            return cls.from_aws_resource_item(item)
        elif isinstance(item, InfoItem):
            return cls.from_info_item(item)
        elif isinstance(item, OpenUrlItem):
            return cls.from_open_url_item(item)
        elif isinstance(item, OpenFileItem):
            return cls.from_open_file_item(item)
        elif isinstance(item, DetailItem):
            return cls.from_detail_item(item)
        else:
            raise TypeError(f"Unknown item type: {type(item)}")


@attrs.define
class Handler(afwf.Handler):
    def main(self, query: str):
        sf = afwf.ScriptFilter()
        items = ui.handler(query, ui, skip_ui=True)
        # rprint(items)
        afwf_items = [Item.from_ars_item(item) for item in items]
        # rprint(afwf_items)
        sf.items.extend(afwf_items)
        return sf

    def parse_query(self, query: str):
        return dict(query=query)


handler = Handler(id="search")
