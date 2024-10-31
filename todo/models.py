from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pytz import timezone as pytz_timezone

desired_timezone = pytz_timezone('America/New_York')

class TodoTemplate(models.Model):
    # Other fields
    due_date = models.DateField(null=True, blank=True)
class List(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    list_tag = models.CharField(max_length=50, default='none')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_shared = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text

class ListTags(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag_name = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.tag_name


class ListItem(models.Model):
    # the name of a list item
    PRIORITY_CHOICES = [(1, 'High'), (2, 'Medium'), (3, 'Low')]
    priority = models.PositiveSmallIntegerField(
        choices = PRIORITY_CHOICES,
        default = 2
    )
    item_name = models.CharField(max_length=50, null=True, blank=True)
    # the text note of a list item
    item_text = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    finished_on = models.DateTimeField()
    due_date = models.DateTimeField()
    tag_color = models.CharField(max_length=10)
    delay = models.IntegerField(default=0)
    completion_time = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return "%s: %s" % (str(self.item_text), self.is_done)
    
    def calculate_delay(self):
        if self.is_done and self.finished_on and self.due_date:
            delay_days = (self.finished_on.date() - self.due_date.date()).days # This is getting the delay in days
            if delay_days >= 0:
                self.delay = delay_days

    def calculate_completion_time(self):
        if self.is_done and self.finished_on and self.created_on:
            # Chat GPT Assisted in making timezone aware
            finished_on = timezone.make_aware(self.finished_on) if timezone.is_naive(self.finished_on) else self.finished_on
            created_on = timezone.make_aware(self.created_on) if timezone.is_naive(self.created_on) else self.created_on
            #print(finished_on)
            #print(created_on)
            #print(finished_on - created_on)
            self.completion_time = (finished_on - created_on).days


class Template(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class TemplateItem(models.Model):
    item_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    finished_on = models.DateTimeField()
    due_date = models.DateField()
    tag_color = models.CharField(max_length=10)
    
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.item_text

class SharedUsers(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    shared_user = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.list_id)

class SharedList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shared_list_id = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.user)
