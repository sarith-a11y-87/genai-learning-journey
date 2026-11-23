from chat_api.memory import SessionStore


def test_unknown_session_is_empty():
    assert SessionStore().history("nobody") == []


def test_add_and_history_keep_order():
    store = SessionStore()
    store.add("s1", "user", "hello")
    store.add("s1", "assistant", "hi there")
    assert [(m.role, m.content) for m in store.history("s1")] == [
        ("user", "hello"),
        ("assistant", "hi there"),
    ]


def test_sessions_are_isolated():
    store = SessionStore()
    store.add("a", "user", "for A")
    store.add("b", "user", "for B")
    assert [m.content for m in store.history("a")] == ["for A"]
    assert [m.content for m in store.history("b")] == ["for B"]


def test_history_returns_a_copy():
    store = SessionStore()
    store.add("s1", "user", "hello")
    store.history("s1").clear()  # changing the returned list...
    assert len(store.history("s1")) == 1  # ...must not change the stored history


def test_recent_returns_last_n():
    store = SessionStore()
    for i in range(6):
        store.add("s1", "user", f"m{i}")
    assert [m.content for m in store.recent("s1", 3)] == ["m3", "m4", "m5"]
    assert len(store.recent("s1", 50)) == 6


def test_clear_forgets_session():
    store = SessionStore()
    store.add("s1", "user", "hello")
    store.clear("s1")
    store.clear("never-existed")  # must not raise
    assert store.history("s1") == []
