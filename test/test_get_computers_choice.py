from get_computers_choice import get_computers_choice


def test_should_return_str():
    assert type(get_computers_choice()) == str


def test_should_return_random_choice():
    ok_response = ['Rock', 'Paper', 'Scissor']
    assert get_computers_choice() in ok_response
