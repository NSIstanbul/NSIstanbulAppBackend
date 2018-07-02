from django.db.models import Model, CASCADE, \
                              BooleanField, CharField, DateTimeField, \
                              EmailField, ForeignKey, TextField, \
                              URLField
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Company(Model):
    name = CharField(max_length=128)
    email = EmailField(max_length=64, unique=True)
    icon_url = URLField(_("Icon URL"), max_length=1024, null=True, blank=True)
    contact_url = URLField(_('Contact URL'), max_length=1024)

    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name


class CompanyApp(Model):
    company = ForeignKey(Company, on_delete=CASCADE)
    name = CharField(_('App Name'), max_length=128)
    icon_url = URLField(_('Icon URL'), max_length=1024, null=True, blank=True)

    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        verbose_name = _('Company App')
        verbose_name_plural = _('Company Apps')

    def __str__(self):
        return self.name


class Job(Model):
    company = ForeignKey(Company, on_delete=CASCADE)
    position_title = CharField(max_length=256)
    description = TextField(max_length=512)
    city = CharField(max_length=64)
    url = URLField(_('URL'), max_length=1024, null=True, blank=True)

    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.position_title


