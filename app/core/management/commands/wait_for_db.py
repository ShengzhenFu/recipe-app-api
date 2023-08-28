"""
django command to wait for the database to be available
"""
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
import time


class Command(BaseCommand):
    """Django command to wait for database to be ready"""
    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 seconds')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available Now!'))
