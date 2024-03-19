% Subject codes
subject_code(math, m101).
subject_code(science, s202).
subject_code(history, h303).
subject_code(english, e404).

% Teachers and the subjects they teach
teaches(john, math, m101).
teaches(lisa, science, s202).
teaches(mike, history, h303).
teaches(sarah, english, e404).

studies(jack, math, m101).
studies(emma, science, s202).
studies(alex, history, h303).
studies(lily, english, e404).
%query
course(Code,Subject,Teacher,Student):-
teaches(Teacher,Subject,Code),
studies(Student,Subject,Code).
