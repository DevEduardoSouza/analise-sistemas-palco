"""Gera uma pagina HTML por diagrama, com o BPMN ja embutido e renderizado
pelo bpmn-js. Serve para conferir o desenho no navegador e para capturar as
imagens PNG que vao anexadas ao Documento de Visao.

Uso:
    python tools/render_html.py
    # depois abra build/P1-....html no navegador

As paginas ficam em build/ e nao entram no controle de versao.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BPMN_DIR = ROOT / "bpmn"
BUILD = ROOT / "build"

TEMPLATE = """<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<title>{titulo}</title>
<script src="https://unpkg.com/bpmn-js@17.9.1/dist/bpmn-navigated-viewer.production.min.js"></script>
<style>
  html, body {{ margin: 0; background: #fff; font-family: system-ui, sans-serif; }}
  #titulo {{ padding: 14px 20px 0; font-size: 15px; font-weight: 600; color: #1d1d1f; }}
  #canvas {{ height: {altura}px; }}
  .bjs-powered-by {{ display: none; }}
</style>
</head>
<body>
<div id="titulo">{titulo}</div>
<div id="canvas"></div>
<script>
const xml = {xml};
const viewer = new BpmnJS({{ container: '#canvas' }});
viewer.importXML(xml).then(() => {{
  viewer.get('canvas').zoom('fit-viewport', 'auto');
  document.body.dataset.pronto = 'sim';
}}).catch(err => {{
  document.body.dataset.pronto = 'erro';
  document.getElementById('titulo').textContent = 'ERRO: ' + err.message;
}});
</script>
</body>
</html>
"""

TITULOS = {
    "P1": "P1 — Criação e publicação de evento",
    "P2": "P2 — Venda de ingresso online",
    "P3": "P3 — Cancelamento e reembolso",
    "P4": "P4 — Check-in e controle de acesso",
    "P5": "P5 — Produção e realização do evento",
    "P6": "P6 — Fechamento financeiro e repasse",
}


def main():
    BUILD.mkdir(exist_ok=True)
    for arq in sorted(BPMN_DIR.glob("*.bpmn")):
        chave = arq.name.split("-")[0]
        xml = arq.read_text(encoding="utf-8")
        altura = 620 if xml.count("<bpmn:lane ") > 3 else 520
        html = TEMPLATE.format(
            titulo=TITULOS.get(chave, arq.stem),
            xml=json.dumps(xml),
            altura=altura,
        )
        destino = BUILD / (arq.stem + ".html")
        destino.write_text(html, encoding="utf-8")
        print(destino)


if __name__ == "__main__":
    main()
