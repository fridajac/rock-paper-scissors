from evaluate_game import evaluate_game


def test_should_return_enum():
    assert type(evaluate_game('Rock', 'Scissor')) == bool


def test_should_return_true_if_user_won():
    assert evaluate_game('Rock', 'Scissor') is True


def test_should_return_true_if_user_won():
    assert evaluate_game('Scissor', 'Paper') is True


def test_should_return_true_if_user_won():
    assert evaluate_game('Paper', 'Rock') is True


def test_should_return_false_if_computer_won():
    assert evaluate_game('Scissor', 'Rock') is False


def test_should_return_false_if_computer_won():
    assert evaluate_game('Paper', 'Scissor') is False


def test_should_return_false_if_computer_won():
    assert evaluate_game('Rock', 'Paper') is False


def test_should_return_none_if_draw():
    assert evaluate_game('Paper', 'Paper') is None


def test_should_return_none_if_draw():
    assert evaluate_game('Rock', 'Rock') is None


def test_should_return_none_if_draw():
    assert evaluate_game('Scissor', 'Scissor') is None
