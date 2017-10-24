"""."""
# -*-coding=utf-8-*-

def test_message_one_buffer_length():
    """."""
    from client import client
    assert client("test") == "test"


def test_several_buffer_lengths():
    """."""
    from client import client
    assert client("This is a really long message for testing purposes") == "This is a really long message for testing purposes"


def test_one_buffer_length():
    """."""
    from client import client
    assert client("testerte") == "testerte"


def test_for_non_ascii_characters():
    """."""
    from client import client
    assert client("testerte£") == "testerte£"