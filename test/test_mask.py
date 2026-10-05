from security.masker import (
    mask_phone,
    mask_email,
    mask_token,
    mask_jwt,
    mask_secret,
)




def test_mask_phone():
    phone = "13812345678"
    result = mask_phone(phone)

    assert result == "138****5678"



def test_mask_email():
    email = "kkchat@gmail.com"
    result = mask_email(email)

    assert result == "kk****@gmail.com"

def test_mask_token():
    token = "sk-abcdef123456"
    result = mask_token(token)

    assert result == "<API_KEY_MASKED>"


def test_mask_jwt():
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    result = mask_jwt(jwt)

    assert result == "<JWT_MASKED>"




def test_mask_secret_phone():
    # Arrange
    text = "My phone is 13812345678"

    # Act
    result = mask_secret(text)

    # Assert
    assert result.safe is True
    assert result.text == "My phone is 138****5678"
    assert "Phone Number" in result.reason



def test_mask_secret_email():
    text = "My email is kkchat@gmail.com"

    result = mask_secret(text)

    assert result.safe is True
    assert result.text == "My email is kk****@gmail.com"
    assert "Email Address" in result.reason



def test_mask_secret_token():
    text = "API Key: sk-abcdef123456"

    result = mask_secret(text)

    assert result.safe is True
    assert "<API_KEY_MASKED>" in result.text
    assert "API Key" in result.reason



def test_mask_secret_jwt():
    text = (
        "Token: "
        "eyJhbGciOiJIUzI1NiJ9."
        "eyJ1c2VyIjoiS0oifQ."
        "abc123xyz"
    )

    result = mask_secret(text)

    assert result.safe is True
    assert "<JWT_MASKED>" in result.text
    assert "Json Web Token" in result.reason


def test_mask_secret_multiple():
    text = (
        "Phone: 13812345678, "
        "Email: kkchat@gmail.com"
    )

    result = mask_secret(text)

    assert "138****5678" in result.text
    assert "kk****@gmail.com" in result.text






