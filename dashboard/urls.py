
from django.urls.conf import include, path


urlpatterns = [
    path('', include('dashboard.api.urls'))
]
