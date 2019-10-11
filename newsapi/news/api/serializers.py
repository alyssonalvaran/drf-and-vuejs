from rest_framework import serializers

from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def validate(self, data):
        """
        checks if title and description don't contain the same content
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Description cannot be the same as the title.")
        return data
    
    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError("Title must have at least 60 characters.")
        return value
