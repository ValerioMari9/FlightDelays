import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._numCom=None
        self._aPartenza=None
        self._aArrivo=None
        self._numTrt=None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def readNumCom(self,e):
        try:
            self._numCom=int(self._view.inNumCom.value)
            return 1
        except (TypeError, ValueError):
            self._numCom=None
            return 0
    def readNumTrt(self,e):
        try:
            self._numTrt = int(self._view.inNumTrt.value)
            return 1
        except (TypeError, ValueError):
            self._numTrt = None
            return 0
    def readPartenza(self,e):
        try:
            self._aPartenza=int(self._view.ddPart.value)
            return 1
        except (TypeError, ValueError):
            self._aPartenza=None
            return 0
    def readArrivo(self,e):
        try:
            self._numTrt = int(self._view.ddArr.value)
            return 1
        except (TypeError, ValueError):
            self._numTrt = None
            return 0
    def analizzaAeroporti(self,e):
        self._view.txt_result.controls.clear()
        if not self.readNumCom(1):
            self._view.txt_result.controls.append(ft.Text("Errore", color=ft.colors.RED ))
            self._view.update_page()
            return
        nN, nA, n=self._model.buildGraph(self._numCom)
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {nA}"))
        self._view.ddPart.disabled=False
        self._view.ddArr.disabled=False
        self._view._butConnessi.disabled=False
        self._view.ddPart.options.clear()
        self._view.ddArr.options.clear()
        l=[ft.dropdown.Option(text=str(i), key=i.ID) for i in n]
        self._view.ddPart.options.extend(l)
        self._view.ddArr.options.extend(l)
        self._view.update_page()
    def aeroportiConnessi(self,e):
        print("ReadPartenza called")
        self._view.txt_result.controls.clear()
        if not self.readPartenza(1):
            self._view.txt_result.controls.append(ft.Text("Errore", color=ft.colors.RED))
            print(self._aPartenza)
            self._view.update_page()
            return
        n=self._model.aeroportiConnessi(self._aPartenza)
        l=[ft.Text(f"{k+1}) {str(i[0])} - numero voli: {i[1]} ") for k,i in enumerate(n)]
        self._view.txt_result.controls.extend(l)
        self._view.update_page()

    def cercaItinerario(self,e):
        pass