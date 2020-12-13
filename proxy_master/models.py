from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, help_text="Имя БФП")
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name


class Proxy(models.Model):
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, )
    proxy_id = models.AutoField(primary_key=True, editable=False)
    proxy_port = models.IntegerField(help_text="Port в диапазоне 30.000 - 32.000", null=False, default=0)
    proxy_name = models.CharField(max_length=50, help_text="Имя отключаемой прокси")
    fp_name = models.CharField(max_length=50, help_text="FP_name", default="ololo")
    author = models.CharField(max_length=50, help_text="Имя автора ", null=False, default="eg")
    protocol = models.CharField(max_length=50, help_text="Протокол создаваемой прокси", default="TCP")
    time_to_stop = models.DateTimeField(blank=True, null=False, default=timezone.now())
    time_to_start = models.DateTimeField(blank=True, null=False, default=timezone.now())
    proxy_status = models.BooleanField(blank=True, null=False, default="0")

    def publish(self):
        self.time_to_start = timezone.now()
        self.save

    def __str__(self):
        return self.proxy_name


class staticParam(models.Model):
    static_path = models.CharField(max_length=50, help_text="Путь до бинарника proxy")
    proxy_type = models.CharField(max_length=50, default="tcp" ,help_text="тип прокси")

    def __str__(self):
        return "ParamName"