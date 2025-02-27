# developer: Taoshidev
# Copyright © 2023 Taoshi, LLC

from dataclasses import dataclass

from vali_objects.dataclasses.base_objects.base_dataclass import BaseDataClass


@dataclass
class ClientOutput(BaseDataClass):
    client_uuid: str
    stream_type: str
    topic_id: int
    request_uuid: str
    predictions: list[list[float]]
    additional_details: dict

    def __eq__(self, other):
        return self.equal_base_class_check(other)
