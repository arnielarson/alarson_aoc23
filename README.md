# aoc_23

Advent of Code 2023


### Select Problem Notes

- Problem 5 - mapping seeds to locations.  This was pretty interesting, the input was in ranges and each input was mapped multiple times to an end location.  But the ranges were BIG numbers and brute force wasn't going to really work.  I brute force reverse mapped from 0 up to find the SMALLEST location.  Although forward mapping individual numbers would be too much, a little bit of clever code and can apply the mapping directly to the ranges themselves, which makes the mappings far more efficient.

- Problem 7 - included 5 card "poker" like hands with some slightly custom comparison/tie braking logic.  Not too difficult.  Part 2 made J's wild requiring more complex logic to compare hands

- Problem 8 - graph traversal!  I could not get part 2 of this!  Had to peek at someone elsees solution first.  The graph has nodes "XXX" and a 2 layer mapping.  In part 1 had to find how many steps to get from start "AAA" to end "ZZZ".  Answer was around 13000.  Part 2 simultaneously traversed from a set of 6 start nodes..  to get to a set of 6 end nodes simultaneously {Si} to get to 6 end nodes {Ei}.  That be roughly P(E1)^6 which would lead to like huge.  Of course there's a trick.  Each individual Start/End node has a cycle and you can predict the step where they will all simultaneously be met with least common multiple algorithm. 
- Problem 10 - the grid is a graph of pipes.  The pipes form a loop (1D) in the 2D grid.  Part 1 is just to find the furthest point from the start.  Part 2 was much trickier for me. Find the points that are topologically interior, which was much more difficult.

- Problem 12 - again one that I couldn't quite figure out on my own and I had to look at someone elses solution.  ?'s in lines of text are to be replaced with M '.''s and N-M '#''s and the resulting line must match a certain pattern.  Brute force is to just try all permutations.  But that is N!/(N-M)!M! which of course get's huge quick.  Worked for part 1, but for part2 the lines are expanded and a more efficient solutions is needed.  More efficient is to recursively process the line starting at 0, and generate (count) all of the matching solutions.  This is still too long, but you can employ a caching strategy once you start getting tot he end of the first matches, maintain a dictionary of substrings at the end that have completed and the solution goes fast!

- Problem 13 - finding symmetries (reflections) in 2D patterns.  Kind of novel, had to write a lot of code to get it right, also had to reread several times to figure out the constraints.

- Problem 14 - Kind of cool - pretend the grid is like a surface with objects on it, some fixed some that can move (rocks), and the surface can be tilted so that the objects accumulate on a side.  Part 2 is to tilt the surface NWSE 1B times..  My computer can't really do that many computations in a reasonable time, so the trick is to find out how and when the surface gets into a stable subcycle and can predict object locations at later points..
