from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Member model
    Arguments:
        serializers {[type]} -- [description]
    """
    class Meta:
        model = Member
        fields = ('url', 'id', 'name', 'week1task', 'leaderforWeek')
