from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer


class MemberViews(viewsets.ModelViewSet):
    """Dynamic View for the model

    Arguments:
        viewsets {[type]} -- [description]
    """

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
