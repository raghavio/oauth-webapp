"""
Default configurations.
"""

# App secret key. Used to create secure sessions.
SECRET_KEY = "\x03\xf3\x9f\xe3\xd0\x9b-I\x97~U\x9ez\x9359+\xea\xe5J"

# Plain text file we use to store user data. It's at root so just provide the file name.
DATABASE_FILE = "database"

# Details for Facebook OAuth
FACEBOOK = {
    "name": "Facebook",
    "client_id": "210978529266397",
    "client_secret": "a0facebf9f04574e9776bd5cd15a8464",
    "redirect_uri": "http://localhost:5000/oauth/facebook",
    "scope": "email",
    "login_url": "https://www.facebook.com/dialog/oauth",
    "login_params": ["client_id", "redirect_uri", "scope"],
    "token_url": "https://graph.facebook.com/v2.3/oauth/access_token",
    "token_params": ["client_id", "redirect_uri", "client_secret"],
    "user_data_api": "https://graph.facebook.com/v2.5/me",
    "user_data_params": {"fields": "name, first_name, last_name, email, gender, link, id"}
}

# Details for Google OAuth
GOOGLE = {
    "name": "Google",
    "client_id": "687376816228-qmj1n7vpqnhlc1pehdqrrdv55k501gda.apps.googleusercontent.com",
    "client_secret": "7uG15dibA5AHckGGUTRobUKZ",
    "redirect_uri": "http://localhost:5000/oauth/google",
    "scope": "profile email",
    "login_url": "https://accounts.google.com/o/oauth2/auth",
    "login_params": ["client_id", "redirect_uri", "scope", "response_type"],
    "response_type": "code",
    "token_url": "https://accounts.google.com/o/oauth2/token",
    "token_params": ["client_id", "redirect_uri", "client_secret", "scope", "grant_type"],
    "grant_type": "authorization_code",
    "user_data_api": "https://www.googleapis.com/userinfo/v2/me",
    "user_data_params": None
}

