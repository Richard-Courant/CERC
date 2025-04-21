# cotizador.py

from typing import Literal

class Cotizador:
    precios = {
        "tipo_servicio": {
            "Tarea": 200,
            "Examen": 400,
            "Proyecto": 300,
            "Clase": 150,
            "Regularizacion": 200
        },
        "nivel": {
            "Universidad": 50,
            "Bachillerato": 25,
            "Secundaria": -25
        },
        "urgencia": {
            "Alta": 0.25,
            "Media": 0.1,
            "Baja": 0.0
        },
        "area_materia": {
            "Fisico_Matematicas": 0.1,
            "Quimico_Biologicas": 0.1,
            "Sociales": 0,
            "Humanidades": 0
        },
        "dificultad": {
            "Alta": 0.25,
            "Media": 0,
            "Baja": 0
        }
    }

    def cotizar_servicio(
        self,
        tipo_servicio: Literal['Tarea', "Examen", "Proyecto", "Clase", "Regularizacion"],
        nivel: Literal["Universidad", "Bachillerato", "Secundaria"],
        urgencia: Literal["Alta", "Media", "Baja"],
        area_materia: Literal["Fisico_Matematicas", "Quimico_Biologicas", "Sociales", "Humanidades"],
        dificultad: Literal["Alta", "Media", "Baja"],
    ) -> dict:

        try:
            base = self.precios["tipo_servicio"][tipo_servicio]
            extra_nivel = self.precios["nivel"][nivel]
            extra_urgencia = base * self.precios["urgencia"][urgencia]
            extra_dificultad = base * self.precios["dificultad"][dificultad]
            extra_area = base * self.precios["area_materia"][area_materia]

            tarifa_final = base + extra_nivel + extra_urgencia + extra_dificultad + extra_area

            return {
                "base": base,
                "extra_nivel": extra_nivel,
                "extra_urgencia": extra_urgencia,
                "extra_dificultad": extra_dificultad,
                "extra_area": extra_area,
                "total": round(tarifa_final, 2)
            }

        except Exception as e:
            return {"error": str(e)}
