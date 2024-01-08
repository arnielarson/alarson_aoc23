# aoc_23

Advent of Code 2023

https://adventofcode.com/2023/about

### Take Away

I began these "exercises" without any knowledge of what it would be like or where it would go.  The problems turned out to be engaging and novel and often quite interesting and challenging.  It scratched the part of my brain where algorithms used to reside and I dusted off some of the cobwebs there.  Many of the puzzles I was able to complete on a first go in one sitting.  Some of the part 2's were too difficult to figure out on my own and I resorted to looking at how others approached them.  I learned a few things in the process and remembered many a thing I've studied in the past.  I hope that if life permits I'll try it again next year.

### Select Problem Notes

- Problem 5 - mapping seeds to locations.  First sort of difficult problem.. This was pretty interesting, the input was in ranges and each input was mapped multiple times to an end location.  But the ranges were BIG numbers and brute force wasn't going to really work.  I brute force reverse mapped from 0 up to find the SMALLEST location.  Although forward mapping individual numbers would be too much, a little bit of clever code and can apply the mapping directly to the ranges themselves, which makes the mappings far more efficient.

- Problem 7 - included 5 card "poker" like hands with some slightly custom comparison/tie braking logic.  Not too difficult.  Part 2 made J's wild requiring more complex logic to compare hands

- Problem 8 - graph traversal!  I could not get part 2 of this!  Had to peek at someone elsees solution first.  The graph has nodes "XXX" and a 2 layer mapping.  In part 1 had to find how many steps to get from start "AAA" to end "ZZZ".  Answer was around 13000.  Part 2 simultaneously traversed from a set of 6 start nodes..  to get to a set of 6 end nodes simultaneously {Si} to get to 6 end nodes {Ei}.  That be roughly P(E1)^6 which would lead to like huge.  Of course there's a trick.  Each individual Start/End node has a cycle and you can predict the step where they will all simultaneously be met with least common multiple algorithm. 
- Problem 10 - the grid is a graph of pipes.  The pipes form a loop (1D) in the 2D grid.  Part 1 is just to find the furthest point from the start.  Part 2 was much trickier for me. Find the points that are topologically interior, which was much more difficult.

- Problem 12 - again one that I couldn't quite figure out on my own and I had to look at someone elses solution.  ?'s in lines of text are to be replaced with M '.''s and N-M '#''s and the resulting line must match a certain pattern.  Brute force is to just try all permutations.  But that is N!/(N-M)!M! which of course get's huge quick.  Worked for part 1, but for part2 the lines are expanded and a more efficient solutions is needed.  More efficient is to recursively process the line starting at 0, and generate (count) all of the matching solutions.  This is still too long, but you can employ a caching strategy once you start getting tot he end of the first matches, maintain a dictionary of substrings at the end that have completed and the solution goes fast!  This is an example of dynamic programming or a "greedy" algorithm.  

- Problem 13 - finding symmetries (reflections) in 2D patterns.  Kind of novel, had to write a lot of code to get it right, also had to reread several times to figure out the constraints.

- Problem 14 - Kind of cool - pretend the grid is like a surface with objects on it, some fixed some that can move (rocks), and the surface can be tilted so that the objects accumulate on a side.  Part 2 is to tilt the surface NWSE 1B times..  My computer can't really do that many computations in a reasonable time, so the trick is to find out how and when the surface gets into a stable subcycle and can predict object locations at later points..

- Problem 17 - travelling through a map minimizing some cost.  Obviously a heap problem although in my first implementation I did just do a sort on the list of frontier nodes.  I later figured out how to use the heapq package from Python which I know I've done in the past.

- Problem 18 - Another topological interior / exterior problem.  Spent a lot of time trying to find a generative solution that was better than what'd I'd done in 10.  I did and it was fun and somewhat novel but had no hope of solving part b :)  I had to again peak at someone elses solution to realize that you really need some math, Pick's theorem and some geometry to get the solution.


- Problem 19 - processing workflows recursively.  Interesting problem to organize code around.  I ended up creating a workflow class to organize my code.  This lead to solution to part2 where instead of mapping numbers through the workflow, can map ranges, which either map entirely on each step, or at most bifurcate into two ranges, and propagate through workflow.

- Problem 20 - Implement a simulation for comms modules.  Primay miodueles include "flip flops", Conjunctions, both can have multiple outputs, and conjunctions can have multiple inputs.  Also a button, broadcast (which just propagates signal to multiple outputs) and an output (which terminates that pulse.  Implemented modules as classes and used queue to maintain correct ordering of when pulses actuate.  Fun problem, goal is to simulate button presses and part 2 requires looking for cycling behavior.


- Problem 21 - Path finding in grid, given N steps how many locations can you end on...  Part2 is big, allowing the grid to repeat itself infitintely and allowing for MANY steps.  (Did not get part 2)  Would require some math and exploiting the symmetry in the grid..


- Problem 23 - Again Path finding, part 1 with constraints, naive solution where I ennumerate all paths works fine.. Part 2 eliminate constraints and find the longest path.  Seems like you have to explor all paths, my algorithm took up too much memory I think.

- Problem 24 - Hailstones (x,y,z,vx,vy,vz), part 1 is find if paths in (x,y) plane intersect for t>0..  Interesiting implementations.  Part 2 is to find a single "rock" that position and velocity that will collide with all of the hailstones..  Therefore system must be massively overdetermined..

- Problem 25 - COULDN'T GET!!  A modest graph (1500 nodes, 3500 edges) find the 3 edges that can be cut to create two disparate sub graphs..  Naive algorithm (3500^3) try each combination, check if graph is disconnected, is way too much computation.  I was unable to come up with a probablistic algorithm that could identify the min cuts.  So now I may try to implement Karger's random cut algorithm to see if I can find the min cut.. 

