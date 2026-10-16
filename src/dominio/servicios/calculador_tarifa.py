"""Domain Service para recargos por urgencia."""

class CalculadorTarifaEmergencia:
    @staticmethod
    def calcular_total(tarifa_base: float, es_nocturno: bool) -> float:
        recargo = 1.50 if es_nocturno else 1.20
        return tarifa_base * recargo