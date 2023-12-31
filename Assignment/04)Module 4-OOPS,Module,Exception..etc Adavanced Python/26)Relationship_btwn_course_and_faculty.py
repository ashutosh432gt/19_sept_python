# What relationship is appropriate for Course and Faculty?
# A course is associated with a faculty. 
# This typically implies a one-to-many relationship, 
# where one faculty member can be associated with multiple
# courses. You might have a Course class with a faculty member 
# as an attribute or a list of faculty members if there can be multiple instructors.

class Course:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

class Faculty:
    def __init__(self, name):
        self.name = name
