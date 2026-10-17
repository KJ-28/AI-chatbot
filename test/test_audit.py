from security.audit import log_security_event
from security.input_filter import SecurityResult
from pathlib import Path
import json
def test_log_security_event():

    result = SecurityResult(
    safe=True,
    score=0,
    reason=[],
    text="Hello KK"
    )

    log_security_event(result)

    log_file = Path("logs/security.log")
    assert log_file.exists()

    
    content = log_file.read_text(
        encoding="utf-8"
    )
    lines = content.splitlines()
    first_log = lines[0]
    event = json.loads(first_log)
    
    assert event["safe"] is True
    assert event["score"] == 0
    assert event["reason"] == []
    assert event["text"] == "Hello KK"