import json
from python_xml_json_explorecourses import xml_to_dictionary


print('hi hello world')
params = {
    # "q": "EDUC101",  # no day time nor location
    "academicYear": "20222023",
    "q": "EDUC147",  # L or not L
}

# params = {
#    "q": "EDUC",
#    "totalSubjectSearch": 1,
# }

dictionary = xml_to_dictionary(**params)
json_object = json.dumps(dictionary, indent=2)
print(json_object)
