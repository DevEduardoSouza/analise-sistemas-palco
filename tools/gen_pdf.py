"""Gera o PDF de entrega do Documento de Visao, com os diagramas BPMN anexados
ao final, na ordem de P1 a P6, e a sintese da entrevista como segundo anexo.

Usa o Chrome ou o Edge instalados para imprimir o HTML em PDF.

Uso:
    python -m pip install markdown
    python tools/gen_pdf.py

O PDF fica em build/documento-de-visao.pdf.
"""

import base64
import re
import subprocess
import sys
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_bpmn import PROCESSES, FILENAMES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BUILD = ROOT / "build"

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page { size: A4; margin: 20mm 18mm; }
@page paisagem { size: A4 landscape; margin: 12mm; }
body { font-family: "Times New Roman", serif; font-size: 11.5pt; line-height: 1.45; color: #111; }
h1 { font-size: 20pt; text-align: center; margin: 0 0 14pt; }
h2 { font-size: 15pt; margin-top: 22pt; border-bottom: 1px solid #999; padding-bottom: 3pt; }
h3 { font-size: 12.5pt; margin-top: 16pt; }
h4 { font-size: 11.5pt; margin-top: 12pt; }
h2, h3, h4 { page-break-after: avoid; }
p { text-align: justify; margin: 6pt 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.5pt; }
th, td { border: 1px solid #777; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e6e6e6; }
tr { page-break-inside: avoid; }
hr { display: none; }
a { color: inherit; text-decoration: none; }
.quebra { page-break-before: always; }
.anexo { page: paisagem; page-break-before: always; text-align: center; }
.anexo h3 { text-align: left; margin: 0 0 6pt; }
.anexo img { width: 100%; max-height: 165mm; object-fit: contain; }
"""


def sem_links(md):
    """Troca links para arquivos do repositorio pelo texto, que nao funciona no PDF."""
    return re.sub(r"\[([^\]]+)\]\((?!#)[^)]+\)", r"\1", md)


def corpo_documento():
    md = (DOCS / "documento-de-visao.md").read_text(encoding="utf-8")
    # o sumario com ancoras do markdown nao serve no PDF
    md = re.sub(r"## Sumário\n.*?\n---\n", "", md, flags=re.S)
    md = md.replace("**Data:** ___/___/______  **Versão:** 0.2", "**Data:** 15/09/2026  **Versão:** 1.0")
    md = md.replace(
        "A transcrição completa e a síntese dos problemas relatados, numerados de A01 a A16, "
        "estão em [entrevista.md](entrevista.md) e são citadas ao longo deste documento.",
        "A síntese dos problemas relatados, numerados de A01 a A16, está no Anexo B e é citada "
        "ao longo deste documento.",
    )
    # a secao 6 vira a apresentacao do anexo com as imagens
    md = md.replace(
        "Os diagramas do processo estão em [processos/](processos/) na forma de arquivos `.bpmn` "
        "abríveis no Bizagi Modeler e no bpmn.io, acompanhados da descrição textual de cada processo.",
        "Os diagramas dos seis processos são apresentados a seguir, um por página, e foram modelados "
        "em BPMN 2.0.",
    )
    md = md.replace(
        "na [matriz de rastreabilidade](rastreabilidade.md), que liga cada atividade dos diagramas "
        "ao requisito funcional correspondente.",
        "pelo quadro abaixo, que relaciona cada processo aos requisitos funcionais atendidos pelas "
        "suas atividades.",
    )
    # campos do cabecalho, um por linha
    cabecalho, resto = md.split("\n---\n", 1)
    cabecalho = re.sub(r"^(\*\*.*?)\s*$", r"\1  ", cabecalho, flags=re.M)
    md = cabecalho + "\n---\n" + resto
    return sem_links(md)


def anexo_bpmn():
    partes = []
    for proc in PROCESSES:
        png = ROOT / "bpmn" / "png" / FILENAMES[proc.key].replace(".bpmn", ".png")
        dados = base64.b64encode(png.read_bytes()).decode()
        partes.append(
            f'<div class="anexo"><h3>Anexo A.{proc.key[1]} — {proc.key}: {proc.name}</h3>'
            f'<img src="data:image/png;base64,{dados}" alt="Diagrama BPMN {proc.key}"></div>'
        )
    return "\n".join(partes)


def anexo_entrevista():
    md = (DOCS / "entrevista.md").read_text(encoding="utf-8")
    cabecalho = md.split("---")[0]
    cabecalho = re.sub(r"^# .*\n", "", cabecalho)
    cabecalho = cabecalho.replace(
        "A transcrição está completa e com as falas originais. Ao final há a síntese dos achados, "
        "que serve de base para os requisitos e para os diagramas BPMN.",
        "A transcrição completa acompanha o repositório do projeto. Abaixo, a síntese dos achados "
        "que serviu de base para os requisitos e para os diagramas BPMN.",
    )
    cabecalho = re.sub(r"\*\*(Técnica|Entrevistado|Entrevistador):\*\*(.*)\n", r"**\1:**\2  \n", cabecalho)
    sintese = md.split("## Síntese dos achados", 1)[1].replace("### ", "#### ")
    return "## Anexo B — Síntese da entrevista com o dono da Cena Livre\n\n" + cabecalho + sintese


def main():
    BUILD.mkdir(exist_ok=True)
    ext = ["tables", "sane_lists"]
    doc = markdown.markdown(corpo_documento(), extensions=ext)
    doc = doc.replace("<h2>1. Introdução</h2>", '<h2 class="quebra">1. Introdução</h2>', 1)
    doc = doc.replace("<h2>6. Anexos", '<h2 class="quebra">6. Anexos', 1)
    entrevista = markdown.markdown(anexo_entrevista(), extensions=ext)
    entrevista = entrevista.replace("<h2>", '<h2 class="quebra">', 1)

    html = (
        '<!doctype html><html lang="pt-br"><head><meta charset="utf-8">'
        f"<title>Documento de Visão — Sistema Palco</title><style>{CSS}</style></head><body>"
        f"{doc}{anexo_bpmn()}{entrevista}</body></html>"
    )
    arq_html = BUILD / "documento-de-visao.html"
    arq_html.write_text(html, encoding="utf-8")

    navegador = next((n for n in NAVEGADORES if Path(n).exists()), None)
    if not navegador:
        sys.exit("Chrome ou Edge nao encontrado; abra build/documento-de-visao.html e imprima em PDF.")
    arq_pdf = BUILD / "documento-de-visao.pdf"
    subprocess.run(
        [navegador, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={arq_pdf}", arq_html.as_uri()],
        check=True, capture_output=True, timeout=120,
    )
    print(f"{arq_pdf} ({arq_pdf.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
