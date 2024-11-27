from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser, PermissionsMixin):
    nombre_de_usuario = models.CharField(
        _('Nombre de Usuario'),
        max_length=150,
    )
    correo_electronico = models.EmailField(
        _('Correo Electrónico'),
        unique=True,
    )
    edad = models.PositiveIntegerField(_('Edad'), default=0, blank=True)  # edad
    es_superusuario = models.BooleanField(default=False)
    es_personal = models.BooleanField(_('Es Personal'), default=False)
    esta_activo = models.BooleanField(_('Está activo'), default=True)
    fecha_union = models.DateTimeField(_('Fecha que se unió'), default=timezone.now)

    objects = UserManager()

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