
def test_input_text(expected_result, actual_result):
    """
    Ассерт,для проверки фактического и ожидаемого результата
    :argument expected_result:  Фактическое значение проверки
    :argument actual_result:  Ожидаемое значение проверки
    """
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


if __name__ == "__main__":
    test_input_text(5,4)