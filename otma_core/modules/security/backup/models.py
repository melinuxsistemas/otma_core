from django.db import models
from django.conf import settings


class Backup(models.Model):
    class Meta:
        db_table = 'core_security_backup'
        verbose_name = "Backup"
        verbose_name_plural = "Backups"

    created_date = models.DateTimeField(auto_now=True, null=False)
    file_name = models.CharField("Nome do arquivo", null=False, blank=False,unique=True, max_length=15, validators=[],error_messages=settings.ERRORS_MESSAGES)
    file_size = models.PositiveIntegerField("Tamanho do arquivo", null=False, error_messages=settings.ERRORS_MESSAGES)
    file_link = models.CharField("Url do arquivo", null=False, blank=False, max_length=100, validators=[], error_messages=settings.ERRORS_MESSAGES)
