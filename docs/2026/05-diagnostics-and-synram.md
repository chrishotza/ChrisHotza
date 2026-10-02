# 2026 — COV / SYN-RAM

<details open>
<summary>ES Español</summary>

## COV

COV fue un campo experimental de nodos en Rust con memoria de posición, coherencia, energía, gradiente, topología y estabilidad.

Los nodos podían estar activos o abstractos y podían colapsar/reactivarse bajo dinámicas definidas.

## SYN-RAM

SYN-RAM trasladó la idea hacia la observación del sistema operativo.

La primera implementación fue de solo lectura. Las fases posteriores introdujeron intervención controlada en user-space, operaciones reversibles sobre el working set, filtros de candidatos y procesos interactivos protegidos.

## Evidencia

Un episodio del 17 de enero de 2026 registró un evento de alta presión alrededor de 7z.exe y una intervención de trim sobre el working set, con mediciones antes/después de hard faults, I/O stall y la variable de presión.

## Papel histórico

Esta rama convirtió estado, memoria y presión en un lazo de control computacional en vivo.

</details>

<details>
<summary>EN English</summary>

## COV

COV was an experimental Rust field of nodes with position, coherence, energy, gradient, topology and stability memory.

Nodes could be active or abstract and could collapse/reactivate under defined dynamics.

## SYN-RAM

SYN-RAM moved the idea into operating-system observation.

The first implementation was read-only. Later phases introduced controlled user-space intervention, reversible working-set operations, candidate filters and protected interactive processes.

## Evidence

A January 17, 2026 episode recorded a high-pressure event around 7z.exe and a working-set trim intervention, with before/after measurements of hard faults, I/O stall and the pressure variable.

## Historical role

This branch turned state, memory and pressure into a live computational control loop.

</details>