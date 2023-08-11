from rest_framework import serializers

from .models import Product, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    # category = (
    #     CategorySerializer()
    # )  # Use the CategorySerializer to display category name
    # tags = TagSerializer(many=True)

    class Meta:
        fields = "__all__"
        # (
        #     "id",
        #     "name",
        #     "description",
        #     "category",
        #     "price",
        #     "created_at",
        #     "tags",
        # )
        read_only_fields = ["created_at"]
        model = Product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_name = instance.category.name if instance.category else None
        representation["category"] = category_name
        # representation["category"] = representation["category"]["name"]
        tag_names = [tag.name for tag in instance.tags.all()]
        representation["tags"] = tag_names
        # representation["tags"] = [tag["name"] for tag in representation["tags"]]
        return representation
