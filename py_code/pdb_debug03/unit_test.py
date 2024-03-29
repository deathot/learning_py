class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        
    def _setattr__(self, key, value):
        self[key] = value

d= Dict(a = 1, b = 2)
print(d['a'], d.a)







