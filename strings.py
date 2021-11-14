"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

def no_duplicates(a_string) -> str:
    ls = list(set(a_string))
    ls.sort()
    return ''.join(ls)

def reversed_words(a_string) -> str:
    return a_string.split()[::-1]

def four_char_strings(a_string) -> list:
    return [a_string[i: i+4] for i in range(0, len(a_string), 4)]

# Tests Definition
def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'

def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']

def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

def main():
    return pytest.main([__file__])


if __name__ == '__main__':
    main()
    
