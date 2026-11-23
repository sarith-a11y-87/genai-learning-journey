def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_chat_returns_reply(client):
    resp = client.post("/chat", json={"session_id": "s1", "message": "Hello"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["session_id"] == "s1"
    assert body["reply"] == "echo: Hello"
    # stored history is "Hello" (2 tokens) + "echo: Hello" (3 tokens)
    assert body["history_tokens"] == 5


def test_system_prompt_is_sent_first_but_not_stored(client, fake_llm):
    client.post("/chat", json={"session_id": "s1", "message": "Hello"})
    sent = fake_llm.calls[0]
    assert sent[0].role == "system"
    assert sent[0].content == "TEST SYSTEM PROMPT"
    assert [(m.role, m.content) for m in sent[1:]] == [("user", "Hello")]


def test_chat_remembers_the_session(client, fake_llm):
    client.post("/chat", json={"session_id": "s1", "message": "My budget is 2M"})
    client.post("/chat", json={"session_id": "s1", "message": "What was my budget?"})
    second_call = fake_llm.calls[1]
    contents = [m.content for m in second_call]
    assert contents == [
        "TEST SYSTEM PROMPT",
        "My budget is 2M",
        "echo: My budget is 2M",
        "What was my budget?",
    ]


def test_sessions_do_not_leak(client, fake_llm):
    client.post("/chat", json={"session_id": "alice", "message": "secret A"})
    client.post("/chat", json={"session_id": "bob", "message": "hi"})
    bob_call = fake_llm.calls[1]
    assert all("secret A" not in m.content for m in bob_call)


def test_history_is_trimmed_before_calling_llm(client, fake_llm):
    # settings fixture sets max_history_messages=4
    for i in range(5):
        client.post("/chat", json={"session_id": "s1", "message": f"msg {i}"})
    last_call = fake_llm.calls[-1]
    assert last_call[0].role == "system"
    assert len(last_call) == 1 + 4
    assert last_call[-1].content == "msg 4"


def test_empty_message_is_rejected(client):
    resp = client.post("/chat", json={"session_id": "s1", "message": ""})
    assert resp.status_code == 422


def test_missing_session_id_is_rejected(client):
    resp = client.post("/chat", json={"message": "hi"})
    assert resp.status_code == 422
