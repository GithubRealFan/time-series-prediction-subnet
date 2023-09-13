# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Taoshi
# Copyright © 2023 TARVIS Labs, LLC

from dataclasses import dataclass, fields
from typing import Optional

import numpy as np


@dataclass
class BaseDataClass:

    def __post_init__(self):
        self.schema_integrity_check()

    def equal_base_class_check(self, other):
        if not isinstance(other, BaseDataClass):
            return False
        fields_list = fields(self)
        # Compare all fields for equality
        for field in fields_list:
            field_name = field.name
            field_value_self = getattr(self, field_name)
            field_value_other = getattr(other, field_name)

            if isinstance(field_value_self, np.ndarray):
                # Compare NumPy arrays using np.array_equal()
                if not np.array_equal(field_value_self, field_value_other):
                    return False
                # for elem1, elem2 in zip(field_value_self, field_value_other):
                #     if isinstance(elem1, np.ndarray) and isinstance(elem2, np.ndarray):
                #         if not np.array_equal(elem1, elem2):
                #             return False
                #     elif elem1 != elem2:
                #         return False
            elif field_value_self != field_value_other:
                return False
        return True

    def schema_integrity_check(self):
        def t_list_check(f, f_t):
            if f_t == int or f_t == float:
                pass
            else:
                raise TypeError(f"The field `{f.name}` was assigned by `{f_t}` instead of int or float")

        for field in fields(type(self)):
            if field.type == Optional[list[float]] \
                    or field.type == list[float] \
                    or field.type == list[int]:
                if getattr(self, field.name) is not None:
                    t_list_check(field, type(getattr(self, field.name)[0]))
            elif field.type == list[list[float]]:
                if getattr(self, field.name) is not None:
                    t_list_check(field, type(getattr(self, field.name)[0][0]))
            elif field.type == dict[str, list[float]] \
                    or field.type == dict[str, list[int]]:
                if getattr(self, field.name) is not None:
                    if type(getattr(self, field.name)) != dict:
                        raise TypeError(f"The field `{field.name}` was "
                                        f"assigned by `{type(getattr(self, field.name))}` instead of dict")
                    else:
                        f_type = type([value[0] for key, value in getattr(self, field.name).items()][0])
                        k_type = type([key for key, value in getattr(self, field.name).items()][0])
                        t_list_check(field, f_type)
                        if k_type != str:
                            raise TypeError(f"The field `{field.name}` was "
                                            f"assigned by key value `{k_type}` instead of str")
            elif field.type == np:
                pass
            elif not isinstance(getattr(self, field.name), field.type):
                current_type = type(getattr(self, field.name))
                raise TypeError(f"The field `{field.name}` was assigned by `{current_type}` instead of `{field.type}`")
