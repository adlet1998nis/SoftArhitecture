from django.http import JsonResponse


def get_name(request):
    return JsonResponse({'name': 'Adlet'})


def get_surname(request):
    return JsonResponse({'surname': 'Balzhanov'})


def get_id(request):
    return JsonResponse({'id': '123'})


def get_additional_message(request):
    return JsonResponse({'msg': 'How are you doing?'})
