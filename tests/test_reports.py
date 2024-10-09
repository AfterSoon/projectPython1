from src.reports import spending_by_category
from src.utils import get_excel


def test_spending_by_category(category):
    assert (
        spending_by_category(get_excel("dataframe"), "Фастфуд", "17.01.2018")
        == category
    )


def test_record_file(category):
    with open("report.txt", "r") as file:
        content = file.read()
        assert content == category
