from .input_filter import check_input,SecurityResult
from .injection import detect_prompt_injection
from .masker import mask_secret
from .risk import calculate_risk

def run_security(text:str)  -> SecurityResult   :


    """
    Run all the security checks

    Args:
        text (str):
            User input.
        
            
    Returns:
        SecurityResult:
        {
            "allowed"  : bool,
            "text"  : str,
            "risk"  : int,
            "reason"  : list[str] 
        
        }  

        ## 字典补充解释说明

        allowed:
            Whether the input is allowed.

        text:
            Sanitized user input.

        risk:
            Risk score (0-100).

        reason:
            List of detected risks.
    
    """

    ## 输入的安全检查
    input_result = check_input(text)


    if not input_result.safe:
        return input_result


    ## 输入内容的安全检查
    injection_result = detect_prompt_injection(input_result.text)

    
    if not injection_result.safe:
        return injection_result

    mask_result = mask_secret(injection_result.text)

    risk_result = calculate_risk(
    input_result,
    injection_result,
    mask_result,
)


    
    return risk_result





