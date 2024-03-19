dob(bjay,'15/3/1947').
dob(jam,'25/2/2005').
dob(gari,'25/2/2005').
dob(joel,'18/4/2006').

%query
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).
