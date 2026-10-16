"""Service Layer (Application Service CU-02)."""
from ...dominio.servicios.calculador_tarifa import CalculadorTarifaEmergencia
from ...infraestructura.repositorios.mascota_repository import IMascotaRepository

class AtencionUrgenciaAppService:
    def __init__(self, mascota_repo: IMascotaRepository):
        self.mascota_repo = mascota_repo

    def procesar_ingreso_urgencia(self, mascota_id: str, motivo: str, es_nocturno: bool) -> dict:
        mascota = self.mascota_repo.obtener_por_id(mascota_id)
        if not mascota:
            raise ValueError(f"Mascota con ID {mascota_id} no encontrada.")
        
        costo_total = CalculadorTarifaEmergencia.calcular_total(tarifa_base=500.0, es_nocturno=es_nocturno)
        
        return {
            "status": "URGENCIA_REGISTRADA",
            "mascota": mascota.nombre,
            "motivo": motivo,
            "costo_atencion": costo_total
        }