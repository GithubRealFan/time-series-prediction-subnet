from dataclasses import dataclass

from vali_objects.dataclasses.base_objects.base_dataclass import BaseDataClass


@dataclass
class PredictionOutput(BaseDataClass):
    client_uuid: str
    stream_type: int
    topic_id: int
    request_uuid: str
    predictions: list[list[float]]

    def __eq__(self, other):
        return self.equal_base_class_check(other)
