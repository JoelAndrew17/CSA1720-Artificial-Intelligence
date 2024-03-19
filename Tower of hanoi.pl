% Define the predicate to solve Towers of Hanoi
hanoi(1, Start, _, End, [move(Start, End)]).
hanoi(N, Start, Helper, End, Moves) :-
    N > 1,
    M is N - 1,
    hanoi(M, Start, End, Helper, FirstMoves),
    hanoi(1, Start, _, End, LastMove),
    hanoi(M, Helper, Start, End, SecondMoves),
    append([FirstMoves, LastMove, SecondMoves], Moves).

% Predicate to print the list of moves
print_moves([]).
print_moves([move(Start, End) | Tail]) :-
    format("Move from ~w to ~w~n", [Start, End]),
    print_moves(Tail).

% Predicate to solve Towers of Hanoi with N disks
solve_hanoi(N) :-
    hanoi(N, left, middle, right, Moves),
    print_moves(Moves).

% Example usage:
% ?- solve_hanoi(3).
