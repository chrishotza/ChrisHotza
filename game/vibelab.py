#!/usr/bin/env python3
"""GitHub-native community game: evolving a fictional vibe-coder agent.
No dependencies, no secrets, no user-provided Python execution.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "game" / "lab-state.json"
README = ROOT / "README.md"
START = "<!-- VIBE-LAB:START -->"
END = "<!-- VIBE-LAB:END -->"
ISSUES = "https://github.com/chrishotza/ChrisHotza/issues/new"
ACTIONS = {
    "skill": {
        "python": "Python", "research": "Investigación", "security": "Seguridad",
        "vision": "Visión computacional", "data": "SQL y datos", "testing": "Testing",
        "agents": "Orquestación de agentes", "math": "Optimización", "memory": "Memoria de IA",
        "science": "Experimentación", "debugging": "Debugging", "api": "APIs",
    },
    "plugin": {
        "github": "GitHub Actions", "playwright": "Playwright", "ollama": "Ollama",
        "n8n": "n8n", "fastapi": "FastAPI", "docker": "Docker",
        "huggingface": "Hugging Face", "supabase": "Supabase", "render": "Render",
        "kaggle": "Kaggle", "pandas": "Pandas", "gradio": "Gradio",
    },
    "model": {
        "gpt": "GPT", "claude": "Claude", "gemini": "Gemini",
        "llama": "Llama", "qwen": "Qwen", "gemma": "Gemma",
        "deepseek": "DeepSeek", "mistral": "Mistral",
    },
    "build": {
        "research": "Research Stack", "maker": "Builder Stack",
        "science": "Science Stack", "audit": "Audit Stack",
    },
}
XP = {"skill": 12, "plugin": 13, "model": 15, "build": 25}
TYPE_NAMES = {"skill": "SKILL", "plugin": "COMPLEMENTO", "model": "MODELO", "build": "SETUP"}
SETUP_GOALS = {
    "research": "Explorar hipótesis con pruebas, fuentes y trazabilidad.",
    "maker": "Convertir una idea en prototipo con una API y automatización.",
    "science": "Procesar datos e imágenes, medir resultados y documentarlos.",
    "audit": "Revisar seguridad, regresiones y evidencias de ejecución.",
}
TITLE = re.compile(r"^LAB:(skill|plugin|model|build):([a-z0-9_-]{2,24})$", re.ASCII)

def empty_state():
    return {
        "version": 1, "turn": 0, "xp": 0, "level": 1,
        "inventory": {"skill": {}, "plugin": {}, "model": {}, "build": {}},
        "setups": [], "history": [], "actors": {},
    }

def load(path=STATE):
    if not path.exists():
        return empty_state()
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("version") != 1:
        raise ValueError("Unsupported state version")
    for category in ACTIONS:
        raw["inventory"].setdefault(category, {})
    return raw

def pick(items, index, default):
    if not items:
        return default
    return sorted(items, key=lambda key: (-items[key], key))[index % len(items)]

def make_setup(state, build_kind):
    inv = state["inventory"]
    index = state["turn"]
    models = list(inv["model"])
    plugins = list(inv["plugin"])
    skills = list(inv["skill"])
    model = ACTIONS["model"].get(pick(inv["model"], index, ""), "Modelo por elegir")
    plugin = ACTIONS["plugin"].get(pick(inv["plugin"], index // 2, ""), "Complemento por elegir")
    skill = ACTIONS["skill"].get(pick(inv["skill"], index // 3, ""), "Skill por adquirir")
    n = len(state["setups"]) + 1
    return {
        "id": n, "type": build_kind,
        "name": "%s #%d" % (ACTIONS["build"][build_kind], n),
        "model": model, "plugin": plugin, "skill": skill,
        "purpose": SETUP_GOALS[build_kind],
    }

def apply(state, title, actor="visitante"):
    match = TITLE.fullmatch(title.strip())
    if not match:
        raise ValueError("Not a LAB move")
    category, key = match.groups()
    if key not in ACTIONS[category]:
        raise ValueError("Unknown action")
    actor = re.sub(r"[^a-zA-Z0-9-]", "", actor)[:39] or "visitante"
    state["turn"] += 1
    state["xp"] += XP[category]
    state["level"] = 1 + state["xp"] // 50
    current = state["inventory"][category]
    current[key] = current.get(key, 0) + 1
    if category == "build":
        state["setups"].append(make_setup(state, key))
        state["setups"] = state["setups"][-16:]
    entry = {"turn": state["turn"], "actor": actor, "kind": category, "key": key}
    state["history"].append(entry)
    state["history"] = state["history"][-18:]
    state["actors"][actor] = state["actors"].get(actor, 0) + 1
    if len(state["actors"]) > 200:
        state["actors"] = dict(sorted(state["actors"].items(), key=lambda kv: (-kv[1], kv[0]))[:150])
    return entry

def move_link(category, key, label):
    title = "LAB:%s:%s" % (category, key)
    # Prefill only a command title; GitHub requires a logged-in visitor to SUBMIT the issue.
    url = ISSUES + "?title=" + quote(title, safe="") + "&body=" + quote(
        "Jugada del laboratorio. Creá el issue para sumar esta mejora al agente compartido. "
        "GitHub Actions actualiza el perfil y cierra esta jugada cuando termina.", safe=""
    )
    return "[%s](%s)" % (label, url)

def inventory_line(state, category):
    items = state["inventory"][category]
    if not items:
        return "Sin adquirir"
    ordered = sorted(items.items(), key=lambda kv: (-kv[1], kv[0]))
    return " · ".join(
        "%s ×%d" % (ACTIONS[category].get(key, key), count) for key, count in ordered[:9]
    ) + (" · …" if len(ordered) > 9 else "")

def render(state):
    turns = state["turn"]
    lvl = state["level"]
    xp = state["xp"]
    bar = "▰" * (xp % 50 // 5) + "▱" * (10 - xp % 50 // 5)
    sections = []
    sections += [
        START,
        "",
        "<div align=\"center\">",
        "",
        "### VIBE CODER / AGENTE EN EVOLUCIÓN ∞",
        "",
        "**Nivel %d** · **%d XP** · **%d jugadas** · **%d setups creados**" %
        (lvl, xp, turns, state["inventory"]["build"] and sum(state["inventory"]["build"].values()) or 0),
        "",
        bar + "  → Siguiente nivel: %d XP" % ((lvl * 50)),
        "",
        "</div>",
        "",
        "> **Es un juego compartido, no instalaciones reales.** Cada jugador elige una mejora, confirma "
        "una jugada en GitHub Issues y una Action actualiza este agente dentro del README. "
        "Volvé al perfil y refrescá para ver el nuevo estado. No hace falta abrir ningún repositorio para entenderlo.",
        "",
        "| 🧠 SKILLS ADQUIRIDAS | 🧩 COMPLEMENTOS | 🤖 IAs SUMADAS |",
        "| :-- | :-- | :-- |",
        "| %s | %s | %s |" % tuple(inventory_line(state, c) for c in ("skill", "plugin", "model")),
        "",
        "#### 🎮 Elegí la próxima evolución",
        "",
        "Cada enlace prepara la jugada. **Hay que pulsar Submit new issue** para que se procese; "
        "GitHub no permite ejecutar un juego instantáneo con JavaScript en el README.",
        "",
        "<details open>",
        "<summary><b>01 / Aprender una skill (+12 XP)</b></summary>",
        "",
        " · ".join(move_link("skill", k, v) for k, v in ACTIONS["skill"].items()),
        "",
        "</details>",
        "",
        "<details>",
        "<summary><b>02 / Conectar un complemento (+13 XP)</b></summary>",
        "",
        " · ".join(move_link("plugin", k, v) for k, v in ACTIONS["plugin"].items()),
        "",
        "</details>",
        "",
        "<details>",
        "<summary><b>03 / Sumar otra IA al equipo (+15 XP)</b></summary>",
        "",
        " · ".join(move_link("model", k, v) for k, v in ACTIONS["model"].items()),
        "",
        "</details>",
        "",
        "<details>",
        "<summary><b>04 / Compilar un nuevo setup (+25 XP)</b></summary>",
        "",
        " · ".join(move_link("build", k, v) for k, v in ACTIONS["build"].items()),
        "",
        "</details>",
        "",
    ]
    latest = state["setups"][-1] if state["setups"] else None
    sections += ["", "#### 🖥️ Setup actual"]
    if latest:
        sections += [
            "",
            "**%s** — %s" % (latest["name"], latest["purpose"]),
            "",
            "| Skill | IA | Complemento |",
            "| :-- | :-- | :-- |",
            "| %s | %s | %s |" % (latest["skill"], latest["model"], latest["plugin"]),
        ]
    else:
        sections += [
            "",
            "**SIN COMPILAR.** Juntá skills, IAs y complementos. Después elegí *Compilar un setup*.",
            "",
            "| Skill | IA | Complemento |",
            "| :-- | :-- | :-- |",
            "| Por elegir | Por elegir | Por elegir |",
        ]
    if state["history"]:
        sections += ["", "<details>", "<summary><b>📟 Últimas jugadas de la comunidad</b></summary>", "",
                     "| Turno | Jugador | Acción |", "| --: | :-- | :-- |"]
        for e in reversed(state["history"][-10:]):
            name = ACTIONS[e["kind"]][e["key"]]
            sections.append("| %d | @%s | %s: %s |" %
                (e["turn"], e["actor"], TYPE_NAMES[e["kind"]], name))
        sections += ["", "</details>"]
    sections += [
        "", "<sub>∞ Sin nivel máximo. El estado se actualiza a cada jugada confirmada. "
        "La lista de setups recientes se conserva acotada para mantener el README rápido; el XP y el progreso "
        "siguen creciendo. Los nombres de modelos y complementos son opciones simuladas, no conexiones activas.</sub>",
        "", END,
    ]
    return "\n".join(sections)

def update_readme(text, game):
    if START not in text or END not in text:
        raise ValueError("README game markers missing")
    first = text.index(START)
    last = text.index(END, first) + len(END)
    return text[:first] + game + text[last:]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--title", default="")
    p.add_argument("--actor", default="visitante")
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    state = load()
    if args.check:
        test = empty_state()
        for i in range(500):
            kind = list(ACTIONS)[i % 4]
            k = list(ACTIONS[kind])[i % len(ACTIONS[kind])]
            apply(test, "LAB:%s:%s" % (kind, k), "tester")
        assert test["turn"] == 500 and test["level"] > 100
        assert len(test["setups"]) <= 16 and len(test["history"]) <= 18
        assert render(test).count(START) == 1
        print("PASS: 500 valid turns, infinite XP, bounded logs, safe command parser")
        return
    apply(state, args.title, args.actor)
    text = README.read_text(encoding="utf-8")
    new = update_readme(text, render(state))
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    README.write_text(new, encoding="utf-8")
    print("Move processed, turn %d, level %d" % (state["turn"], state["level"]))

if __name__ == "__main__":
    main()
