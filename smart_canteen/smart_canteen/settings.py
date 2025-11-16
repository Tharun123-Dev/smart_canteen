from pathlib import Path
import os

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY - use environment variables in production
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "demo-secret-key-change-in-production"  # replace with env var in production
)

# DEBUG: set to False in production
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in ("1", "true", "yes")

# Hosts and CSRF trusted origins
ALLOWED_HOSTS = [
    "smart-canteen-r1nx.onrender.com",
    "localhost",
    "127.0.0.1",
]

# CSRF trusted origins must include scheme (https) for deployed domains
CSRF_TRUSTED_ORIGINS = [
    "https://smart-canteen-r1nx.onrender.com",
]

# If your app is behind a proxy/load balancer (Render does this),
# tell Django to trust X-Forwarded-Proto header so it recognizes HTTPS.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "menu_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "smart_canteen.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "smart_canteen.wsgi.application"
ASGI_APPLICATION = "smart_canteen.asgi.application"

# Database - SQLite for development. For production consider Postgres.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# Use STATIC_ROOT for collectstatic in production (Render uses this)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (uploaded by users)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Authentication redirects
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "menu_list"
LOGOUT_REDIRECT_URL = "/"
LOGOUT_GET_ALLOWED = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings - use environment variables for sensitive values
EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("DJANGO_EMAIL_PORT", 587))
EMAIL_USE_TLS = os.environ.get("DJANGO_EMAIL_USE_TLS", "True").lower() in (
    "1",
    "true",
    "yes",
)
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER", "you@example.com")
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD", "")  # set this securely
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Security-related flags: enable when DEBUG=False (production)
if not DEBUG:
    # Ensure cookies are only sent over HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Additional security headers you may enable depending on needs:
    # SECURE_HSTS_SECONDS = 31536000  # enable HSTS
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True
    # SECURE_SSL_REDIRECT = True

# Optional: Logging (basic)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
