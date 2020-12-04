from django.db import models
from datetime import date

# Create your models here.
class Election(models.Model):
    e_id = models.IntegerField(primary_key = True)
    state = models.CharField(max_length = 20, blank=True)
    date_of_elections = models.DateField()
    purpose = models.CharField(max_length = 25, blank=True)

    def __str__(self):
        return str(self.e_id) + ' - ' + self.purpose + ' - ' + self.state

class Constituency(models.Model):
    consti_id = models.IntegerField(primary_key = True)
    ward = models.CharField(max_length = 20, blank=True)
    state = models.CharField(max_length = 20, blank=True)

    def __str__(self):
        return str(self.consti_id) + ' - ' + self.ward + ' - ' + self.state

class Election_officer(models.Model):
    ec_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20, blank=True)
    consti_id = models.ForeignKey(Constituency, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.ec_id) + ' - ' + self.name + ' - ' + str(self.consti_id.ward)

class Party(models.Model):
    p_id = models.IntegerField(primary_key = True)
    party_name = models.CharField(max_length = 20, blank=True)
    symbol = models.CharField(max_length = 20, blank=True)

    def __str__(self):
        return str(self.p_id) + ' - ' + self.party_name + ' - ' + self.symbol

class Candidate(models.Model):
    c_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20, blank=True)
    age = models.IntegerField()
    sex = models.CharField(max_length = 1)
    m_status = models.CharField(max_length = 1)
    consti_id = models.ForeignKey(Constituency, on_delete = models.CASCADE)
    e_id = models.ForeignKey(Election, on_delete = models.CASCADE)
    p_id = models.ForeignKey(Party, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.c_id) + ' - ' + self.name + ' - ' + str(self.age) + ' - ' + str(self.p_id.party_name)

class Voter(models.Model):
    v_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20, blank=True)
    a_id = models.IntegerField()
    age = models.IntegerField()
    dob = models.DateField()
    sex = models.CharField(max_length = 1)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length=25)
    city = models.CharField(max_length = 20, blank=True)
    state = models.CharField(max_length = 20, blank=True)    

    def __str__(self):
        return str(self.v_id) + ' - ' + self.name

class Election_Result(models.Model):
    date_of_result = models.DateField()
    vote_count = models.IntegerField()
    c_id = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    e_id = models.ForeignKey(Election, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.date_of_result) + ' - ' + str(self.e_id.e_id) + ' - ' + str(self.c_id.name)+ ' - ' + str(self.vote_count)