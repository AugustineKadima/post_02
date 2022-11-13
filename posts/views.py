from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['POST', 'GET'])
def post_list(request):
    try:
        posts = Post.objects.all()
    except:
        return Exception("Error! Could not fetch posts.")

    if request.method == "GET":
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['PUT', 'GET', 'DELETE'])
def post_detail(response, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Exception("Error: post not found.")

    if response.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, status=200)
    
    elif response.method == 'PUT':
        data = JSONParser.parse(response)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif response.method == 'DELETE':
        post.delete()
        return JsonResponse(status=204)

