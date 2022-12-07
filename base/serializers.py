from rest_framework import serializers

from base.models import Post, Task


class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    subtitle = serializers.CharField(max_length=256)
    latlng = serializers.CharField(max_length=256)

    class Meta:
        model = Post
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    collector = serializers.CharField(max_length=256)
    janitor = serializers.CharField(max_length=256)
    vehicle = serializers.CharField(max_length=256)
    MCP = serializers.CharField(max_length=256)

    class Meta:
        model = Task
        fields = '__all__'
