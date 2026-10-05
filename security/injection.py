from .input_filter import SecurityResult
from .config import INJECTION_RULES

def detect_prompt_injection(text: str) -> SecurityResult:
    """
    Detect Prompt Injection Attack

    Args:
        text (str): User Input

    Returns:
        SecurityResult
    """
    
    ## 1. Normalize (标准化)
    original_text = text
    text = text.lower()

    ## 2. detect (检测)
    ## 第一层：遍历每一个 category
    for category, patterns in INJECTION_RULES.items():
        
        ## 第二层：遍历 category 里面的每一个 pattern
        for pattern in patterns:
            
            ## 命中？
            if pattern.lower() in text:
                # YES -> 立即返回 SecurityResult(False) [不安全]
                return SecurityResult(
                    safe=False,          # 修正：去掉逗号，下同
                    score=100,
                    reason=[f"命中注入规则，类别: {category}, 关键词: {pattern}"], # 建议把命中的类别和词带上，便于调试
                    text=original_text   # 返回原始文本
                )
            
            # NO -> 继续循环 (这里不需要写 else，因为不命中自然就会进入下一次循环)

    ## 3. 全部循环结束
    ## NO -> 返回 SecurityResult(True) [安全]
    return SecurityResult(
        safe=True,
        score=0,
        reason=[],
        text=original_text  # 如果安全，建议返回 original_text，或者按你原代码返回 "" (视你的业务需求而定)
    )





