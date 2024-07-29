from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blogapp.serializer import UserSerializer,CreatePostSerializer,CommentSerializer
from blogapp.models import Userprofile,CreatePost,Comments
from rest_framework import permissions,authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.

class UserProfileView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=UserSerializer
    queryset=Userprofile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data,context={'user':request.user})
        print(serializer)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
        except:
            return Response({'msg':"invalid"},status=status.HTTP_208_ALREADY_REPORTED)
        
    @action(methods=['post'],detail=True)
    def add_followers(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user_to_follow=Userprofile.objects.get(id=id)
        user_to_follow.followers.add(request.user)
        return Response({"msg":"followed"})
        
class PostCreateView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CreatePostSerializer
    queryset=CreatePost.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer=CreatePostSerializer(data=request.data,context={'user':request.user})
    #     print(serializer)
    #     try:
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data)
    #     except:
    #         return Response({'msg':"invalid"},status=status.HTTP_208_ALREADY_REPORTED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['post'],detail=True)  
    def add_likes(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post_to_like=CreatePost.objects.get(id=id)
        post_to_like.likes.add(request.user)
        return Response({"msg":"likes added"})
    
    @action(methods=['post'],detail=True)
    def add_comments(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post_to_comment=CreatePost.objects.get(id=id)
        serializer=CommentSerializer(data=request.data,context={'user':request.user,'post_to_comment':post_to_comment})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

    
        
