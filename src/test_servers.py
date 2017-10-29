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


# Tests for step2
# def test_get_reponse_ok():
#     """Test a proper GET request returns 200 OK."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == 'HTTP/1.1 200 OK\n\r\n\nfake.html'


# def test_put_request_error():
#     """Test a PUT request is 405 error."""
#     response = client((
#         'PUT fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 405 Improper request method.'
#                         '\nInternal server error\n\r\n\n')


# def test_delete_request_error():
#     """Test a DELETE request is 405 error."""
#     response = client((
#         'DELE fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 405 Improper request method.'
#                         '\nInternal server error\n\r\n\n')


# def test_post_request_error():
#     """Test a POST request is 405 error."""
#     response = client((
#         'POST fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 405 Improper request method.'
#                         '\nInternal server error\n\r\n\n')


# def test_valid_protocol():
#     """Test valid HTTP/1.1 protocol returns 200 OK."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == 'HTTP/1.1 200 OK\n\r\n\nfake.html'


# def test_invalid_protocol():
#     """Test invalid HTTP protocol returns 400 error."""
#     response = client((
#         'GET fake.html HTTP/22.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 400 Improper protocol.'
#                         '\nInternal server error\n\r\n\n')


# def test_header_not_exist():
#     """Test if header is not in request returns 406 error."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\n\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 406 Improper header.'
#                         '\nInternal server error\n\r\n\n')


# def test_header_exist():
#     """Test if header is in request returns 200 OK."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == 'HTTP/1.1 200 OK\n\r\n\nfake.html'


# def test_header_improper_format():
#     """Test if improper header returns 406 error."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 406 Improper header.'
#                         '\nInternal server error\n\r\n\n')


# def test_header_proper_formal():
#     """Test if proper header returns 200 OK."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == 'HTTP/1.1 200 OK\n\r\n\nfake.html'


# def test_exception_on_protocol_error():
#     """Test if error raises exception."""
#     pytest.raises(ValueError)
#     client((
#         'GET fake.html HTTP/1.2\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )


# def test_exception_on_method_error():
#     """Test if error raises exception."""
#     pytest.raises(ValueError)
#     client((
#         'PUT fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )


# def test_exception_on_header_error():
#     """Test if error raises exception."""
#     pytest.raises(ValueError)
#     client((
#         'GET fake.html HTTP/1.1\r\n'
#         '\nHost: www.something.com:80\r\n'
#         '\nSome test string to see if this works.')
#     )


# def test_request_include_host():
#     """Test if improper header returns 406 error."""
#     response = client((
#         'GET fake.html HTTP/1.1\r\n\n'
#         '\nSome test string to see if this works.')
#     )
#     assert response == ('HTTP/1.1 400 You must include Host:.'
#                         '\nInternal server error\n\r\n\n')


# Tests for step 3
def test_resolve_uri_200_ok_with_good_request():
    """Test if 200 OK included with response."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    first_line = response.split('\n')
    assert first_line[0] == 'HTTP/1.1 200 OK'


def test_resolve_uri_returns_content_type():
    """Test if header includes content-type."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    second_line = response.split('\n')
    assert second_line[1].startswith('Content-Type:')


def test_resolve_uri_returns_length():
    """Test if header includes length."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    third_line = response.split('\n')
    assert third_line[2].startswith('Length:')


def test_resolve_uri_returns_crlf_line():
    """Test is crlf line is included between header and body."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    crlf_line = response.split('\n')
    assert crlf_line[3] == '\r'


def test_resolve_uri_returns_body_header():
    """Test if body header is included in response."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    body_line = response.split('\n')
    assert body_line[4].startswith('Body:')


def test_resolve_uri_body_contains_file_text():
    """Test if body includes appropriate material."""
    response = client(('GET /make_time.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    assert 'simple script that returns and HTML page with the current'\
        in response


def test_resolve_uri_400_if_file_not_exist():
    """Test if appropirate error if file not exists."""
    response = client(('GET /make_tim.py '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    assert 'HTTP/1.1 400 File does not exist.' in response


def test_resolve_uri_except_if_file_not_exist():
    """Test if appropirate expeption if file not exists."""
    pytest.raises(ValueError)
    client(('GET /make_tim.py '
            'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
            'Some filler text'))


def test_resolve_uri_403_if_try_escape_root():
    """Test if appropirate expeption if file not exists."""
    response = client(('GET ../../ '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    assert 'HTTP/1.1 403 Access denied.' in response


def test_resolve_uri_returns_html_list_if_dir():
    """Test if request for directory returns html."""
    response = client(('GET /images '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    assert '<html>' in response


def test_resolve_uri_returns_list_if_dir():
    """Test if request for directory returns list of files."""
    response = client(('GET /images '
                       'HTTP/1.1\r\n\nHost: www.somesite.com\r\n\n\r\n\n'
                       'Some filler text'))
    assert 'JPEG_example.jpg' and 'sample_1.jpg' and 'Sample_Scene_Balls.jpg'\
        in response
