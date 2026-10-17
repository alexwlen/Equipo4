"""Pruebas Unitarias Ejecutables."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import unittest
from src.dominio.modelos.mascota import Mascota, Alergia
from src.dominio.modelos.agenda import AgendaCita, Cita
from src.dominio.modelos.hospitalizacion import Hospitalizacion
from src.dominio.excepciones import MedicamentoContraindicadoException
from src.dominio.servicios.calculador_tarifa import CalculadorTarifaEmergencia
from src.dominio.servicios.evaluador_duplicados import EvaluadorDuplicadosPropietario
from src.infraestructura.repositorios.mascota_repository import InMemoryMascotaRepository
from src.aplicacion.servicios.atencion_urgencia_service import AtencionUrgenciaAppService

class TestVetCare24(unittest.TestCase):

    def test_invariante_alergia_N01(self):
        alergia = Alergia("Penicilina")
        mascota = Mascota("M001", "Firulais", "Canino", "P001", [alergia])

        mascota.prescribir_medicamento("Infección", "Reposo", "Amoxicilina")
        self.assertEqual(len(mascota.historial_clinico), 1)

        with self.assertRaises(MedicamentoContraindicadoException):
            mascota.prescribir_medicamento("Otitis", "Gotas", "Penicilina Forte")

    def test_interrupcion_agenda_N03(self):
        agenda = AgendaCita("AG-01", "2026-10-16")
        agenda.agregar_cita(Cita("C1", "M001", "10:00 AM"))
        agenda.agregar_cita(Cita("C2", "M002", "10:30 AM"))

        agenda.interrumpir_y_desplazar_por_urgencia(minutos=20)
        self.assertEqual(agenda.citas[0].estado, "DESPLAZADA (+20 min)")

    def test_hospitalizacion_N04(self):
        hosp = Hospitalizacion("H001", "M001", "Deshidratación")
        hosp.registrar_constantes_turno(38.5, 110, "Turno Mañana")
        self.assertEqual(len(hosp.bitacora_constantes), 1)

if __name__ == "__main__":
    unittest.main()