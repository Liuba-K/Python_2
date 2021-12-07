from itertools import islice
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Денис', 'Саша'
    ]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

#student_class = {tutor: klass for tutor, klass in zip(tutors, klasses)}
student_class = (tuple([tutor, klass]) for tutor, klass in zip(tutors, klasses))
#student_class = (tuple([tutor, klass]) if len(tutors) <= len(klasses) else tuple([tutor, "None"]) for tutor, klass in zip(tutors, klasses))#tutor mo
for tup in student_class:
    print(tup)
print(list(islice(student_class, 1)))

