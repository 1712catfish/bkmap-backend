from rest_framework import serializers

from base.models import Post


class PostSerializer(serializers.ModelSerializer):
    latlng = serializers.CharField(max_length=256)
    text = serializers.CharField(max_length=256)

    class Meta:
        model = Post
        fields = '__all__'
