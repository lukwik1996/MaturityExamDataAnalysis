import MaturityExamAnalysis
try:
    import pytest
except ImportError:
    print("You need pytest module intalled to run the tests. "
          "Visit https://docs.pytest.org/en/latest/getting-started.html for installation help.")


if __name__ == '__main__':

    # tests
    test_numbers_attend = [20, 10, 100, 50, 2000, 1000000]
    test_numbers_pass = [10, 1, 27, 40, 1780, 231810]
    test_result = [0, 0, 0, 0, 0, 0]
    correct_result = [50, 10, 27, 80, 89, 23.181]

    test_result, test_numbers_pass, test_numbers_attend = MaturityExamAnalysis.MaturityExamAnalysis.count_pass_rate(
        test_result, test_numbers_pass, test_numbers_attend)

    for i in range(len(test_result)):
        assert test_result[i] == correct_result[i], print('Value expected: ' + str(correct_result[i]) +
                                                          ', value returned: ' + str(test_result[i]))

    """
    TO FIX - BRAK NIEKTORYCH POLSKICH ZNAKOW
    
    test_string = "\x8cl\xb9sk to pi\xeakne wojew\xf3dztwo.\r\n"
    test_string = test_string.encode(encoding="ANSI", errors='ignore')
    test_string_fixed = "Śląsk to piękne województwo."
    tst = MaturityExamAnalysis.MaturityExamAnalysis.clean_string(test_string)
    print(tst)
    assert MaturityExamAnalysis.MaturityExamAnalysis.clean_string(test_string) == test_string_fixed, print(test_string)
    """

    array_1, array_2, array_3 = MaturityExamAnalysis.MaturityExamAnalysis.fill_arrays_with_0(10)
    assert len(array_1) == 10 and len(array_2) == 10 and len(array_3) == 10

    for i in range(len(array_1)):
        assert array_1[i] == 0
        assert array_2[i] == 0
        assert array_3[i] == 0
