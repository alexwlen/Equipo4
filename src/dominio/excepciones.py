"""Excepciones de Dominio del Sistema VetCare 24."""

class ReglaDeNegocioException(Exception):
    """Excepción base para violaciones de invariantes de dominio."""
    pass

class MedicamentoContraindicadoException(ReglaDeNegocioException):
    """Violación N-01: Bloqueo farmacológico por alergia."""
    pass

class CitaFueraDeHorarioException(ReglaDeNegocioException):
    """Violación de la política de agenda."""
    pass