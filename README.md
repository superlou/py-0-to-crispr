https://www.youtube.com/watch?v=cLMo6DYdJRE

https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
https://en.wikipedia.org/wiki/FM-index


1. Implement naive suffix array with Python sort
2. Tried to imlement less naive memory-wise. Didn't work. Python sort seems to make a dict of keys anyway, even though it runs faster? Maybe because it's making the dict in C rather than the list in python from `naive_sa(...)`.

naive_sa and naive_sa2 both use same (lots) of memory
Python's List.sort makes an array of keys?: https://stackoverflow.com/questions/23398051/python-memory-efficient-sort-of-a-list-of-tuples-by-two-elements
https://stackoverflow.com/questions/1517347/about-pythons-built-in-sort-method

3. Python 2.7 used to allow a cmp argument that evaluated comparison outside the sort. Python 3.5 doesn't. Try to implement basic bubble sort just to get memory usage reasonable.

https://realpython.com/sorting-algorithms-python/

4. Compare if they're good enough

At some point, try regex search? Python built-in substring search?

5. [Presentation on SA-IS](https://web.stanford.edu/class/archive/cs/cs166/cs166.1196/lectures/04/Small04.pdf)


You want find PAMs within the first few exons that minimize off-target effects.

MIT specificity score