from django.contrib.auth import get_user_model
from django.core.validators import ValidationError
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer, EmailField, CharField
from rest_framework.authtoken.models import Token


User = get_user_model()


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label=_("Email Address"), required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'token',

        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def validate(self, data):
        email = data.get('email', None)
        username = data.get("username", None)
        password = data["password"]

        if not email and not username:
            raise ValidationError(_('A username or an email is required'))

        user = User.objects.filter(
            Q(username=username) |
            Q(email=email)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError(_('This email or username is not valid.'))
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError(_("Incorrect password. Please try again."))

        token = Token.objects.create(user=user_obj)
        print(token.key)
        return data


