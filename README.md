# k-bandit Exercise



----
## What is it?

The exercise is from the [Sutton and Barto Reinforcement Learning book](https://webdocs.cs.ualberta.ca/~sutton/book/the-book.html) second draft.

> Exercise 2.3 (programming) Design and conduct an experiment to demonstrate
the difficulties that sample-average methods have for nonstationary problems. Use a
modified version of the 10-armed testbed in which all the q∗(a) start out equal and
then take independent random walks. Prepare plots like Figure 2.2 for an actionvalue
method using sample averages, incrementally computed by α =
1
n
, and another
action-value method using a constant step-size parameter, α = 0.1. Use ε = 0.1 and,
if necessary, runs longer than 1000 steps.


----
## How to run?

Simply clone and run `python bandit.py`. Assumes `matplotlib` is available. Also takes a decent amount of time to complete.

----
## Result

The problem was asking how a different step-size method could affect the k-bandit problem assuming a non-stationary target. The resulting graph looks like:

![Graph](https://github.com/sgodwincs/k-bandit-exercise/graph.png)

Where the red curve uses a sample average and the green curve uses a constant step-size parameter. The results are averaged over 2000 runs for each.
