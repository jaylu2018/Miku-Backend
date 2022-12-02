from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class MobileValidator(validators.RegexValidator):
    regex = r'1[3-9]\d{9}'
    message = _("手机号码格式不正确")
    flags = 0
