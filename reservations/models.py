import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models
from . import managers

class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"  # 예약 대기 : 예약만 하고 결제 x
    STATUS_CONFIRMED = "confirmed"  # 예약 확정 : 결제까지 완료돼 예약이 확정된 상태
    STATUS_CANCELED = "canceled"  # 예약 취소

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    objects = managers.CustomReservationManager()

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):  # 현재 날짜가 check_in 날짜보다 큰지,
        # checkout 날짜보다 작은지를 체크
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            start = self.check_in
            end = self.check_out
            difference = end - start
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            if not existing_booked_day:
                super().save(*args, **kwargs)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    BookedDay.objects.create(day=day, reservation=self)
                return
        return super().save(*args, **kwargs)
