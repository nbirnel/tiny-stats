tiny stats
==========

Tiny statistical tools.

Sometimes, you don't want to break out the heavy tools. 
You just want to add some numbers (`total`),
or get a stem-and-leaf graph (`stem-and-leaf`) on the fly.

These are not well documented, tested, or efficient. 

tools:

* `max`
* `min`
* `range`

* `mean`
* `median`
* `mode`

* `standard-deviation`
* `deviations` deviation for each item
* `variance` variance (standard deviation squared)

* `stem-and-leaf` generate a stem-and-leaf graph
* `dot-graph` generate a dot graph

* `total` Should be called `sum`, but that collides with Unix `sum`.
* `fill` fill blank lines with the previous value

* `factorial`
* `permutations` permutation counts
* `combinations` combination counts

develop
-------

In `src/stats`, do `make` to get a virtualenv.
`. venv/bin/activate` and `pip install -r requirements.txt` to fetch
dev requirements.

`pytest` will skip the slow tests by default.

Tests with `@pytest.mark.slow` are for big values on O(n²) functions.
These are really painfully slow,
but they *must* be run if you alter the functions in questions.
