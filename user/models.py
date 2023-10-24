from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    phone = models.CharField(_("Phone Number "), max_length=13, unique=True)
    admission_no = models.CharField(max_length=12, unique=True)
    date_of_birth = models.DateTimeField()
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", 'first_name', 'last_name', 'email']