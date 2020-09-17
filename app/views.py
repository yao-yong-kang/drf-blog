from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response

from .serializers import UserSerializer,ArticleSerializer
from .models import Article,Category
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#fbv @api_view
@api_view(['GET'])
def article_list(request):
    """
    这是文章列表
    :param request:
    :return:
    """
    if request.method=='GET':
        reponse_data = ArticleSerializer(instance=Article.objects.all(), many=True)
        return Response(reponse_data.data, status=status.HTTP_200_OK)
def article_detail(request,pk):
    pass

