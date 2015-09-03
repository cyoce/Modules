class Colors:
    def __init__(self):
        self.colors = {
            'HEADER'    : '\033[95m',
            'OKBLUE'    : '\033[94m',
            'OKGREEN'   : '\033[92m',
            'WARNING'   : '\033[93m',
            'FAIL'      : '\033[91m',
            'ENDC'      : '\033[0m' ,
            'BOLD'      : '\033[1m' ,
            'UNDERLINE' : '\033[4m'
            }
    def cprint(self, text, *colors):
        color = ''
        for clr in colors:
            if clr != '' : color += self.colors[clr]
        print(color + text + (self.colors['ENDC'] * len(colors)))
    def showcolors(self):
        for name in self.colors:
            self.cprint(name,name)
Color = Colors()
