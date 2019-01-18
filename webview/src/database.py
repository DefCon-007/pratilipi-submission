from webview.models import citites, pvrusers


def getAllCititesName() :
    data = citites.objects.all()
    return [x.name for x in data]

def getAllUsersByCity(city) :
    data = pvrusers.objects.filter(city__name=city)
    res = []
    for d in data :
        res.append({
            "fname" : d.first_name,
            "lname" : d.last_name,
            "email" : d.email,
        })
    return res