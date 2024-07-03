import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        temp_anno = self._view._txtAnno.value
        try:
            temp_anno = int(temp_anno)
            if temp_anno < 1816 or temp_anno > 2016:
                raise ValueError
        except ValueError:
            self._view.create_alert("Inserire un anno tra 1816 e 2016")
            return

        self._model.build_graph(temp_anno)
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.get_n_componenticonnesse()} componenti connesse."))
        temp_grado_vertici = self._model.get_grado_vertici()
        temp_chiavi = sorted(temp_grado_vertici.keys())

        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
        for v in temp_chiavi:
            self._view._txt_result.controls.append(ft.Text(f"{v} -- {temp_grado_vertici[v]} vicini"))
        self._view.update_page()



