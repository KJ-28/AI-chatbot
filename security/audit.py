from .input_filter import SecurityResult
import json
from datetime import datetime

def log_security_event(
        result : SecurityResult,
) -> None:
    """
    write Security Audit Log 

    Args:


    Returns:
        None

    """

    create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = {
        "timestamp": create_time,
        "module": "Security Audit",
        "safe": result.safe,
        "score": result.score,
        "reason": result.reason,
        "text": result.text,
    }

    log = json.dumps(
    event,
    ensure_ascii=False
    )

    with open(
        "logs/security.log",
        "a",
        encoding="utf-8"
    ) as f:
        f.write(log + "\n")


    