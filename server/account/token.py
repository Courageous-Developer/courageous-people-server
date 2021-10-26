import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationToken(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.is_active)


account_activation_token = AccountActivationToken()
