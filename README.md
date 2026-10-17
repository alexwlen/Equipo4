# VetCare 24 — Sistema de Gestión Clínica Veterinaria

**Materia:** Componentes de Lógica de Negocio  
**Institución:** FIME — UANL  
**Profesor:** Miguel Ángel Gómez Marroquín

## Integrantes

| Integrante | Matrícula |
| Lepe Rodríguez Angel Uriel | 2115842 |
| López Guzmán Eder Abihú] | 2116464 |
| Rodriguez Lara Alexia Guadalupe | 2117441 |

## Alcance del sistema

VetCare 24 es una clínica veterinaria que administra historiales clínicos, esquemas de vacunación con reglas de vencimiento, hospitalización continua y atención prioritaria de emergencias. El sistema no es un simple CRUD, sino un núcleo clínico donde conviven múltiples actores y reglas que deben mantenerse consistentes en tiempo real.

Para la Unidad 3 se seleccionó el patrón **Domain Model**, apoyado en **Repository**, **Unit of Work** y **CQRS básico**, con el fin de proteger invariantes clínicas como el bloqueo farmacológico por alergias (N-01) y la interrupción automática de la agenda ante urgencias (N-03). El diseño cubre los siguientes casos de uso:

- **CU-01:** Registro de mascota con datos esenciales.
- **CU-02:** Procesar ingreso por urgencia médica.
- **CU-03:** Registrar atención médica y receta con alerta de alergia.
- **CU-04:** Aplicar vacuna y programar próximo refuerzo.
- **CU-05:** Registrar ingreso y seguimiento de hospitalización.
