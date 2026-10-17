#!/usr/bin/env python3
"""Dependency-free guard for the bilingual illustrated GitHub profile.

Run at repository root: python scripts/check_profile.py
The list is intentionally pinned: adding/removing a public project requires
an explicit review of its description, artwork, and target repository.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXPECTED = {
    "chrishotza/Skill-Conscious": "proyecto-skill.svg",
    "chrishotza/Repo-Orbit": "proyecto-orbit.svg",
    "chrishotza/PromptForge": "proyecto-promptforge.svg",
    "chrishotza/cov-ia": "proyecto-cov-ia.svg",
    "chrishotza/ai4s-life-science-2026": "proyecto-cells.svg",
    "chrishotza/Aeris-Dairy-Twin": "proyecto-aeris.svg",
    "chrishotza/Adaptiv-Topologica-Optimization-Framework": "proyecto-atof.svg",
    "chrishotza/adaptive-topological-optimization": "proyecto-topology.svg",
    "chrishotza/bloc-reloc-v2": "proyecto-bloc.svg",
    "ConsciousPulse/bess-operational-intelligence": "proyecto-bess.svg",
    "chrishotza/Crypto-Security-Forensics-Lab": "proyecto-crypto.svg",
    "chrishotza/Flint-Prop-AMM-Research": "proyecto-flint.svg",
    "chrishotza/T3N-Enterprise-Audit-Agent": "proyecto-t3n.svg",
    "chrishotza/DayZConsoleObservatory": "proyecto-dayz.svg",
    "chrishotza/UnGesto-": "proyecto-ungesto.svg",
}
PRIVATE = (
    "chrishotza/AGI", "chrishotza/RSNA", "chrishotza/Biohub-lab",
    "chrishotza/Research-Lab", "chrishotza/trafficflowbench-2026",
    "chrishotza/Escuela-de-Animaci-n",
)
SVG_NS = "{http://www.w3.org/2000/svg}"
FORBIDDEN_SVG_TAGS = {"script", "foreignObject", "iframe", "image", "animateMotion"}
IMAGE_PATTERN = re.compile(
    r'<a href="https://github\.com/([^"]+)">'
    r'<img src="\./assets/([^"]+\.svg)" alt="([^"]+)" width="([^"]+)">'
)


def main() -> int:
    errors: list[str] = []
    readme = README.read_text(encoding="utf-8")
    images = IMAGE_PATTERN.findall(readme)
    pairs = [(repo, image) for repo, image, _alt, _width in images]
    expected = list(EXPECTED.items())

    if pairs != expected:
        errors.append("The 15 artwork/repository pairs or their order differ from the reviewed public-project index")
    if len(images) != 15 or len(set(pairs)) != 15:
        errors.append("Expected 15 unique illustrated project cards")
    if readme.count('<tr>') != 7 or readme.count('<td width="50%"') != 14:
        errors.append("The seven 2-column HTML table rows have changed")
    for language in ("EN", "ES"):
        if readme.count(f"<strong>{language}</strong>") != 15:
            errors.append(f"Missing or duplicate {language} descriptions")
    if "<script" in readme.lower() or "<iframe" in readme.lower():
        errors.append("Executable/embed HTML is not allowed in GitHub profile Markdown")
    for name in PRIVATE:
        if f"github.com/{name}" in readme:
            errors.append(f"Private repository linked: {name}")

    for repo, image, alt, width in images:
        if not alt.strip() or width not in {"100%", "49%"}:
            errors.append(f"Bad alt text or width for {repo}")
        img_path = ROOT / "assets" / image
        if not img_path.is_file():
            errors.append(f"Missing SVG: {image}")
            continue
        try:
            root = ET.parse(img_path).getroot()
            if root.tag != SVG_NS + "svg":
                errors.append(f"Invalid SVG root: {image}")
            for el in root.iter():
                if el.tag.split("}")[-1] in FORBIDDEN_SVG_TAGS:
                    errors.append(f"Unsupported or unsafe SVG element in {image}")
                if any(key.lower().endswith("href") for key in el.attrib):
                    errors.append(f"External href/reference is not allowed in {image}")
        except ET.ParseError as exc:
            errors.append(f"Invalid XML in {image}: {exc}")

    if errors:
        print("PROFILE CHECK FAILED")
        for issue in errors:
            print(" -", issue)
        return 1
    print("PROFILE CHECK OK: 15 public repositories, 15 valid local SVGs, EN/ES, 7 table rows, no private links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
