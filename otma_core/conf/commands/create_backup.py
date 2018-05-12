from django.core.management.base import BaseCommand
from otma_core.modules.security.backup.models import Backup
from otma_core.modules.security.backup.services import BackupManager


class Command(BaseCommand):
    help = 'Print hello world'

    def handle(self, **options):
        backup_paramters = BackupManager().create_backup()
        try:
            backup = Backup.objects.get(backup_file_name=backup_paramters['file_name'])
        except:
            backup = Backup()

        backup.file_name = backup_paramters['file_name']
        backup.file_link = backup_paramters['link']
        backup.file_size = backup_paramters['size']
        backup.save()
