"""
pytest conftest file need for fixtures
"""
import pytest
from fixtures.pandas_pipe_setup import (
    explode_pos,
    explode_duplicate_pos,
    map_column_rewrite_pos,
    map_column_new_col_pos,
)
