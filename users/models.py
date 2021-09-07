from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_IGBO = "igbo"
    LANGUAGE_HAUSA = "hausa"
    LANGUAGE_YORUBA = "yoruba"

    CURRENCY_USD = "usd"
    CURRENCY_NGN = "ngn"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_NGN, "NGN"),
    ]

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_IGBO, "Igbo"),
        (LANGUAGE_YORUBA, "Yoruba"),
        (LANGUAGE_HAUSA, "Hausa"),
    ]

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ]

    # NULL is for the database, while BLANK is for the form
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)

    superhost = models.BooleanField(default=False)
