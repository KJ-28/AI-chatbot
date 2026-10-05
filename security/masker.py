from .config import SECRET_RULES
from .input_filter import SecurityResult
import re


def mask_phone(phone: str) -> str:
    return phone[:3] + "****" + phone[-4:]


def mask_email(email: str) -> str:
    username,domain = email.split("@")
    return username[:2] + "****" + "@" + domain


def mask_token(token: str) -> str:
    return "<API_KEY_MASKED>"

def mask_jwt(jwt: str) -> str:
    return "<JWT_MASKED>"

def mask_secret(text:str) -> SecurityResult :
## normalise

    original_text = text
    masked_text = text
    masked_reason = []

## loop SECRET_RULES

    for rule_name,rule in SECRET_RULES.items():
        pattern = rule["pattern"]
        mask_type = rule["mask_type"]
        description = rule["description"]

        match = re.search(pattern, masked_text)
        if not match:
            continue
        matched_text = match.group()
        if mask_type == "phone":
            masked_value =  mask_phone(matched_text)
        elif mask_type == "email":
            masked_value =  mask_email(matched_text)
        elif mask_type == "token":
            masked_value =  mask_token(matched_text)
        elif mask_type == "jwt" :
            masked_value = mask_jwt(matched_text)


        masked_text = masked_text.replace(
            matched_text,
            masked_value

        )

        masked_reason.append(description)



    
    return SecurityResult(
    safe=True,
    score=0,
    reason=masked_reason,
    text=masked_text,
)

