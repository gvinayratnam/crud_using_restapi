from django.shortcuts import render
from . models import BookModel
from . serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def Booklist(request):
    bookobj = BookModel.objects.all() #queryset
    serializer = BookSerializer(bookobj,many=True)
    return Response(serializer.data)

@api_view(['post'])
def post_Booklist(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['post'])
def update_Booklist(request,id):
    print(id)
    bookobj = BookModel.objects.get(id=id)
    serializer = BookSerializer(instance = bookobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def dele_book(request,id):
    print(id)
    book_obj = BookModel.objects.get(id=id)
    book_obj.delete()
    return Response('book is deleted')

