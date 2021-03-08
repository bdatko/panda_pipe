"""
Functions decorated with log_step
"""

import logging
import types
from typing import Any, Callable, Dict, List, Tuple, Union

import pandas as pd
from IPython.display import display
from sklego.pandas_utils import log_step

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.NullHandler())


@log_step(names=True, print_fn=logger.info)
def start_pipeline(dataf: pd.DataFrame, deep=True) -> pd.DataFrame:
    """
    pandas dataframe method: Make a copy of this object’s indices and data.
    """
    return dataf.copy(deep=deep)


@log_step(print_fn=logger.info, shape_delta=True)
def dropna(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Remove missing values.
    """
    return dataf.dropna(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def explode_setup(
    dataf: pd.DataFrame, columns: Union[List[str], Tuple[str]], delimiter: str = ","
) -> pd.DataFrame:
    """
    For each column in `columns` apply a split by delimiter if the cell is a str and the `delimiter` is within the cell
    """

    for column in columns:
        dataf[column] = dataf[column].apply(
            lambda x: x.split(delimiter) if isinstance(x, str) and delimiter in x else x
        )

    return dataf


@log_step(print_fn=logger.info, shape_delta=True)
def explode(
    dataf: pd.DataFrame, column: Union[str, Tuple], ignore_index=False
) -> pd.DataFrame:
    """
    pandas dataframe method: Transform each element of a list-like to a row, replicating index values.
    """
    return dataf.explode(column, ignore_index=ignore_index)


@log_step(print_fn=logger.info, shape_delta=True)
def vectorize_str(
    dataf: pd.DataFrame, columns: List[str], method: str, **kwargs
) -> pd.DataFrame:
    """
    For each column in `columns` apply str `method` with `kwargs`
    """
    for column in columns:
        dataf[column] = getattr(dataf[column].str, method)(**kwargs)
    return dataf


@log_step(print_fn=logger.info, shape_delta=True)
def drop_duplicates(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Return DataFrame with duplicate rows removed.
    """
    return dataf.drop_duplicates(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def replace(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas method: Values of the DataFrame are replaced with other values dynamically
    """
    return dataf.replace(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def sum_columns(
    dataf: pd.DataFrame, to_column: str, columns: List[str]
) -> pd.DataFrame:
    """
    Sum `columns` along axis=1 storing the result `to_column`.
    """
    dataf[to_column] = dataf[columns].sum(axis=1)
    return dataf


@log_step(names=True, print_fn=logger.info, shape_delta=True)
def reset_index(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Reset the index, or a level of it.
    """
    return dataf.reset_index(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def rename(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Alter axes labels.
    """
    return dataf.rename(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def drop(dataf: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Drop specified labels from rows or columns.
    """
    return dataf.drop(**kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def query(dataf: pd.DataFrame, expr: str, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Query the columns of a DataFrame with a boolean expression.
    """
    return dataf.query(expr, **kwargs)


@log_step(print_fn=logger.info, shape_delta=True)
def series_to_frame(series: pd.Series, new_col_names: Dict[Any, Any]) -> pd.DataFrame:
    """Turns a pd.Series into a pd.DataFrame, reseting the index, and renaming the columns"""
    return series.to_frame().reset_index().rename(columns=new_col_names)


@log_step(print_fn=logger.info, shape_delta=True)
def astype(dataf: pd.DataFrame, dtype, **kwargs) -> pd.DataFrame:
    """
    pandas dataframe method: Cast a pandas object to a specified dtype `dtype`.
    """
    return dataf.astype(dtype, **kwargs)


def display_all(dataf: pd.DataFrame) -> None:
    """
    Display more columns and rows within jupyter notebooks
    """
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        display(dataf)


@log_step(print_fn=logger.info, shape_delta=True)
def map_column(
    dataf: pd.DataFrame,
    column: str,
    arg: Union[Callable, Dict, pd.Series],
    to_column: str = None,
    **kwargs
) -> pd.DataFrame:
    """Wrapper for pd.Series.map, with the option to either replace column to add a new column"""
    if to_column is None:
        dataf[column] = dataf[column].map(arg, **kwargs)
    else:
        dataf[to_column] = dataf[column].map(arg, **kwargs)
    return dataf


__all__ = [
    name
    for name, thing in globals().items()
    if not (name.startswith("_") or isinstance(thing, types.ModuleType))
]
