from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    image = serializers.CharField(allow_null=True, required=False)
