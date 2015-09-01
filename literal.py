class Lit:
    def __init__(self,dct=dict({}),**props):
        self.__dict__.update(props)
        self.__dict__.update(dct)
