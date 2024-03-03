from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer
from .models import Ticket
from module_machine.models import Machine
from module_failure.models import Failure

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/tickets/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of tickets'
        },
        {
            'Endpoint': '/tickets/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single ticket object'
        },
        {
            'Endpoint': '/tickets/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new ticket with data sent in post request'
        },
        {
            'Endpoint': '/tickets/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing ticket with data sent in put request'
        },
        {
            'Endpoint': '/tickets/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getTickets(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(ticket, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTicket(request):
    data = request.data

    # Retrieve machine instance from the database
    machine_id = data.get('machine')
    machine = Machine.objects.get(pk=machine_id)
    
    # Retrieve failure instance from the database
    failure_id = data.get('failure')
    failure = Failure.objects.get(pk=failure_id)

    ticket = Ticket.objects.create(
        description=data['description'],
        machine=machine,
        failure=failure
    )
    serializer = TicketSerializer(ticket, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTicket(request, pk):

    try:
        ticket = Ticket.objects.get(id=pk)
    except Ticket.DoesNotExist:
        return Response(status=404)

    # Update description field if provided in request
    ticket.description = request.data.get('description', ticket.description)
    # Update machine field if provided in request
    machine_id = request.data.get('machine')
    if machine_id is not None:
        try:
            machine = Machine.objects.get(pk=machine_id)
            ticket.machine = machine
        except Machine.DoesNotExist:
            return Response({'error': 'Machine with provided ID does not exist'}, status=400)
    # Update failure field if provided in request
    failure_id = request.data.get('failure')
    if failure_id is not None:
        try:
            failure = Failure.objects.get(pk=failure_id)
            ticket.failure = failure
        except Failure.DoesNotExist:
            return Response({'error': 'Failure with provided ID does not exist'}, status=400)
    # Save the updated ticket
    ticket.save()

    # Serialize and return the updated ticket
    serializer = TicketSerializer(ticket)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return Response('Ticket was deleted!')