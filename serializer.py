from rest_framework import serializers
from blogapp.models import Userprofile,CreatePost,Comments

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Userprofile
        fields=['id','image','dob','bio','user']

    def create(self, validated_data):
        user=self.context.get('user')
        return Userprofile.objects.create(user=user,**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        fields=['user','post','comment']

    def create(self, validated_data):
        user=self.context.get("user")
        post=self.context.get("post")
        return Comments.objects.create(user=user,post=post,**validated_data)

    
class CreatePostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    likes_count=serializers.IntegerField(read_only=True)
    comment=CommentSerializer(read_only=True,many=True)
    comment_count=serializers.CharField(read_only=True)
    class Meta:
        model=CreatePost
        fields=['image','title','content','user','date','likes','likes_add','comment','comment_count']
