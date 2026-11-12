import os
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import telas
from banco import cliente

PORTA = 8000
PASTA = os.path.dirname(os.path.abspath(__file__))

ROTAS = {
    "/": telas.tela_inicio,
    "/paciente/novo": telas.tela_cadastrar_paciente,
    "/medico/novo": telas.tela_cadastrar_medico,
    "/consulta/agendar": telas.tela_agendar_consulta,
}


class Parametros:
    def __init__(self, dados):
        self._dados = dados

    def __call__(self, nome):
        return self._dados.get(nome, [""])[0].strip()

    def lista(self, nome):
        return self._dados.get(nome, [])


class Manipulador(BaseHTTPRequestHandler):
    def do_GET(self):
        self.tratar(None)

    def do_POST(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        corpo = self.rfile.read(tamanho).decode("utf-8")
        self.tratar(Parametros(parse_qs(corpo, keep_blank_values=True)))

    def tratar(self, formulario):
        url = urlparse(self.path)
        if url.path == "/estilos.css":
            with open(os.path.join(PASTA, "estilos.css"), "rb") as arquivo:
                return self.responder(200, arquivo.read(), "text/css; charset=utf-8")

        tela = ROTAS.get(url.path)
        if tela is None:
            return self.responder(404, "Página não encontrada".encode("utf-8"), "text/plain; charset=utf-8")

        html = tela(Parametros(parse_qs(url.query, keep_blank_values=True)), formulario)
        self.responder(200, html.encode("utf-8"), "text/html; charset=utf-8")

    def responder(self, codigo, corpo, tipo):
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    cliente.admin.command("ping")
    servidor = HTTPServer(("127.0.0.1", PORTA), Manipulador)
    print(f"Agenda Médica rodando em http://localhost:{PORTA}  (Ctrl+C para encerrar)")
    webbrowser.open(f"http://localhost:{PORTA}")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrado.")

