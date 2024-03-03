from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FailureSerializer
from .models import Failure

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/failures/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of failures'
        },
        {
            'Endpoint': '/failures/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single failure object'
        },
        {
            'Endpoint': '/failures/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new failure with data sent in post request'
        },
        {
            'Endpoint': '/failures/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing failure with data sent in put request'
        },
        {
            'Endpoint': '/failures/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getFailures(request):
    failures = Failure.objects.all()
    serializer = FailureSerializer(failures, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFailure(request, pk):
    failure = Failure.objects.get(id=pk)
    serializer = FailureSerializer(failure, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createFailure(request):
    data = request.data

    failure = Failure.objects.create(
        category=data['category'],
        name=data['name'],
    )
    serializer = FailureSerializer(failure, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateFailure(request, pk):

    try:
        failure = Failure.objects.get(id=pk)
    except Failure.DoesNotExist:
        return Response(status=404)

    # Update category field if provided in request
    failure.category = request.data.get('category', failure.category)
    # Update name field if provided in request
    failure.name = request.data.get('name', failure.name)
    
    # Save the updated failure
    failure.save()

    # Serialize and return the updated failure
    serializer = FailureSerializer(failure)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteFailure(request, pk):
    failure = Failure.objects.get(id=pk)
    failure.delete()
    return Response('Failure was deleted!')