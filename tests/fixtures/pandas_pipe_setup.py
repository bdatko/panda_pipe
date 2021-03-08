"""
pytest fixtures for common setup
"""
import pytest
import pandas as pd


@pytest.fixture(
    params=(
        (
            pd.read_csv("tests/fixtures/dataframe_test_explode_input.csv"),
            pd.read_csv("tests/fixtures/dataframe_test_explode_output.csv"),
        ),
    )
)
def explode_pos(request):
    """
    Setup dataframe for positive testing of explode
    """
    return request.param


@pytest.fixture(
    params=(
        (
            pd.read_csv(
                "tests/fixtures/dataframe_test_explode_drop_duplicates_input.csv"
            ),
            pd.read_csv(
                "tests/fixtures/dataframe_test_explode_drop_duplicates_output.csv"
            ),
        ),
    )
)
def explode_duplicate_pos(request):
    """
    Setup dataframe for positive testing of explode with duplicates
    """
    return request.param


@pytest.fixture(
    params=(
        (
            pd.DataFrame(
                [
                    {"customer": "A", "message": "hi i need help i want a card"},
                    {"customer": "B", "message": "i want a card"},
                ]
            ),
            pd.DataFrame(
                [
                    {
                        "customer": "A",
                        "message": {"card", "i", "want", "help", "need", "hi"},
                    },
                    {"customer": "B", "message": {"card", "want", "i",}},
                ]
            ),
        ),
    )
)
def map_column_rewrite_pos(request):
    """
    Setup dataframe for positive case of mapping the same column
    """
    return request.param


@pytest.fixture(
    params=(
        (
            pd.DataFrame(
                [
                    {"customer": "A", "message": "hi i need help i want a card"},
                    {"customer": "B", "message": "i want a card"},
                ]
            ),
            pd.DataFrame(
                {
                    "customer": {0: "A", 1: "B"},
                    "message": {
                        0: ["hi", "i", "need", "help", "i", "want", "a", "card"],
                        1: ["i", "want", "a", "card"],
                    },
                    "message_set": {
                        0: {"card", "help", "hi", "i", "need", "want"},
                        1: {"card", "i", "want"},
                    },
                }
            ),
        ),
    )
)
def map_column_new_col_pos(request):
    """
    Setup dataframe for positive case of mapping the same column
    """
    return request.param
