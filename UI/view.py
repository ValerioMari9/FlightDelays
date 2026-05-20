import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self.inNumCom=None
        self.ddPart=None
        self.ddArr=None
        self.inNumTrt = None

    def load_interface(self):
        COLORE_PRIMARIO = ft.colors.BLUE_600  # Per il titolo e accenti di focus
        COLORE_SFONDO_BTN = ft.colors.BLUE_50  # Sfondo pulsanti (azzurro leggero e fresco)
        COLORE_TESTO_BTN = ft.colors.BLUE_900  # Testo pulsanti per un contrasto leggibile
        LARGHEZZA_LABEL = 200  # Mantiene l'allineamento perfetto a sinistra

        STILE_PULSANTE_VIVACE = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),  # Angoli moderni leggermente smussati
            bgcolor=COLORE_SFONDO_BTN,
            color=COLORE_TESTO_BTN,
            animation_duration=200,  # Feedback fluido al passaggio del mouse
        )
        # -----------------------------------------------

        # # title
        self._title = ft.Text(
            "Flight delays",
            color=COLORE_PRIMARIO,
            size=32,
            weight=ft.FontWeight.BOLD,
        )
        self._page.controls.append(
            ft.Container(
                content=self._title,
                margin=ft.margin.only(bottom=25, top=15),
                alignment=ft.alignment.center
            )
        )

        # ROW with some controls
        # text field for the name
        self.inNumCom = ft.TextField(
            label="# compagnie minimo",
            on_change=self._controller.readNumCom,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.BLUE_200,  # Bordo colorato coerente
            focused_border_color=COLORE_PRIMARIO,  # Colore vivace quando attivo
            height=50,
            expand=2
        )

        self.ddPart = ft.Dropdown(
            label="Partenza",
            disabled=True,
            on_change=self._controller.readPartenza,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.BLUE_200,
            focused_border_color=COLORE_PRIMARIO,
            height=50,
            expand=2
        )

        self.ddArr = ft.Dropdown(
            label="Arrivo",
            disabled=True,
            on_change=self._controller.readArrivo,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.BLUE_200,
            focused_border_color=COLORE_PRIMARIO,
            height=50,
            expand=2
        )

        self.inNumTrt = ft.TextField(
            label="Numero massimo di tratte",
            disabled=True,
            on_change=self._controller.readNumTrt,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.colors.BLUE_200,
            focused_border_color=COLORE_PRIMARIO,
            height=50,
            color=ft.colors.BLACK,
            expand=2
        )

        # Pulsanti con il nuovo stile vivace
        self._butAnalizza = ft.ElevatedButton(
            text="Analizza aeroporti",
            on_click=self._controller.analizzaAeroporti,
            style=STILE_PULSANTE_VIVACE,
            height=50,
            expand=1
        )

        self._butConnessi = ft.ElevatedButton(
            text="Aeroporti connessi",
            on_click=self._controller.aeroportiConnessi,
            style=STILE_PULSANTE_VIVACE,
            height=50,
            expand=1,
            disabled=True
        )

        self._butCerca = ft.ElevatedButton(
            text="Cerca itinerario",
            on_click=self._controller.cercaItinerario,
            style=STILE_PULSANTE_VIVACE,
            height=50,
            expand=1,
            disabled=True
        )

        # Costruzione delle Righe
        r = ft.Row([
            ft.Container(ft.Text("# compagnie minimo", size=14, color=ft.colors.BLUE_GREY_700), width=LARGHEZZA_LABEL),
            self.inNumCom,
            self._butAnalizza
        ], spacing=20)
        self._page.controls.append(ft.Container(content=r, margin=ft.margin.only(bottom=12)))

        r = ft.Row([
            ft.Container(
                ft.Text("Aeroporto di partenza", weight=ft.FontWeight.W_600, size=14, color=ft.colors.BLUE_GREY_900),
                width=LARGHEZZA_LABEL),
            self.ddPart,
            self._butConnessi
        ], spacing=20)
        self._page.controls.append(ft.Container(content=r, margin=ft.margin.only(bottom=12)))

        r = ft.Row([
            ft.Container(
                ft.Text("Aeroporto di arrivo", weight=ft.FontWeight.W_600, size=14, color=ft.colors.BLUE_GREY_900),
                width=LARGHEZZA_LABEL),
            self.ddArr,
            ft.Container(expand=1, height=50)
        ], spacing=20)
        self._page.controls.append(ft.Container(content=r, margin=ft.margin.only(bottom=12)))

        r = ft.Row([
            ft.Container(
                ft.Text("Numero tratte massimo", weight=ft.FontWeight.W_600, size=14, color=ft.colors.BLUE_GREY_900),
                width=LARGHEZZA_LABEL),
            self.inNumTrt,
            self._butCerca
        ], spacing=20)
        self._page.controls.append(ft.Container(content=r, margin=ft.margin.only(bottom=25)))

        # Area Risultati stilizzata (sfondo leggero per staccarla dai controlli)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        container_risultati = ft.Container(
            content=self.txt_result,
            border=ft.border.all(1, ft.colors.BLUE_100),
            border_radius=8,
            bgcolor=ft.colors.GREY_50,
            expand=True
        )
        self._page.controls.append(container_risultati)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
