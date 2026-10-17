"""Agregado Hospitalización (Aggregate Root)."""
from datetime import datetime
from typing import List
from ..excepciones import ReglaDeNegocioException

class RegistroVital:
    """Value Object inmutable N-04."""
    def __init__(self, temperatura: float, frecuencia_cardiaca: int, observaciones: str):
        self.temperatura = temperatura
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self.observaciones = observaciones
        self.fecha_hora = datetime.now()

class Hospitalizacion:
    """Aggregate Root para seguimiento continuo."""
    def __init__(self, hospitalizacion_id: str, mascota_id: str, motivo: str):
        self.hospitalizacion_id = hospitalizacion_id
        self.mascota_id = mascota_id
        self.motivo = motivo
        self.estado = "ACTIVO"
        self.bitacora_constantes: List[RegistroVital] = []

    def registrar_constantes_turno(self, temp: float, fc: int, obs: str):
        if self.estado != "ACTIVO":
            raise ReglaDeNegocioException("No se pueden agregar registros a una hospitalización terminada.")
        registro = RegistroVital(temp, fc, obs)
        self.bitacora_constantes.append(registro)

    def dar_de_alta(self):
        self.estado = "DADO_DE_ALTA"