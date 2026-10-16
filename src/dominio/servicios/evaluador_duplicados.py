"""Domain Service para detección de clientes duplicados N-05."""

class EvaluadorDuplicadosPropietario:
    @staticmethod
    def es_duplicado(correo_nuevo: str, correos_existentes: list) -> bool:
        return correo_nuevo.strip().lower() in [c.strip().lower() for c in correos_existentes]