# Operações diretas no Mongo.

from datetime import date
from banco import banco


def para_minutos(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def para_hora(minutos):
    return f"{minutos // 60:02d}:{minutos % 60:02d}"


def nome_completo(p):
    return f"{p['nome_social'] or p['nome']} {p['sobrenome1']} {p['sobrenome2']}".strip()


# Pacientes

def cadastrar_paciente(d):
    banco.pacientes.insert_one(dict(d))


def buscar_paciente_por_cpf(cpf):
    """Pesquisa pelo paciente exclusivamente pelo CPF, sem tratamentos."""
    return banco.pacientes.find_one({"cpf": cpf})


# Médicos

def cadastrar_medico(d):
    banco.medicos.insert_one(dict(d))


def medicos_da_especialidade(especialidade):
    return list(banco.medicos.find({"especialidades": especialidade}))


# Consultas

def horarios_livres(medico, data):
    livres = []
    duracao = int(medico["duracao_min"])
    dia_semana = date.fromisoformat(data).isoweekday()
    ocupados = {c["hora"] for c in banco.consultas.find({"medico_id": medico["_id"], "data": data})}

    for intervalo in medico["intervalos"]:
        if intervalo["dia_semana"] != dia_semana:
            continue
        for ini in range(para_minutos(intervalo["inicio"]), para_minutos(intervalo["fim"]) - duracao + 1, duracao):
            hora = para_hora(ini)
            if hora not in ocupados:
                livres.append(hora)
    return sorted(livres)


def agendar_consulta(paciente, medico, especialidade, data, hora):
    fim = para_minutos(hora) + int(medico["duracao_min"])
    banco.consultas.insert_one({
        "paciente_id": paciente["_id"],
        "medico_id": medico["_id"],
        "especialidade": especialidade,
        "data": data,
        "hora": hora,
        "hora_fim": para_hora(fim),
    })

