from .input_filter import SecurityResult

def get_risk_level(score: int) -> str:
    """Return risk level based on score."""
    if score < 20:
        return "LOW"
    elif score < 50:
        return "MEDIUM"
    elif score < 80:
        return "HIGH"
    else:
        return "CRITICAL"





def calculate_risk(
    input_result: SecurityResult,
    injection_result: SecurityResult,
    mask_result: SecurityResult,

        
) -> SecurityResult:
    """
    calculate security risk score
    """

    score = 0
    if injection_result.safe is False:
        score += 70

    if mask_result.reason:
        score += 30


    score = min(score, 100)

    


    safe = score < 50 and injection_result.safe
    level = get_risk_level(score)
    reason = injection_result.reason + mask_result.reason
    reason.append(f"Risk Level: {level}")

    return SecurityResult(
        safe=safe,
        score=score,
        reason=reason,
        text=mask_result.text,
    )