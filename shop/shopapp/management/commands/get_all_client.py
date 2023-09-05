from django.core.management import BaseCommand

from shopapp.models import Client


class Command(BaseCommand):
    help = "Get all client."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
