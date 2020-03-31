import requests
import ipdb

# Lists, tuples, and sets

"""
## Lists
 * You can modify a list
 * It keeps it's order
"""

l = ["Jane", "Stacy", "Anna"]
#print(l[0]) # Subscript notation
"""
l[1] = "Laura"
l.append("Amanda")
l.remove("Anna")"""
the_list = [{'id': 123, 'name': "ClickFunnels", 'popularity': 10, 'version': 1}, {'id': 124, 'name': "ClickFunnels", 'popularity': 10, 'version': 2}, {
    'id': 128, 'name': "Zoho Books", 'popularity': 200, 'version': 2}, {'id': 125, 'name': "FBLA", 'popularity': 10000, 'version': 2}]
ipdb.set_trace()
sorted_by_popularity = sorted(the_list, key=lambda x: x['name'], reverse=True)


"""
## Tuples
 * You can't modify a tuple
 * It keeps it's order
 * Mostly used for package data
 * Django uses this in get or create functions
"""
# t = ("Jane", "Stacy", "Anna")
# print(t[0]) # Subscript notation
# t[1] = "Laura" # Errors
# t.append("Amanda") # Errors
# t.remove("Anna") # Errors
"""
r = requests.get('https://hooks.zapier.com/hooks/catch/1867581/o1pr4xx/')

def create_response_tuple(response):
    return (response.status_code, response.json())

response_tuple = create_response_tuple(r)
ipdb.set_trace()

print("the end")
"""

"""
obj, created = Whatever.objects.get_or_create(name='thingymabob')
the_result_tuple = Whatever.objects.get_or_create(name='thingymabob')
obj, created = the_result_tuple
the_result_tuple[0] == obj

def notify_when_whataver_created():
    name = 'thingymabob'
    obj, created = Whatever.objects.get_or_create(name=name)

    if created:
        print("Hey you just created {}".format(obj.name))
"""
"""
## Sets
 * You can modify a set
 * Duplicates are not allowed
 * The order isn't guaranteed
 * You cannot use subscript notation to access items

s = {"Jane", "Stacy", "Anna"}
# print()
s.add("Anna") # Append adds at the end, since order isn't guaranteed you can't append
s.add("Anna") # Ignored as duplicates aren't allowed
"""
s = {"Jane", "Stacy", "Anna"}
the_set = set()
the_set = {item['name'] for item in the_list}

if "ClickFunnels" in the_set:
    ipdb.set_trace()
    print('Oh you poor poor man')
    the_set.remove("ClickFunnels")

ipdb.set_trace()
print('the actual end')

unique_ids = {item['id'] for item in the_list}
print(len(unique_ids))

# Advanced set operations

friends = {"Jane", "Stacy", "Anna"}
local = {"Stacy"}
abroad = {"Jane", "Anna"}


# difference() takes one set and removes elements of another set from it
local_friends = friends.difference(abroad)
abroad_friends = abroad.difference(friends)
print(local_friends)
print(abroad_friends)  # Returns an empty set as all items are removed


# union() unites two sets, remember duplicates are ignored
print(local.union(abroad))


# intersection() returns items that appear in both sets
art = {"Jane", "Stacy", "Amanda", "Laura"}
science = {"Jane", "Stacy", "Anna", "Lucy"}
print(art.intersection(science))
