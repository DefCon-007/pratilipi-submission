from webview.models import citites


def getAllCititesName() :
    data = citites.objects.all()
    return [x.name for x in data]
