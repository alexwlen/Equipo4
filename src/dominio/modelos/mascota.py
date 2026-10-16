"""Agregado Mascota (Aggregate Root)."""
from datetime import datetime
from typing import List, Optional
from ..excepciones import MedicamentoContraindicadoException

class Alergia:
    """Value Object."""
    def __init__(self, sustancia: str):
        if not sustancia or not sustancia.strip():
            raise ValueError("La sustancia de la alergia no puede estar vacía.")
        self.sustancia = sustancia.strip().upper()

class NotaMedica:
    """Entidad dentro del Aggregate Mascota."""
    def __init__(self, diagnostico: str, tratamiento: str, medicamento: str):
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.medicamento = medicamento.strip().upper()
        self.fecha = datetime.now()

class Mascota:
    """Aggregate Root para la gestión clínica del paciente."""
    def __init__(self, mascota_id: str, nombre: str, especie: str, propietario_id: str, alergias: Optional[List[Alergia]] = None):
        self.mascota_id = mascota_id
        self.nombre = nombre
        self.especie = especie
        self.propietario_id = propietario_id
        self.alergias = alergias or []
        self.historial_clinico: List[NotaMedica] = []

    def prescribir_medicamento(self, diagnostico: str, tratamiento: str, medicamento: str) -> NotaMedica:
        """Protege la Invariante N-01 de seguridad farmacológica."""
        med_upper = medicamento.strip().upper()
        for alergia in self.alergias:
            if alergia.sustancia in med_upper:
                raise MedicamentoContraindicadoException(
                    f"[BLOQUEO N-01] {self.nombre} es alérgico/a a '{alergia.sustancia}'. "
                    f"No se puede prescribir '{medicamento}'."
                )
        
        nota = NotaMedica(diagnostico, tratamiento, medicamento)
        self.historial_clinico.append(nota)
        return nota