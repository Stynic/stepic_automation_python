def test_substring(full_string, substring):
    if str(substring) not in str(full_string):
        print(f'expected \'{substring}\' to be substring of \'{full_string}\'')


if __name__ == '__main__':
    test_substring('fulltext', 'some_value')
    test_substring(1, 1)
    test_substring('some_text', 'some')