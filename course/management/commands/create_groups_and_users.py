from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create default groups and users'

    def handle(self, *args, **kwargs):
        # Grupları oluşturma
        admin_group, created = Group.objects.get_or_create(name='Admin')
        trainer_group, created = Group.objects.get_or_create(name='Trainer')
        learner_group, created = Group.objects.get_or_create(name='Learner')

        # Örnek kullanıcıları oluşturma ve gruplara atama

        # Admin kullanıcısı
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(username='admin', password='adminpassword')
            admin_user.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS('Admin user "admin" created and added to "Admin" group.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user "admin" already exists.'))

        # Trainer kullanıcısı
        if not User.objects.filter(username='trainer').exists():
            trainer_user = User.objects.create_user(username='trainer', password='trainerpassword')
            trainer_user.groups.add(trainer_group)
            self.stdout.write(self.style.SUCCESS('Trainer user "trainer" created and added to "Trainer" group.'))
        else:
            self.stdout.write(self.style.WARNING('Trainer user "trainer" already exists.'))

        # Learner kullanıcısı
        if not User.objects.filter(username='learner').exists():
            learner_user = User.objects.create_user(username='learner', password='learnerpassword')
            learner_user.groups.add(learner_group)
            self.stdout.write(self.style.SUCCESS('Learner user "learner" created and added to "Learner" group.'))
        else:
            self.stdout.write(self.style.WARNING('Learner user "learner" already exists.'))

        # Renee kullanıcısı
        if not User.objects.filter(username='renee').exists():
            renee_user = User.objects.create_user(username='renee', password='password')
            renee_user.groups.add(learner_group)
            self.stdout.write(self.style.SUCCESS('User "renee" created and added to "Learner" group.'))
        else:
            self.stdout.write(self.style.WARNING('User "renee" already exists.'))
