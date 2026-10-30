from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 4


def test_days_left_is_negative_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == -2

def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    assert is_urgent(due, today) is True

def test_is_urgent_when_due_in_exactly_limit_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    assert is_urgent(due, today) is True


def test_is_not_urgent_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    assert is_urgent(due, today) is False

def test_sort_by_due_puts_soonest_first():
    # Arrange
    late = {"title": "Report", "due": date(2026, 10, 30)}
    soon = {"title": "Quiz", "due": date(2026, 10, 21)}
    tasks = [late, soon]
    # Act
    result = sort_by_due(tasks)
    # Assert
    assert result[0] == soon

def test_completion_rate_is_zero_when_no_tasks():
    assert completion_rate(0, 0) == 0.0


def test_completion_rate_rounds_to_one_decimal_place():
    assert completion_rate(1, 3) == 33.3

