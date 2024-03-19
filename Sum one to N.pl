sum(0,0).
sum(N,Result):-
	N>0,
	M is N-1,
	sum(M,Sub),
	Result is N + Sub.
