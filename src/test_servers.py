# -*-coding=utf-8-*-
"""Test client side server echo."""
import pytest


def test_message_one_buffer_length():
    """Buffer length less than 8."""
    from client import client
    assert client("test") == "HTTP/1.1 200 OK \n <CRLF>\ntest"


def test_response_ok():
    """Test that expected byte string is created."""
    from server import response_ok
    assert response_ok() == b'HTTP/1.1 200 OK \n <CRLF>\n'


def test_response_error():
    """Test that expected byte string is created."""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 Internal server error \n <CRLF>\n'


def test_several_buffer_lengths():
    """Buffer length greater than 8."""
    from client import client
    test_string = "This is a really long message for testing purposes"
    assert client(test_string) == 'HTTP/1.1 200 OK \n <CRLF>\n' + test_string


def test_one_buffer_length():
    """Buffer length of 8."""
    from client import client
    assert client("testerte") == "HTTP/1.1 200 OK \n <CRLF>\ntesterte"


NON_ASCII = [
    ('foo&', u'foo&'),
    ('foo$', u'foo$'),
    ('foo#', u'foo#'),
    ('foo@', u'foo@'),
    ('foo*', u'foo*')
]


@pytest.mark.parametrize('val, result', NON_ASCII)
def test_for_non_ascii_characters(val, result):
    """Test if message includes non-ascii characters."""
    from client import client
    assert client(val) == 'HTTP/1.1 200 OK \n <CRLF>\n' + result
