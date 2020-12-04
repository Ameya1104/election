from django.contrib import admin
from .models import Election, Constituency, Election_officer, Party, Candidate, Voter, Election_Result

# Register your models here.
admin.site.register(Election)
admin.site.register(Constituency)
admin.site.register(Election_officer)
admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Election_Result)