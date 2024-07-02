from rest_framework.serializers import ModelSerializer
from notifications.models import Notification

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        #fields = '__all__' # Esto no es recomendable
        fields = ['uuid','body','email','title','created','modified']

"""
{
    "body":"body1",
    "email":"email1@mail.com",
    "title":"title 1",
}
"""