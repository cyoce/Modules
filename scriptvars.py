class ScriptConstructor:
    def __init__(self,nvars):
        self.svars = set(nvars)
    def newvars(self,nvars):
        allvars = set(nvars)
        return allvars.symmetric_difference(self.svars)
