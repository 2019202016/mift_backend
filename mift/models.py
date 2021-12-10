import datetime

from mift_backend.accounts.user.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

POST_TYPE = (
    ('Fund', "Fund"),
    ('Volunteering', "Volunteering"),
)


class POST(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=POST_TYPE, max_length=20)
    last_date = models.DateField()
    ngo_name = models.CharField(max_length=100)
    ngo_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="", blank=True)
    created_at = models.DateField(default=datetime.date.today(), blank=True)
    filled = models.BooleanField(default=False)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{8,10}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    phone_number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(POST, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return self.user.get_full_name()
