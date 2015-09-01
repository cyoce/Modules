class Lit:
    def __init__(self,lit=dict({}),**props):
        self.__dict__.update(props)
        self.__dict__.update(lit)
