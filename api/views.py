from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bible_Book
from .serializers import BibleBookSerializer


# Create your views here.
@api_view(["POST"])
def api_home(request):
    serializer = BibleBookSerializer(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()
        print(serializer.data)

        return Response(serializer.data)
    else:
        return Response({"status": "fail", "message": "Invalid data passed!"})
