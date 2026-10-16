"""Contratos e implementaciones de repositorios (Inversión de Dependencias)."""
from abc import ABC, abstractmethod
from typing import Optional, Dict
from ...dominio.modelos.mascota import Mascota

class IMascotaRepository(ABC):
    @abstractmethod
    def obtener_por_id(self, mascota_id: str) -> Optional[Mascota]: pass
    @abstractmethod
    def guardar(self, mascota: Mascota): pass

class InMemoryMascotaRepository(IMascotaRepository):
    def __init__(self):
        self._db: Dict[str, Mascota] = {}

    def obtener_por_id(self, mascota_id: str) -> Optional[Mascota]:
        return self._db.get(mascota_id)

    def guardar(self, mascota: Mascota):
        self._db[mascota.mascota_id] = mascota