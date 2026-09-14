from agent import draft_reply, simulate_send
from mailbox import get_message


if __name__ == "__main__":
    message = get_message("m-001")
    assert message is not None
    draft = draft_reply(message)
    print({"message_id": draft.message_id, "intent": draft.intent.value, "draft": draft.body, "requires_approval": draft.requires_approval})
    try:
        simulate_send(draft, approved=False)
    except PermissionError as exc:
        print({"send_blocked": str(exc)})
