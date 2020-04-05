def test_substring(full_string, substring):
    if str(substring) not in str(full_string):
        print(f'expected {full_string} to be substring of {substring}')


if __name__ == '__main__':
    test_substring('fulltext', 'some_value')
    test_substring(1, 1)
    test_substring('some_text', 'some')