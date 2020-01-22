from collections import defaultdict, Counter
from math import floor, sqrt

def num_from_str(string, base=0):
    try:
        return int(string, base=base)
    except ValueError:
        return float(string)

def stem_and_leaf(data, rlen=1):
    """
    Accept data (list)
    Optionally  rlen (default 1)
    return a stem-and-leaf (dict of stem: list[leaves])
    """
    # FIXME class with __repr__
    zero_pad = len(str(max([abs(s) for s in data])))
    fmt = "%0" + str(zero_pad) + "d"
    llen = zero_pad - rlen

    sort_formatted = sorted([fmt % s for s in data])

    stems = defaultdict(list)
    for i in sort_formatted:
        stems[i[0:llen]] += [int(i[-rlen:])]
    return stems


def print_stem_and_leaf(sl):
    """
    accept a stem-and-leaf data structure.
    Print it.
    """
    for stem, ll in sl.items():
        leaves = " ".join([str(l) for l in ll])
        print(stem + " | " + leaves)


def mean(data):
    """
    Accept data (list).
    Return mean:
    μ of population
    x bar of sample
    """
    return sum(data) / len(data)


def median(data):
    """
    Accept data (list).
    Return median
    """
    ordered = sorted(data)
    length = len(ordered)
    mid_hi = floor(length / 2)
    if length % 2 == 1:
        return ordered[mid_hi]
    mid_lo = mid_hi - 1
    return (ordered[mid_hi] + ordered[mid_lo]) / 2


def modes(data):
    """
    Accept data (list)
    Return list of modes,
    or None
    """
    if len(set(data)) == 1:
        return None
    counts = Counter(sorted(data))
    most = max(counts.values())
    return [k for k in counts if counts[k] == most]


def srange(data):
    """
    Accept data (list)
    Return range of data.
    """
    return max(data) - min(data)


def deviations(data):
    """
    Accept data (list of x).
    Return deviations (list of x - μ)
    """
    mu = mean(data)
    return [val - mu for val in data]

def sum_of_squares_of_deviations(data):
    """
    Accept data (list of x), optionally statistical (bool).
    Return SS sub x "sum of squares":  Σ(x-μ)²
    """
    return sum([x ** 2 for x in deviations(data)])

def variance(data, is_sample=True):
    """
    Accept data (list of x), optionally statistical (bool).
    Return variance: σ² = Σ(x-μ)²/N
    or statistical variance s² = Σ(x-xbar)²/(n-1)
    Σ(x-μ)² often notated SS sub x, "sum of squares"
    """

    return sum_of_squares_of_deviations(data) / (len(data) - int(is_sample))


def standard_deviation(data, is_sample=True):
    """
    Accept data (list of x), optionally statistical (bool).
    Return standard deviation σ
    or statistical standard deviation s
    """
    return sqrt(variance(data, is_sample=is_sample))


def is_empirical_bell(data, statistical=False):
    """
    #FIXME not implemented
    Accept data (list of x), optionally statistical (bool)
    Return True if 
    68% within 1 standard deviation of mean AND
    95% within 2 standard deviations of mean AND
    99.7% within 3 standard deviations of mean.
    Else return False
    """
    pass
