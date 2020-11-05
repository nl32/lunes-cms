from rest_framework import serializers

from .models import Discipline, TrainingSet, Document, AlternativeWord

class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'title', 'description')

class TrainingSetSerializer(serializers.HyperlinkedModelSerializer):
    discipline = DisciplineSerializer()
    class Meta:
        model = TrainingSet
        fields = ('id', 'title', 'description')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    training_set = TrainingSetSerializer()
    class Meta:
        model = Document
        fields = ('id', 'word', 'article', 'image', 'cropping', 'audio')

class AlternativeWordSerializer(serializers.HyperlinkedModelSerializer):
    document = DocumentSerializer()
    class Meta:
        model = AlternativeWord
        fields = ('alt_word', 'document')