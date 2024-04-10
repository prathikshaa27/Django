import os
from django.conf import settings
settings.configure()


from django.http import QueryDict

new_query = 'a=1&a=2&c=3'
query_dict = QueryDict(new_query)
print(query_dict)

query_dict = QueryDict.fromkeys(['p','q','r'],value="num")
print(query_dict)

#returns the value for the given key
to_retrive_key = query_dict['q']
print(to_retrive_key)

#setting the key
#uery_dict['s'] = 'new number'
print(query_dict)
print('a' in query_dict)

to_set_default = query_dict.get('s','default')
print(to_set_default)
