from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from app.core.config import settings


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY,
                                   algorithms=["HS256"])
        return decoded_token["sub"]
    except jwt.JWTError:
        return None




# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
# 		auth=("api", "YOUR_API_KEY"),
# 		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
# 			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomeness!"})




def send_simple_message(email, token):
    import requests
    response = requests.post(
		"https://api.mailgun.net/v3/sandboxb3839c633abd4f39b95585ad7c931b31.mailgun.org/messages",
		auth=("api", "38e4c9fffe1f81bb0a95ac3d64a02587-f0e50a42-e8f42ea5"),
		data={"from": "marcos.201nascimento@gmail.com",
			"to": [email["email"]],
			"subject": "Reset Password",
			"text": f"To reset your password http://localhost:8081/reset-password?tk={token}"})

    return response