"""Agregado AgendaCita (Aggregate Root)."""
from typing import List

class Cita:
    """Entidad Cita."""
    def __init__(self, cita_id: str, mascota_id: str, hora: str, estado: str = "PROGRAMADA"):
        self.cita_id = cita_id
        self.mascota_id = mascota_id
        self.hora = hora
        self.estado = estado

class AgendaCita:
    """Aggregate Root para la agenda diaria de la clínica."""
    def __init__(self, agenda_id: str, fecha: str):
        self.agenda_id = agenda_id
        self.fecha = fecha
        self.citas: List[Cita] = []

    def agregar_cita(self, cita: Cita):
        self.citas.append(cita)

    def interrumpir_y_desplazar_por_urgencia(self, minutos: int = 20):
        """Invariante N-03: Reordenamiento automático por urgencia."""
        for cita in self.citas:
            if cita.estado == "PROGRAMADA":
                cita.estado = f"DESPLAZADA (+{minutos} min)"