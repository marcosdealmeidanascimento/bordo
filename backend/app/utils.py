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
    import smtplib
    from email.message import EmailMessage
    email_address = 'marcos.201nascimento@gmail.com'
    password = 'nxufqqvaxpkmyflu'
    msg = EmailMessage()
    msg['Subject'] = 'Password Reset'
    msg['From'] = "LogBook App"
    msg['to'] = email['email']
    msg.set_content(
        f"""\
            A password reset was requested. If you didn't requested, no further action is needed.

            To reset your password click the link below:
            http://localhost:8081/reset-password?{token}&tk={token}

        """
    )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, password)
        smtp.send_message(msg=msg)