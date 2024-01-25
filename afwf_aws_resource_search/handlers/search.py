# -*- coding: utf-8 -*-

"""
"""

import typing as T
import attrs
import afwf.api as afwf

from aws_resource_search.api import (
    preprocess_query,
    BaseSearcher,
    DetailItem,
    InfoItem,
    UrlItem,
    FileItem,
    ExceptionItem,
    AwsResourceItem,
    AwsResourceTypeItem,
    SetAwsProfileItem,
    ShowAwsInfoItem,
    handler as ui_handler,
    UI,
)
from aws_resource_search.ui_init import ui, ars

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


T_ARS_ITEM = T.Union[
    AwsResourceTypeItem,
    AwsResourceItem,
    DetailItem,
    InfoItem,
    UrlItem,
    FileItem,
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
        afwf_item = (
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
            .copy_id(item.get_id())
            .copy_name(item.get_name())
        )
        try:
            afwf_item.copy_arn(item.get_arn())
        except NotImplementedError:
            pass
        return afwf_item

    @classmethod
    def from_info_item(cls, item: InfoItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        )

    @classmethod
    def from_open_url_item(cls, item: UrlItem):
        return cls(
            title=item.title,
            subtitle=item.subtitle,
            uid=item.uid,
            icon=afwf.Icon.from_image_file(afwf.IconFileEnum.info),
        ).open_url(item.arg)

    @classmethod
    def from_open_file_item(cls, item: FileItem):
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
        elif isinstance(item, UrlItem):
            return cls.from_open_url_item(item)
        elif isinstance(item, FileItem):
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
