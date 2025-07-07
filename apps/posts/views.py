from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.files.storage import default_storage

from apps.posts.serializers import PostSerializer
from apps.posts.utils.posts import save_post, get_user_posts

class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            return Response({'error': 'Заполните заголовок и содержание'}, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.FILES.get('image')
        image_path = None

        if image_file:
            image_path = default_storage.save(f'post_images/{image_file.name}', image_file)

        post = save_post(request.user.id, title, content, image_path)
        return Response(post, status=status.HTTP_201_CREATED)

class PostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = get_user_posts(request.user.id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)