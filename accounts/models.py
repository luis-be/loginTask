from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Gestor de usuarios para manejar creación de usuarios y superusuarios."""

    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        extra_fields.setdefault('is_active', True)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('El superusuario debe tener is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(correo_electronico, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nombre_de_usuario = models.CharField(
        _('Nombre de Usuario'),
        max_length=150,
    )
    correo_electronico = models.EmailField(
        _('Correo Electrónico'),
        unique=True,
    )
    edad = models.PositiveIntegerField(_('Edad'), default=0, blank=True)
    is_staff = models.BooleanField(
        _('Estado de Personal'),
        default=False,
        help_text=_('Indica si el usuario puede acceder al sitio de administración.'),
    )
    is_superuser = models.BooleanField(
        _('Estado de Superusuario'),
        default=False,
        help_text=_('Indica si el usuario tiene todos los permisos.'),
    )
    is_active = models.BooleanField(
        _('Activo'),
        default=True,
        help_text=_('Indica si este usuario está activo.'),
    )
    date_joined = models.DateTimeField(_('Fecha que se unió'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'correo_electronico'
    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_de_usuario']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'

    def clean(self):
        super().clean()
        self.correo_electronico = self.__class__.objects.normalize_email(self.correo_electronico)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.correo_electronico], **kwargs)
