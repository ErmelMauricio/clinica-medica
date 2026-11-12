# Este arquivo só serve para rodar a primeira vez, ele cria as collections e insere os documentos mockados no banco Mongo.

from datetime import date, timedelta


def dia_relativo(dias):
    return (date.today() + timedelta(days=dias)).isoformat()


DADOS = {
    "pacientes": [
        {"id": 1, "cpf": "52998224725", "nome": "Ana", "sobrenome1": "Souza", "sobrenome2": "Lima", "nome_social": "", "sexo": "Feminino", "genero": "Cisgênero", "telefone1": "51999990001", "telefone2": "", "email": "ana.souza@exemplo.com"},
        {"id": 2, "cpf": "11144477735", "nome": "Bruno", "sobrenome1": "Ferreira", "sobrenome2": "", "nome_social": "", "sexo": "Masculino", "genero": "", "telefone1": "51999990002", "telefone2": "5133330002", "email": ""},
        {"id": 3, "cpf": "39053344705", "nome": "Daniel", "sobrenome1": "Menezes", "sobrenome2": "", "nome_social": "Dani", "sexo": "Masculino", "genero": "Não binário", "telefone1": "51999990003", "telefone2": "", "email": ""},
    ],
    "medicos": [
        {"id": 1, "nome": "Helena Duarte", "crm": "12345", "uf": "RS", "especialidades": ["Clínico geral"], "duracao_min": 30,
         "intervalos": [
             {"dia_semana": 1, "inicio": "08:00", "fim": "12:00"}, {"dia_semana": 1, "inicio": "14:00", "fim": "18:00"},
             {"dia_semana": 3, "inicio": "08:00", "fim": "12:00"}, {"dia_semana": 5, "inicio": "08:00", "fim": "12:00"}]},
        {"id": 2, "nome": "Rafael Moreira", "crm": "67890", "uf": "RS", "especialidades": ["Cardiologista"], "duracao_min": 40,
         "intervalos": [{"dia_semana": 2, "inicio": "08:00", "fim": "12:00"}, {"dia_semana": 4, "inicio": "14:00", "fim": "18:00"}]},
        {"id": 3, "nome": "Camila Rocha", "crm": "23456", "uf": "RS", "especialidades": ["Pediatra"], "duracao_min": 20,
         "intervalos": [{"dia_semana": d, "inicio": "09:00", "fim": "12:00"} for d in (1, 2, 3, 4, 5)]},
    ],
    "consultas": [
        {"id": 1, "paciente_id": 1, "medico_id": 1, "especialidade": "Clínico geral", "data": dia_relativo(1), "hora": "09:00", "hora_fim": "09:30"},
        {"id": 2, "paciente_id": 2, "medico_id": 2, "especialidade": "Cardiologista", "data": dia_relativo(1), "hora": "14:00", "hora_fim": "14:40"},
    ],
}

ESPECIALIDADES = ["Clínico geral", "Pediatra", "Ginecologista", "Obstetra", "Ortopedista",
                  "Cardiologista", "Oftalmologista", "Neurologista", "Endocrinologista", "Urologista"]
SEXOS = ["Masculino", "Feminino", "Intersexo"]
GENEROS = ["Cisgênero", "Transgênero", "Não binário", "Gênero fluido"]
UFS = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
       "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
DIAS_DA_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

