from piedra import get_winner


def test_get_winner():
    try:
        assert get_winner('p', 't') == 'human'
        assert get_winner('a', 'p') == 'human'
        assert get_winner('t', 'a') == 'human'
        assert get_winner('a', 't') == 'machine'
        assert get_winner('t', 'p') == 'machine'
        assert get_winner('p', 'a') == 'machine'
        assert get_winner('p', 'p') is None
        assert get_winner('a', 'a') is None
        assert get_winner('t', 't') is None

        print("test_get_winner ... SUCCESS!")

    except AssertionError as e:
        print("Test Failed!")
        raise

test_get_winner()
