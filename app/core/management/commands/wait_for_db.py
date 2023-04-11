"""
Django comand wait for the database to be avilable.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Djanog command to wait for database."""

    def handle(self, *args, **options):
        pass