import datetime
STATUS_NEW = 0
STATUS_ACCEPTED = 1

STATUS_CHOICES = {
    (STATUS_NEW, 'New'),
    (STATUS_ACCEPTED, 'Accepted'),
}

STATUS_CHOICES_DICT = dict(STATUS_CHOICES)
print(STATUS_CHOICES_DICT)
print(type(STATUS_CHOICES))
print(STATUS_CHOICES_DICT[0])
