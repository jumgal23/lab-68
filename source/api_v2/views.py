import json
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from webapp.models import Article
from api_v2.serializers import ArticleSerializer, ArticleModelSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def json_echo_view(request, *args, **kwargs):
    answer = {
        'message': 'Hello World!',
        'method': request.method
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    return JsonResponse(answer)


class ArticleView(APIView):
    #
    # def get(self, request, *args, **kwargs):
    #     # article = Article.objects.first()
    #     # serializer = ArticleSerializer(article)
    #     # print(serializer.data)
    #     # return JsonResponse(serializer.data)
    #     articles = Article.objects.order_by('-created_at')
    #     articles_list = ArticleModelSerializer(articles, many=True).data
    #     return Response(articles_list)
    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleModelSerializer(data=request.data)
        # if serializer.is_valid():
        #     article = serializer.save()
        #     return JsonResponse(serializer.data, safe=False)
        # return JsonResponse({'error': serializer.errors}, status=400)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def put(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleModelSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({"key": pk}, status=status.HTTP_204_NO_CONTENT)
