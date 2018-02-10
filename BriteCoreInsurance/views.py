from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def db_get_risktype(request, id):
    """
    :param request: HTTP Request object
    :param id: ID of the Risk Type
    :return: Risk Type with table definitions as a JSON
    """
    try:
        # TODO: Fetch risk from models.py
        pass
    except ObjectDoesNotExist:
        return HttpResponse('Risk Type with the given ID not found', status=404)


def db_get_allrisks(request):
    """

    :param request: HTTP Request object
    :return: All Risk Types with table definitions as a JSON
    """
    try:
        # TODO: Fetch all risks from models.py
        pass
    except ObjectDoesNotExist:
        return HttpResponse('No Risk Types found', status=404)
