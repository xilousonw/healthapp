from django.test import TestCase

# Create your tests here.

from uuid import uuid4
import time

def create_userid():
    str1 = uuid4()
    print(str1)
    str2 = time.time()
    print(str2)
    final_str = str1+str2
    return final_str


res = create_userid()
print(res)
