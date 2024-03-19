% Facts about birds and whether they can fly
can_fly(sparrow).
can_fly(eagle).
can_fly(albatross).

% Query to check if a particular bird can fly
fly_ability(Bird) :-
    can_fly(Bird),
    format("~w can fly.~n", [Bird]).

fly_ability(Bird) :-
    \+ can_fly(Bird),
    format("~w cannot fly.~n", [Bird]).
