git clone this repo to test that the python_xml_json_explorecourses pip package works.

- cd /tmp
- git clone https://github.com/gsedevops/explorecourses_python_package_test 
- cd explorecourses_python_package_test
- pipenv install
- pipenv run python main.py

To verify the package is working, you should see output similar to the following.

```
$ pipenv run python main.py 
hi hello world
{
  "subject": "EDUC",
  "code": "147",
  "title": "Stanford and Its Worlds: 1885-present (HISTORY 58E)",
  "year": "2022-2023",
  "grading": "Letter or Credit/No Credit",
  "description": "The past and future of Stanford University examined through the development of four critical &quot;worlds,&quot; including the Western region of the United States, the US nation-state, the global academy, and the complex phenomena summarized by the name Silicon Valley. Students are asked to consider and theorize these worlds, their interrelationships, and the responsibilities they entail for all of us who live and work at Stanford in the present moment.",
  "term": [
    "2022-2023 Spring"
  ],
  "format_of_course": "LEC",
  "section_units": "3",
  "unitsMin": "3",
  "unitsMax": "3",
  "days": [
    "Monday",
    "Wednesday"
  ],
  "instructors": [
    "Emily Levine",
    "Mitchell Stevens"
  ],
  "tags": "Higher_Ed; History; Undergraduate",
  "sections": [
    {
      "subject": "EDUC",
      "code": "147",
      "term": "2022-2023 Spring",
      "format_of_course": "LEC",
      "sectionNumber": "01",
      "section_units": "3",
      "unitsMin": "3",
      "unitsMax": "3",
      "startTime": "9:30am",
      "endTime": "11:20am",
      "location": "Ceras 300",
      "days": "Monday Wednesday",
      "instructor_name": "Emily Levine; Mitchell Stevens"
    }
  ],
  "explorecourses_url": "https://explorecourses.stanford.edu/search?academicYear=20222023catalog&q=EDUC147",
  "explorecourses_xml": "https://explorecourses.stanford.edu/search?academicYear=20222023&view=xml-20200810&q=EDUC147",
  "coursediscovery_url": "https://coursediscovery.gse.stanford.edu/node/courses/educ-147-2024-2025",
  "section_count": 1,
  "course_offered": true,
  "course_valid": true,
  "program": [],
  "category": [
    "Higher_Ed",
    "History"
  ],
  "audience": [
    "Undergraduate"
  ]
}

```

