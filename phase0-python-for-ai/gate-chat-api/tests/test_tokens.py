from chat_api.models import Message
from chat_api.tokens import estimate_history_tokens, estimate_tokens


def test_estimate_tokens_rounds_up():
    assert estimate_tokens("") == 0
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("abcde") == 2


def test_estimate_history_tokens_sums_messages():
    history = [
        Message(role="user", content="abcd"),  # 1
        Message(role="assistant", content="abcdefgh"),  # 2
    ]
    assert estimate_history_tokens(history) == 3
    assert estimate_history_tokens([]) == 0
