from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
labels = (
    ('Per', 'Personal'),
    ('Wor', 'Work'),
    ('Sho', 'Shopping'),
    ('Oth', 'Others'),
)
category=(
    ('act','Active'),
    ('don','Done'),
)
class Post(models.Model):
    description=models.TextField()
    labels=models.CharField(max_length=3,choices=labels)
    date_posted=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=3,choices=category)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('todo-list')