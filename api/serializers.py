from rest_framework import serializers

from blog.models import Blog, User, Entry


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'name',
            'tagline',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
        ]


class EntrySerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    authors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = [
            'id',
            'blog',
            'headline',
            'body_text',
            'pub_date',
            'mod_date',
            'authors',
            'n_comments',
            'n_pingbacks',
            'rating'
        ]