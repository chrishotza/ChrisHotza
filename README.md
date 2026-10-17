<!-- REAL README GAME / GitHub native HTML-only state machine. No JS, redirects or external execution. -->
## 🎮 Una partida adentro de este README

**Creo cosas con IA.** La máquina está jugando al tres en raya. ¿Le ganás?

Esto **es un juego con reglas, turnos y adversario automático**: elegís una posición, la computadora hace su movimiento y ves el tablero actualizado, **sin salir de esta página**. No es un chat con IA en vivo: todas las respuestas legales están calculadas previamente.

<details>
<summary><b>▶ JUGAR AHORA — X CONTRA LA MÁQUINA</b></summary>

**X = vos** · **O = máquina** · **1–9 = casillas disponibles**. Tres en línea gana. Tocá una jugada debajo del tablero. Las demás opciones del mismo turno se cerrarán automáticamente.

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ 5 │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TU TURNO · ELEGÍ LA PRIMERA CASILLA**

<details name="tx1">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t01x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t01x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t01x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t016x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t016x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0165x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t016x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t01x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t01x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t0x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t02x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t02x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t023x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t023x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ O │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t023x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0237x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t02x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t025x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t025x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ O │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t025x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0257x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t02x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t027x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t027x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0273x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t027x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0275x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t02x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t028x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t028x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t028x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0287x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="t0x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t03x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t03x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t03x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t03x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t03x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t0x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t05x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t05x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t05x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t056x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0561x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t056x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t056x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0567x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t05x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t05x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t0x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t06x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t061x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t061x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0615x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t061x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t06x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t06x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t065x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0651x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t065x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t065x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0657x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t06x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t067x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t067x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t067x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0675x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t06x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t068x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t068x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t068x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t0x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t07x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t07x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t07x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t07x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t076x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t076x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t076x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t0765x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t07x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t0x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t08x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t08x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t08x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t08x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t086x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t086x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t086x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t08x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="tx1">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t10x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t10x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t10x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t106x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t106x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1065x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t106x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t10x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t10x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t1x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t12x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t12x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t12x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t12x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t12x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t128x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1283x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t128x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t128x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t1x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t13x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t13x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t13x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t13x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t13x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t138x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t138x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1386x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t138x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t1x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t15x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t15x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t15x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t15x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t15x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t158x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t158x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1586x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t158x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t1x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t16x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t16x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t16x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t16x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t16x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t168x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1683x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t168x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1685x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t168x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t1x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t17x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t17x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t17x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t17x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t17x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t178x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t178x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t178x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t1x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t18x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t182x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1823x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t182x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t182x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t18x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t183x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t183x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1836x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t183x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t18x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t185x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t185x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1856x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t185x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t18x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t186x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1863x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t186x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t1865x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t186x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t18x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t187x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t187x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t187x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="tx1">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t20x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t20x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t203x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t203x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ O │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t203x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2037x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t20x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t205x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t205x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ O │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t205x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2057x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t20x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t207x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t207x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2073x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t207x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2075x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t20x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t208x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t208x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t208x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2087x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ X │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="t2x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t21x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t21x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t21x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t21x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t21x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t218x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2183x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t218x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t218x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t2x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t23x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t23x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t23x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t23x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t23x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t238x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2381x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t238x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t238x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2387x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="t2x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t25x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t25x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t25x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t25x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t25x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t2x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t26x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t26x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t26x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t26x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t26x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t268x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t268x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t268x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t2x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t27x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t27x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t27x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t27x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t27x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t278x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t278x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2783x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t278x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t2x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t28x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t281x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2813x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t281x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t281x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t28x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t283x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2831x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t283x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t283x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2837x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t28x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t28x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t286x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t286x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t286x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t28x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t287x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t287x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t2873x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t287x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="tx1">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t30x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t30x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t30x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t30x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t30x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t3x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t31x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t31x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t31x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t31x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t31x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t318x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t318x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3186x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t318x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t3x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t32x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t32x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t32x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t32x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t32x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t328x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3281x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t328x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t328x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3287x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="t3x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t35x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t35x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t35x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t35x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t35x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t358x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t358x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t358x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t3x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t36x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t36x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t36x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t36x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t36x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t368x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3681x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t368x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t368x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t3x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t37x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t37x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t37x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t37x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t37x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t378x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t378x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t378x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t3x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t38x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t381x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t381x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3816x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t381x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t38x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t382x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3821x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t382x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t382x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3827x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t38x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t385x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t385x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t385x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t38x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t386x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t3861x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t386x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t386x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t38x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t387x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t387x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t387x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="tx1">
<summary><b>⑤ B2 · jugar X</b></summary>

**Vos:** B2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t41x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t413x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t413x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t413x4">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4138x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t41x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t415x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t415x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t415x4">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t41x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t416x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t416x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4165x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t416x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t41x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t41x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t418x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4183x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t418x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t418x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t4x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t42x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t42x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t423x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ O │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t423x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t423x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4237x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t42x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t42x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ O │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t42x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ O │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t4x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t43x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t431x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t431x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t431x4">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4318x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t43x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t43x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t43x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t43x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t4x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t45x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t451x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t451x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t451x4">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t45x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ X │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t45x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t45x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t45x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t4x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t46x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t461x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t461x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4615x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t461x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t46x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t46x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t46x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t46x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t4x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t47x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t47x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t47x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t47x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t47x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t4x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t48x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t481x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t4813x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ X │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t481x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ X │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t481x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t48x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t48x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t48x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t48x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ 4 │ X │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="tx1">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t50x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t50x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t50x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t506x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5061x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t506x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t506x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5067x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t50x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t50x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t5x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t51x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t51x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t51x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t51x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t51x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t518x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t518x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5186x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t518x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t5x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t52x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t52x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t52x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t52x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t52x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t5x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t53x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t53x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t53x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t53x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t53x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t538x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t538x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t538x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t5x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t56x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t56x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t56x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t56x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t56x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t568x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5681x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t568x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t568x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t5x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t57x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t57x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t57x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t57x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t57x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t578x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t578x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t578x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t5x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t58x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t581x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t581x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5816x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t581x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t58x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t58x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t583x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t583x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t583x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t58x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t586x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t5861x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t586x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t586x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t58x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t587x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t587x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t587x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

</details>

<details name="tx1">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t60x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t601x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t601x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6015x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t601x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t60x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t60x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t605x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6051x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t605x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t605x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6057x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t60x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t607x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t607x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t607x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6075x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t60x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t608x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t608x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t608x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t6x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t61x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t61x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t61x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t61x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t61x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t618x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6183x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t618x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6185x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t618x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t6x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t62x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t62x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t62x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t62x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t62x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t628x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t628x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t628x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t6x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t63x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t63x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t63x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t63x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t63x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t638x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6381x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t638x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t638x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t6x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t65x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t65x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t65x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t65x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t65x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t658x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6581x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t658x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t658x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t6x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t67x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t67x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t67x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t67x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t67x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t6x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t68x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t681x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6813x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t681x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6815x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t681x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t68x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t682x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t682x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t682x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t68x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t683x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6831x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t683x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t683x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t68x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t685x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t6851x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t685x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t685x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t68x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="tx1">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t7x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t70x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t70x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t70x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ 9 │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t70x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t706x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t706x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t706x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t7065x5">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t70x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t7x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t71x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t71x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t71x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t71x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t71x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t718x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t718x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t718x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t7x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t72x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t72x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t72x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t72x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t72x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t728x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t728x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t7283x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t728x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t7x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t73x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t73x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t73x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t73x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t73x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t738x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t738x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t738x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t7x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t75x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t75x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t75x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t75x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t75x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t758x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t758x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t758x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t7x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ 9 │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t76x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t76x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t76x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t76x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ O │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t76x3">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t7x2">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t78x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t781x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t781x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t781x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t78x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t782x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t782x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t7823x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t782x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t78x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t783x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t783x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t783x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t78x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t785x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t785x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t785x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t78x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="tx1">
<summary><b>⑨ C3 · jugar X</b></summary>

**Vos:** C3 　 **CPU:** B2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ 1 │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 2/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8x2">
<summary><b>① A1 · jugar X</b></summary>

**Vos:** A1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t80x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t80x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t80x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t80x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t806x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t806x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t806x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ O │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t80x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ X │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t8x2">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t81x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t812x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8123x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t812x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t812x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t81x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t813x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t813x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8136x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t813x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t81x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t815x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t815x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8156x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t815x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t81x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t816x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8163x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t816x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8165x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t816x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t81x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t817x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t817x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t817x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t8x2">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t82x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t821x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8213x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t821x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t821x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t82x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t823x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8231x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t823x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t823x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8237x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t82x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t82x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t826x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t826x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t826x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t82x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t827x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t827x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8273x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t827x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t8x2">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t83x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t831x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t831x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8316x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t831x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t83x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t832x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8321x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🤝 EMPATE

Tablero lleno, sin ganador.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t832x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t832x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8327x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t83x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t835x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t835x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t835x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t83x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t836x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8361x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t836x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t836x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t83x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t837x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t837x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t837x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t8x2">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t85x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t851x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t851x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8516x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t851x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t85x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t85x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t853x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t853x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t853x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t85x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t856x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8561x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t856x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t856x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t85x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t857x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t857x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t857x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>

<details name="t8x2">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t86x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t861x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8613x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t861x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8615x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t861x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t86x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t862x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ O │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t862x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t862x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t86x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t863x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8631x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ O │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t863x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t863x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t86x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t865x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8651x5">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ O │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t865x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ X │ 8 │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t865x4">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t86x3">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t8x2">
<summary><b>⑧ C2 · jugar X</b></summary>

**Vos:** C2 　 **CPU:** A1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 3/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t87x3">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t871x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t871x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t871x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t87x3">
<summary><b>③ A3 · jugar X</b></summary>

**Vos:** A3 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t872x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** B1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ X │
  ├───┼───┼───┤
B │ O │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t872x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 5/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t8723x5">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ X │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t872x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ X │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t87x3">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t873x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t873x4">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t873x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ X │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t87x3">
<summary><b>⑥ B3 · jugar X</b></summary>

**Vos:** B3 　 **CPU:** A3

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

**TURNO 4/5 · ELEGÍ TU PRÓXIMA CASILLA VACÍA**

<details name="t875x4">
<summary><b>② A2 · jugar X</b></summary>

**Vos:** A2 　 **CPU:** C1

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ X │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ O │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t875x4">
<summary><b>④ B1 · jugar X</b></summary>

**Vos:** B1 　 **CPU:** A2

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ O │ O │
  ├───┼───┼───┤
B │ X │ O │ X │
  ├───┼───┼───┤
C │ 7 │ X │ X │
  └───┴───┴───┘
</pre>

### 💀 PERDISTE

La máquina hizo tres en línea. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

<details name="t875x4">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ O │
  ├───┼───┼───┤
B │ 4 │ O │ X │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

<details name="t87x3">
<summary><b>⑦ C1 · jugar X</b></summary>

**Vos:** C1 · la máquina no pudo responder

<pre>
    1   2   3
  ┌───┬───┬───┐
A │ O │ 2 │ 3 │
  ├───┼───┼───┤
B │ 4 │ O │ 6 │
  ├───┼───┼───┤
C │ X │ X │ X │
  └───┴───┴───┘
</pre>

### 🏆 GANASTE

Tres en línea. La máquina perdió. Partida terminada.

**Otra partida:** actualizá esta misma página o cerrá y volvé a abrir el cartucho.

</details>

</details>

</details>


</details>

<sub>Hecho con HTML nativo de GitHub, sin JavaScript, enlaces ni recarga durante la partida. El adversario es una estrategia determinista precalculada; no utiliza un modelo online.</sub>

---

<!--
Perfil experimental, español principal. Imágenes locales, GitHub-native.
Sin rastreadores, stats externas, JS, chatbot ni resultados inventados.
README anterior: README.archive-2026-10-16.md.
-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/investigacion-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/investigacion-light.svg">
  <img src="./assets/investigacion-dark.svg" width="100%" alt="Diagrama abstracto de investigación con nodos y conexiones celestes sobre fondo oscuro; una referencia sutil a Argentina, sin nombre ni retratos.">
</picture>

<div align="center">

**Investigación independiente** · **IA aplicada** · **Argentina 🇦🇷**

</div>

### Investigar, construir, comprobar.

Trabajo con IA para explorar problemas, desarrollar herramientas y poner a prueba ideas. Me interesan los sistemas inteligentes, la computación científica y las aplicaciones que puedan tener utilidad fuera de una pantalla.

No todo lo que aparece acá está terminado, ni todo experimento sale bien. La idea es aprender algo en el proceso y, cuando se pueda, **generar valor para la sociedad**.

[**Proyectos ↓**](#proyectos) &nbsp;·&nbsp; [**Cómo trabajo ↓**](#metodo) &nbsp;·&nbsp; [**Archivo de investigación ↗**](docs/README.md)

---

<a id="proyectos"></a>

### En qué ando

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/chrishotza/Skill-Conscious"><img width="100%" src="./assets/proyecto-skill.svg" alt="Skill-Conscious: investigación experimental de memoria, autorreferencia y estado en sistemas de IA"></a>
<br>
<sub>Modelos de memoria, estado persistente y autoobservación. Investigación experimental, no una demostración de conciencia.</sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/chrishotza/Repo-Orbit"><img width="100%" src="./assets/proyecto-orbit.svg" alt="RepoOrbit: catálogo navegable de repositorios para agentes de IA"></a>
<br>
<sub>Un atlas de repositorios que los agentes pueden consultar sin cargar miles de páginas en contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/chrishotza/ai4s-life-science-2026"><img width="100%" src="./assets/proyecto-cells.svg" alt="AI4S Life Science: análisis de imágenes de microscopía y seguimiento de células"></a>
<br>
<sub>Seguimiento celular y análisis de trayectorias a partir de microscopía, con resultados internos documentados.</sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/chrishotza/UnGesto-"><img width="100%" src="./assets/proyecto-ungesto.svg" alt="UnGesto: adhesiones a varias causas sociales desde un mismo flujo"></a>
<br>
<sub>Adhesiones a causas seleccionadas desde una misma plataforma. Las integraciones externas siguen en desarrollo.</sub>
</td>
</tr>
</table>

**También:** [PromptForge](https://github.com/chrishotza/PromptForge) · [ATOF](https://github.com/chrishotza/Adaptiv-Topologica-Optimization-Framework) · [AERIS](https://github.com/chrishotza/Aeris-Dairy-Twin) · [BESS](https://github.com/chrishotza/bess-operational-intelligence) · [más repositorios](https://github.com/chrishotza?tab=repositories)

---

<a id="metodo"></a>

### El método

`Pregunta → Hipótesis → IA + código → Pruebas → Resultado → Iteración`

No tengo una formación formal en todas las áreas que investigo. Uso herramientas y agentes de IA para desarrollar ideas, pero intento que las conclusiones dependan de las pruebas, no de lo convincente que suene una respuesta generada.

<details>
<summary><b>Más sobre las investigaciones y cómo están documentadas</b></summary>

Las líneas incluyen arquitectura experimental de IA, ingeniería de contexto, optimización, biología computacional, energía y herramientas para problemas concretos.

Cada repositorio tiene su propio estado, métodos y limitaciones. El [archivo de investigación](docs/README.md) conserva la trayectoria y el [README anterior](README.archive-2026-10-16.md) sigue disponible completo.

</details>

<details>
<summary><b>English / About this work</b></summary>

Independent researcher and vibe coder from Argentina.

I use AI to explore problems, build prototypes and test what works across experimental AI, scientific computing and practical tools. My goal is to create value for society, with evidence and limitations documented in each repository.

[Explore the projects](#proyectos) · [Research archive](docs/README.md)

</details>

<div align="center">

<sub>Argentina · Investigación abierta · Work in progress</sub>

</div>
