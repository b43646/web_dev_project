from __future__ import absolute_import

from celery import shared_task

from .models import test
import time
@shared_task
def add(x, y):
	add_sum =  x + y
	time.sleep(20)
	add_obj = test(sum=add_sum)
	print str(add_sum)
	add_obj.save()
	print str(add_sum)
	return add_sum



@shared_task
def mul(x, y):
	return x * y


@shared_task
def xsum(numbers):
	return sum(numbers)
