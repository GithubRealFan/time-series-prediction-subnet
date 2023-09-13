# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Taoshi
# Copyright © 2023 TARVIS Labs, LLC

import os


class ValiConfig:
    RMSE_WEIGHT = 0.001
    SCALE_FACTOR = 0.0001
    HISTORICAL_DATA_LOOKBACK_DAYS_MIN = 5
    HISTORICAL_DATA_LOOKBACK_DAYS_MAX = 10
    PREDICTIONS_MIN = 50
    PREDICTIONS_MAX = 300
    DELETE_STALE_DATA = 180
    BASE_DIR = base_directory = os.path.dirname(os.path.abspath(__file__))

