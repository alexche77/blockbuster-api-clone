from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Blockbuster Clone."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    @cached_property
    def is_staff_member(self):
        return self.groups.filter(name=["Admins", "Staff"]).exists()

    @cached_property
    def is_admin_member(self):
        return self.groups.filter(name="Admins").exists()
