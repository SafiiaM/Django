from django.core.management.base import BaseCommand
from myapp2.models import User
from datetime import datetime


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(1, 100):
        #user = User(name='John', email='john@example.com', password='secret', age=25)
        #user = User(name='Neo', email='neo@example.com', password='secret', age=58)
            user = User(
                name=f'Jack{i}', 
                email=f'captain{i}@example.com', 
                password='secret*', 
                phone=8521145226, 
                address="17 Street Popov", 
                age=60, 
                date_reg=datetime(2024, 1, 1)
            )
            user.save()
            self.stdout.write(f'{user}')