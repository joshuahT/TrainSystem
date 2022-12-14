from django.db import models


# DONE
class Train(models.Model):
    class Meta:
        db_table = 'train'
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    type = models.CharField(max_length=40)


# DONE
class Personnel(models.Model):
    class Meta:
        db_table = 'personnel'
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    dob = models.DateField()


# DONE
class Passenger(models.Model):
    class Meta:
        db_table = 'passenger'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()


# DONE
class PassengerAddress(models.Model):
    class Meta:
        db_table = 'passenger_address'
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    street = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)


class Station(models.Model):
    class Meta:
        db_table = "station"
    station_name = models.CharField(max_length=100)
    built_year = models.IntegerField(default=2022)


# DONE
class StationAddress(models.Model):
    class Meta:
        db_table = 'station_address'
    station = models.OneToOneField(Station, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)


# DONE
class Trip(models.Model):
    class Meta:
        db_table = "trip"
    travels_on = models.ForeignKey(Train, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)


# DONE
class Stop(models.Model):
    class Meta:
        db_table = "stop"
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_index = models.IntegerField(default=0)
    date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)


# DONE
class Ticket(models.Model):
    class Meta:
        db_table = "ticket"
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    expiration_date = models.DateField()
    is_valid = models.BooleanField()
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    fare = models.FloatField(default=0.0)


# DONE
class ScheduledOn(models.Model):
    class Meta:
        db_table = "scheduled_on"
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


# DONE
class WorkRoster(models.Model):
    class Meta:
        db_table = "work_roster"
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    work_date = models.DateField()