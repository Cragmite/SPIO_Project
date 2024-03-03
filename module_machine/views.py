from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MachineSerializer
from .models import Machine

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/machines/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of machines'
        },
        {
            'Endpoint': '/machines/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single machine object'
        },
        {
            'Endpoint': '/machines/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new machine with data sent in post request'
        },
        {
            'Endpoint': '/machines/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing machine with data sent in put request'
        },
        {
            'Endpoint': '/machines/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getMachines(request):
    machines = Machine.objects.all()
    serializer = MachineSerializer(machines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMachine(request, pk):
    machine = Machine.objects.get(id=pk)
    serializer = MachineSerializer(machine, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createMachine(request):
    data = request.data

    machine = Machine.objects.create(
        area=data['area'],
        name=data['name'],
    )
    serializer = MachineSerializer(machine, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateMachine(request, pk):

    try:
        machine = Machine.objects.get(id=pk)
    except Machine.DoesNotExist:
        return Response(status=404)

    # Update area field if provided in request
    machine.area = request.data.get('area', machine.area)
    # Update name field if provided in request
    machine.name = request.data.get('name', machine.name)

    # Save the updated machine
    machine.save()

    # Serialize and return the updated machine
    serializer = MachineSerializer(machine)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMachine(request, pk):
    machine = Machine.objects.get(id=pk)
    machine.delete()
    return Response('Machine was deleted!')