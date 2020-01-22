tiny stats
----------

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

* `total` add a column of numbers. Should be called `sum`,
   but that collides with Unix `sum`
* `fill` fill blank lines with the previous value
