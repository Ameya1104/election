from django.urls import path
from . import views
from .views import IndexView, ElectionView, ResultLSView, ResultVSView, AddVoter, DeleteVoter, VoterDetails, IndiVoterDetails, EditVoterView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('election/<int:pk>', ElectionView.as_view(), name = 'elections_view'),
    path('results/loksabha', ResultLSView.as_view(), name = 'results_ls_view'),
    path('results/vidhansabha', ResultVSView.as_view(), name = 'results_vs_view'),
    path('voter', AddVoter.as_view(), name = 'add_voter'),
    path('voter/<int:pk>/delete', DeleteVoter.as_view(), name = 'delete_voter'),
    path('voter/details/', VoterDetails.as_view(), name = 'voter_detail'),
    path('voter/details/<int:pk>', IndiVoterDetails.as_view(), name = 'indi_voter_detail'),
    path('voter/edit/<int:pk>/', EditVoterView.as_view(), name = 'update_voter'),
]