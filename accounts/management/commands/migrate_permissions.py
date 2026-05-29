from django.core.management.base import BaseCommand
from accounts.models import User
from accounts.permission_templates import get_permissions_for_role

class Command(BaseCommand):
    help = 'Migrates existing users to granular permissions based on their role.'

    def handle(self, *args, **options):
        users = User.objects.all()
        updated_count = 0

        for user in users:
            new_perms = get_permissions_for_role(user.role)
            # Only update if they don't have permissions or we want to reset
            if not user.permissions or user.permissions != new_perms:
                user.permissions = new_perms
                user.save(update_fields=['permissions'])
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f'Updated permissions for {user.username} ({user.role})'))

        self.stdout.write(self.style.SUCCESS(f'Successfully migrated {updated_count} users.'))
