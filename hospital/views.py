from rest_framework import generics
from . serializers import TodoSerializers
from . models import Todo
from . permissions import IsOwnerOnly
from rest_framework import permissions

class TodoList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOnly, permissions.IsAuthenticated)
    serializer_class=TodoSerializers
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        # return super().filter_queryset(queryset)
        return queryset

class TodoDetails(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes = (IsOwnerOnly, permissions.IsAuthenticated)
    serializer_class=TodoSerializers
    queryset = Todo.objects.all()