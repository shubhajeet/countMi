class Counter(object):
    def __init__(self) -> None:
        self.n = 0
        self.counter= {}
        super().__init__()
    
    def add(self, x, value=1):
        """
        Count element `x` as if had appeared `value` times.
        By default `value=1` so:
        Effectively counts `x` as occurring once.
        """
        self.n += value
        self.counter[x] = self.counter.get(x,0) + value

    def remove(self, x, value=1):
        """
        element `x` as if have been removed `value` times.
        By default `value=1` so:
        Effectively counts `x` as occurring once.
        """
        self.n -= value
        self.counter[x] = self.counter.get(x,0) - value        

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """
        return self.counter.get(x,0)

    def __getitem__(self, x):
        """
        A convenience method to call `query`.
        """
        return self.query(x)

    def __len__(self):
        """
        The amount of things counted. Takes into account that the `value`
        argument of `add` might be different from 1.
        """
        return self.n