import pytest
from data_tools.pyspark import SparkApp

# ===========================================================

def test_dummy():
    assert 1 == 1

# def test_read_csv():
#     sparkapp = SparkApp()

#     actual_output = sparkapp.read_csv('tests/data/sample.csv')
#     expected_output = sparkapp.spark.read.csv('tests/data/sample.csv', header=True, inferSchema=True)

#     try:
#         assert actual_output.collect() == expected_output.collect()
#     except AssertionError:
#         pytest.fail("RESULT: FAILED")
