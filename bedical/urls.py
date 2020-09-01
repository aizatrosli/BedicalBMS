from django.conf.urls import url,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bed', views.bedView)
router.register('bedbooking', views.bedbookingView)
router.register('bedmanagement', views.bedmanagementView)
router.register('diagnosis', views.diagnosisView)
router.register('doctor', views.doctorView)
router.register('operationbooking', views.operationbookingView)
router.register('patient', views.patientView)
router.register('payment', views.paymentView)


urlpatterns = [
    url('^api/dashboard/data$', views.DashboardData.as_view()),
    url('^api/search/patient$', views.patientSearchiew.as_view()),
    url('^api/search/doctor$', views.doctorSearchiew.as_view()),
    url(r'^autocomplete/bm/$', views.BedBMAutocomplete.as_view(), name='bm-autocomplete'),
    url('api/', include(router.urls)),

]
