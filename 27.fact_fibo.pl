%factorial
fact(0,1).
fact(N,F):-
  N>0,
  N1 is N-1,
  fact(N1,F1),
  F is N*F1.

  %fibo
% Predicate to print the first N Fibonacci numbers
fib_series(0, []).
fib_series(N, [F|T]) :-
  N > 0,
  N1 is N - 1,
  fib_series(N1, T),
  fibonacci(N, F).

% Predicate to calculate the nth Fibonacci number
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :- N > 1, N1 is N - 1, N2 is N - 2, fibonacci(N1, F1), fibonacci(N2, F2), F is F1 + F2.