"""
Tests for pandas_pipe functions
"""
import pytest
from pandas.testing import assert_frame_equal

import pandas_pipe


class TestExplodePandasPipe:
    """
    Test class for the function of create_standard_smiles
    """

    def test_explode_pos(self, explode_pos):
        """
        Test for positive case for explode
        """
        # Arrange
        dataf_input, dataf_expected = explode_pos

        # Act
        result = (
            dataf_input.pipe(
                pandas_pipe.explode_setup, columns=["num", "text"], delimiter=","
            )
            .pipe(pandas_pipe.explode_setup, columns=["states"], delimiter=";")
            .pipe(pandas_pipe.explode, column="num", ignore_index=True)
            .pipe(pandas_pipe.explode, column="text", ignore_index=True)
            .pipe(pandas_pipe.explode, column="states", ignore_index=True)
        )
        result = result.astype({"num": "float64"})

        # Assert
        assert_frame_equal(dataf_expected, result)

    def test_explode_remove_duplicate_pos(self, explode_duplicate_pos):
        """
        Test for positive case for explode after duplicate removal
        """
        # Arrange
        dataf_input, dataf_expected = explode_duplicate_pos

        # Act
        result = (
            dataf_input.pipe(
                pandas_pipe.explode_setup, columns=["message"], delimiter=" "
            )
            .pipe(pandas_pipe.explode, column="message")
            .pipe(pandas_pipe.drop_duplicates)
            .pipe(pandas_pipe.reset_index, drop=True)
        )

        # Assert
        assert_frame_equal(dataf_expected, result)

    def test_explode_input(self, explode_pos):
        """
        Double check for single column in put
        """
        # Arrange
        dataf_input, _ = explode_pos
        # Act
        # Assert
        with pytest.raises(ValueError):
            pandas_pipe.explode(dataf_input, column=["num", "text"])

    def test_explode_setup_pos(self, explode_pos):
        """
        Test for unchanged list input for explode setup
        """
        # Arrange
        dataf_input, _ = explode_pos
        # Act
        result = pandas_pipe.explode_setup(dataf_input, columns=["num"])
        # Assert
        assert_frame_equal(result, dataf_input)

    def test_map_columns_rewrite_pos(self, map_column_new_col_pos):
        """
        Test for applying mapping to the same columns
        """
        # Arrange
        dataf_input, dataf_expected = map_column_new_col_pos

        def remove(x, element):
            x.remove(element)
            return x

        # Act
        result = (
            dataf_input.pipe(pandas_pipe.start_pipeline)
            .pipe(pandas_pipe.vectorize_str, ["message"], "split")
            .pipe(pandas_pipe.map_column, "message", set, to_column="message_set")
            .pipe(
                pandas_pipe.map_column,
                "message_set",
                lambda x: remove(x, "a") if "a" in x else x,
            )
        )
        # Assert
        assert_frame_equal(dataf_expected, result)
