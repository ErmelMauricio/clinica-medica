# Geração do HTML

from banco import banco, buscar_por_id
from regras import (agendar_consulta, buscar_paciente_por_cpf, cadastrar_medico,
                    cadastrar_paciente, horarios_livres, medicos_da_especialidade, nome_completo)

ESPECIALIDADES = ["Clínico geral", "Pediatra", "Ginecologista", "Obstetra", "Ortopedista",
                  "Cardiologista", "Oftalmologista", "Neurologista", "Endocrinologista", "Urologista"]
SEXOS = ["Masculino", "Feminino", "Intersexo"]
GENEROS = ["Cisgênero", "Transgênero", "Não binário", "Gênero fluido"]
UFS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
       "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
DIAS_DA_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

MENU = [
    ("Início", "/"),
    ("Cadastrar paciente", "/paciente/novo"),
    ("Cadastrar médico", "/medico/novo"),
    ("Agendar consulta", "/consulta/agendar"),
]

CAMPOS_DO_PACIENTE = [
    "cpf", "nome", "sobrenome1", "sobrenome2", "nome_social",
    "sexo", "genero", "telefone1", "telefone2", "email"
]


def pagina(conteudo, caminho=""):
    links = "".join(f'<a href="{url}"{" class=ativo" if url == caminho else ""}>{rotulo}</a>' for rotulo, url in MENU)
    topo = f'<header><strong>Agenda Médica</strong><nav>{links}</nav></header>'
    return (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>Agenda Médica</title>'
            f'<link rel="stylesheet" href="/estilos.css"></head><body>{topo}<main>{conteudo}</main></body></html>')


def aviso(texto, tipo="ok"):
    return f'<p class="aviso-{tipo}">{texto}</p>' if texto else ""


def opcoes(lista, escolhido="", texto_vazio=""):
    vazio = f'<option value="">{texto_vazio}</option>' if texto_vazio else ""
    return vazio + "".join(f'<option{" selected" if i == escolhido else ""}>{i}</option>' for i in lista)


def linha(nome, rotulo, tipo="text", valor=""):
    return f'<p><label for="{nome}">{rotulo}</label><input id="{nome}" name="{nome}" type="{tipo}" value="{valor}"></p>'


def seletor(nome, rotulo, lista, texto_vazio="Selecione"):
    return f'<p><label for="{nome}">{rotulo}</label><select id="{nome}" name="{nome}">{opcoes(lista, "", texto_vazio)}</select></p>'


# Tela Inicial

def tela_inicio(q, f):
    opcoes_inicio = '''
        <h2>Agenda Médica</h2>
        <p>Selecione uma opção:</p>
        <div class="lista">
            <a href="/paciente/novo">Cadastrar paciente</a>
            <a href="/medico/novo">Cadastrar médico</a>
            <a href="/consulta/agendar">Agendar consulta</a>
        </div>
    '''
    return pagina(opcoes_inicio, "/")


# Cadastrar Paciente

def tela_cadastrar_paciente(q, f):
    rota = "/paciente/novo"
    mensagem = ""
    if f is not None:
        dados = {campo: f(campo) for campo in CAMPOS_DO_PACIENTE}
        cadastrar_paciente(dados)
        mensagem = aviso("Paciente cadastrado com sucesso!")

    formulario = f'''
        <form method="post" action="{rota}" autocomplete="off">
            {linha("cpf", "CPF")}
            {linha("nome", "Nome")}
            {linha("sobrenome1", "Sobrenome 1")}
            {linha("sobrenome2", "Sobrenome 2")}
            {linha("nome_social", "Nome social")}
            {seletor("sexo", "Sexo", SEXOS, "Selecione")}
            {seletor("genero", "Gênero", GENEROS, "Não informado")}
            {linha("telefone1", "Telefone 1 (WhatsApp)")}
            {linha("telefone2", "Telefone 2")}
            {linha("email", "E-mail")}
            <p><button type="submit">Salvar</button></p>
        </form>
    '''
    return pagina(mensagem + "<h2>Cadastrar paciente</h2>" + formulario, rota)


# Cadastrar Médico

def linhas_de_horario():
    html = ""
    for i, dia in enumerate(DIAS_DA_SEMANA, start=1):
        celulas = ""
        for k in ("a", "b"):
            celulas += f'<td><input type="time" name="ini-{i}-{k}"> até <input type="time" name="fim-{i}-{k}"></td>'
        html += f"<tr><td>{dia}</td>{celulas}</tr>"
    return html


def tela_cadastrar_medico(q, f):
    rota = "/medico/novo"
    mensagem = ""
    if f is not None:
        intervalos = []
        for i in range(1, 8):
            for k in ("a", "b"):
                inicio, fim = f(f"ini-{i}-{k}"), f(f"fim-{i}-{k}")
                if inicio and fim:
                    intervalos.append({"dia_semana": i, "inicio": inicio, "fim": fim})
        dados = {
            "nome": f("nome"),
            "crm": f("crm"),
            "uf": f("uf"),
            "especialidades": f.lista("esp"),
            "duracao_min": int(f("duracao") or 30),
            "intervalos": intervalos,
        }
        cadastrar_medico(dados)
        mensagem = aviso("Médico cadastrado com sucesso!")

    especialidades = "".join(
        f'<label class="marcar"><input type="checkbox" name="esp" value="{e}"> {e}</label>'
        for e in ESPECIALIDADES
    )
    formulario = f'''
        <form method="post" action="{rota}" autocomplete="off">
            {linha("nome", "Nome")}
            {linha("crm", "CRM")}
            {seletor("uf", "UF do CRM", UFS, "Selecione")}
            <fieldset><legend>Especialidades</legend>{especialidades}</fieldset>
            {linha("duracao", "Duração da consulta (min)", "number", "30")}
            <h3>Dias e horários de atendimento</h3>
            <table><tr><th>Dia</th><th>Intervalo 1</th><th>Intervalo 2</th></tr>{linhas_de_horario()}</table>
            <p><button type="submit">Salvar</button></p>
        </form>
    '''
    return pagina(mensagem + "<h2>Cadastrar médico</h2>" + formulario, rota)


# Agendar Consulta

def tela_agendar_consulta(q, f):
    rota = "/consulta/agendar"
    titulo = "<h2>Agendar consulta</h2>"

    if f is not None:
        paciente = buscar_por_id(banco.pacientes, f("paciente"))
        medico = buscar_por_id(banco.medicos, f("medico"))
        agendar_consulta(paciente, medico, f("especialidade"), f("data"), f("hora"))
        msg = aviso(f"Consulta agendada com sucesso: {f('data')} às {f('hora')}, com {medico['nome']}.")
        return pagina(msg + titulo + form_busca_cpf(""), rota)

    paciente = buscar_por_id(banco.pacientes, q("paciente"))
    if paciente is None:
        cpf = q("cpf")
        resultado = ""
        if cpf:
            achado = buscar_paciente_por_cpf(cpf)
            if achado:
                resultado = (f'<div class="lista"><a href="{rota}?paciente={achado["_id"]}">'
                             f'{nome_completo(achado)} — CPF {achado["cpf"]}</a></div>')
            else:
                resultado = aviso("Paciente não localizado", "erro")
        return pagina(titulo + form_busca_cpf(cpf) + resultado, rota)

    especialidade, data = q("especialidade"), q("data")
    disponiveis = [e for e in ESPECIALIDADES if medicos_da_especialidade(e)]
    passo2 = f'''
        <h3>Paciente: {nome_completo(paciente)} (CPF: {paciente["cpf"]})</h3>
        <form method="get" action="{rota}">
            <input type="hidden" name="paciente" value="{paciente['_id']}">
            <p><label for="especialidade">Especialidade</label>
            <select id="especialidade" name="especialidade">{opcoes(disponiveis, especialidade, "Selecione")}</select></p>
            <p><label for="data">Data</label><input id="data" name="data" type="date" value="{data}"></p>
            <p><button type="submit">Ver horários</button></p>
        </form>
    '''
    if not especialidade or not data:
        return pagina(titulo + passo2, rota)

    blocos = f"<h3>Horários livres em {data}</h3>"
    for medico in medicos_da_especialidade(especialidade):
        livres = horarios_livres(medico, data)
        blocos += f"<h4>{medico['nome']}</h4>"
        if not livres:
            blocos += "<p>Sem horários livres neste dia.</p>"
        for hora in livres:
            blocos += (f'<form method="post" action="{rota}" class="horario">'
                       f'<input type="hidden" name="paciente" value="{paciente["_id"]}">'
                       f'<input type="hidden" name="medico" value="{medico["_id"]}">'
                       f'<input type="hidden" name="especialidade" value="{especialidade}">'
                       f'<input type="hidden" name="data" value="{data}">'
                       f'<input type="hidden" name="hora" value="{hora}">'
                       f'<button type="submit">{hora}</button></form>')
    return pagina(titulo + passo2 + blocos, rota)


def form_busca_cpf(cpf):
    return (f'<form method="get" action="/consulta/agendar" autocomplete="off">'
            f'<p><label for="cpf">CPF do paciente</label>'
            f'<input id="cpf" name="cpf" value="{cpf}"> <button type="submit">Buscar</button></p></form>')

