from rest_framework.serializers import ModelSerializer
from xpense_users.models.users import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'