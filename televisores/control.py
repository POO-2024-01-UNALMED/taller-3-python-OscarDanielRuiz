class Control:

    def __init__(self):
        self._tv = None

    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv

    def turnOn(self):
        self._tv.setEstado(True)
    def turnOff(self):
        self._tv.setEstado(False)

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)
        
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)