# -*-coding=utf-8-*-
"""Test client side server echo."""
import pytest
from client import client

# def test_message_one_buffer_length():
#     """Buffer length less than 8."""
#     from client import client
#     assert client("test") == "HTTP/1.1 200 OK \n <CRLF>\ntest"


# def test_response_ok():
#     """Test that expected byte string is created."""
#     from server import response_ok
#     assert response_ok() == b'HTTP/1.1 200 OK \n <CRLF>\n'


# def test_response_error():
#     """Test that expected byte string is created."""
#     from server import response_error
#     assert response_error() == b'HTTP/1.1 500 Internal server error \n <CRLF>\n'


# def test_several_buffer_lengths():
#     """Buffer length greater than 8."""
#     from client import client
#     test_string = "This is a really long message for testing purposes"
#     assert client(test_string) == 'HTTP/1.1 200 OK \n <CRLF>\n' + test_string


# def test_one_buffer_length():
#     """Buffer length of 8."""
#     from client import client
#     assert client("testerte") == "HTTP/1.1 200 OK \n <CRLF>\ntesterte"


# NON_ASCII = [
#     ('foo&', u'foo&'),
#     ('foo$', u'foo$'),
#     ('foo#', u'foo#'),
#     ('foo@', u'foo@'),
#     ('foo*', u'foo*')
# ]


# @pytest.mark.parametrize('val, result', NON_ASCII)
# def test_for_non_ascii_characters(val, result):
#     """Test if message includes non-ascii characters."""
#     from client import client
#     assert client(val) == 'HTTP/1.1 200 OK \n <CRLF>\n' + result


def test_get_reponse_ok():
    """Test a proper GET request returns 200 OK."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == 'HTTP/1.1 200 OK\n<CRLF>\n\nfake.html'


def test_put_request_error():
    """Test a PUT request is 405 error."""
    response = client((
        'PUT fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 405 Improper request method.'
                        '\nInternal server error\n<CRLF>\n')


def test_delete_request_error():
    """Test a DELETE request is 405 error."""
    response = client((
        'DELE fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 405 Improper request method.'
                        '\nInternal server error\n<CRLF>\n')


def test_post_request_error():
    """Test a POST request is 405 error."""
    response = client((
        'POST fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 405 Improper request method.'
                        '\nInternal server error\n<CRLF>\n')


def test_valid_protocol():
    """Test valid HTTP/1.1 protocol returns 200 OK."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == 'HTTP/1.1 200 OK\n<CRLF>\n\nfake.html'


def test_invalid_protocol():
    """Test invalid HTTP protocol returns 400 error."""
    response = client((
        'GET fake.html HTTP/22.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 400 Improper protocol.'
                        '\nInternal server error\n<CRLF>\n')


def test_header_not_exist():
    """Test if header is not in request returns 406 error."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 406 Improper header.'
                        '\nInternal server error\n<CRLF>\n')


def test_header_exist():
    """Test if header is in request returns 200 OK."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\nGivemefile: Name\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == 'HTTP/1.1 200 OK\n<CRLF>\n\nfake.html'


def test_header_improper_format():
    """Test if improper header returns 406 error."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\nHeader: Something'
        '\nMore: \n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == ('HTTP/1.1 406 Improper header.'
                        '\nInternal server error\n<CRLF>\n')


def test_header_proper_formal():
    """Test if proper header returns 200 OK."""
    response = client((
        'GET fake.html HTTP/1.1'
        '\nGivemefile: Name'
        '\nHeader: Blahhhh!\n<CRLF>'
        '\nSome test string to see if this works.')
    )
    assert response == 'HTTP/1.1 200 OK\n<CRLF>\n\nfake.html'
