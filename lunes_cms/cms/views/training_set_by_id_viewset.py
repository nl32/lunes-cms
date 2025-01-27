from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from ..models import TrainingSet, GroupAPIKey
from ..serializers import TrainingSetSerializer
from ..utils import get_key


class TrainingSetByIdViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Defines a view set for a TrainingSet module of a given id.
    Inherits from `viewsets.ReadOnlyModelViewSet` and defines queryset
    and serializers.
    """

    serializer_class = TrainingSetSerializer

    def get_queryset(self):
        """
        Defining custom queryset

        :param self: A handle to the :class:`TrainingSetViewSet`
        :type self: class

        :return: (filtered) queryset
        :rtype: QuerySet
        """
        if getattr(self, "swagger_fake_view", False):
            return TrainingSet.objects.none()
        queryset = TrainingSet.objects.filter(released=True).annotate(
            total_documents=Count(
                "documents",
                filter=Q(documents__document_image__confirmed=True),
                distinct=True,
            )
        )
        key = get_key(self.request)
        if key:
            try:
                queryset = queryset.filter(
                    created_by=GroupAPIKey.objects.get_from_key(key).organization
                )
            except GroupAPIKey.DoesNotExist:
                raise PermissionDenied()
        else:
            queryset = queryset.filter(creator_is_admin=True)
        return queryset
