const banco = db.getSiblingDB("agenda_medica_demo");

function criarId(tipo, numero) {
  return ObjectId(tipo + Number(numero).toString(16).padStart(22, "0"));
}

function C(numero) {
  return criarId("03", numero);
}

function dia(dias) {
  const data = new Date();
  data.setUTCDate(data.getUTCDate() + dias);
  return data.toISOString().slice(0, 10);
}

function garantirColecoes(nomes) {
  const existentes = new Set(banco.getCollectionNames());
  nomes.forEach((nome) => {
    if (!existentes.has(nome)) {
      banco.createCollection(nome);
    }
  });
}

function atualizarOuInserir(colecao, documentos, filtro) {
  const destino = banco.getCollection(colecao);
  documentos.forEach((documento) => {
    destino.replaceOne(filtro(documento), documento, { upsert: true });
  });
}

function buscarPacienteId(cpf) {
  const paciente = banco.pacientes.findOne({ cpf });
  if (!paciente) {
    throw new Error("Paciente não encontrado para o CPF " + cpf);
  }
  return paciente._id;
}

function buscarMedicoId(crm, uf) {
  const medico = banco.medicos.findOne({ crm, uf });
  if (!medico) {
    throw new Error("Médico não encontrado para o CRM " + crm + "/" + uf);
  }
  return medico._id;
}

garantirColecoes([
  "recepcionistas",
  "pacientes",
  "medicos",
  "consultas",
  "ausencias",
]);

atualizarOuInserir(
  "recepcionistas",
  [
    { login: "recepcao1", senha: "123", nome: "Mariana Costa" },
    { login: "recepcao2", senha: "123", nome: "Carlos Lima" },
    { login: "recepcao3", senha: "123", nome: "Juliana Prado" },
  ],
  (documento) => ({ login: documento.login })
);

atualizarOuInserir(
  "pacientes",
  [
    { cpf: "52998224725", nome: "Ana", sobrenome1: "Souza", sobrenome2: "Lima", nome_social: "", sexo: "Feminino", genero: "Cisgênero", telefone1: "51999990001", telefone2: "", email: "ana.souza@exemplo.com" },
    { cpf: "11144477735", nome: "Bruno", sobrenome1: "Ferreira", sobrenome2: "", nome_social: "", sexo: "Masculino", genero: "", telefone1: "51999990002", telefone2: "5133330002", email: "" },
    { cpf: "39053344705", nome: "Daniel", sobrenome1: "Menezes", sobrenome2: "", nome_social: "Dani", sexo: "Masculino", genero: "Não binário", telefone1: "51999990003", telefone2: "", email: "" },
    { cpf: "12345678909", nome: "Carla", sobrenome1: "Pereira", sobrenome2: "Santos", nome_social: "", sexo: "Feminino", genero: "", telefone1: "51999990004", telefone2: "", email: "carla.pereira@exemplo.com" },
    { cpf: "98765432100", nome: "Eduardo", sobrenome1: "Martins", sobrenome2: "", nome_social: "", sexo: "Masculino", genero: "Cisgênero", telefone1: "51999990005", telefone2: "", email: "" },
    { cpf: "24681357928", nome: "Fernanda", sobrenome1: "Oliveira", sobrenome2: "Costa", nome_social: "", sexo: "Feminino", genero: "", telefone1: "51999990006", telefone2: "", email: "" },
    { cpf: "13579246828", nome: "Gustavo", sobrenome1: "Ribeiro", sobrenome2: "", nome_social: "", sexo: "Masculino", genero: "", telefone1: "51999990007", telefone2: "", email: "" },
    { cpf: "11223344517", nome: "Isabela", sobrenome1: "Teixeira", sobrenome2: "", nome_social: "", sexo: "Feminino", genero: "Transgênero", telefone1: "51999990008", telefone2: "", email: "isabela.t@exemplo.com" },
  ],
  (documento) => ({ cpf: documento.cpf })
);

atualizarOuInserir(
  "medicos",
  [
    {
      nome: "Helena Duarte", crm: "12345", uf: "RS", especialidades: ["Clínico geral"], duracao_min: 30,
      intervalos: [
        { dia_semana: 1, inicio: "08:00", fim: "12:00" }, { dia_semana: 1, inicio: "14:00", fim: "18:00" },
        { dia_semana: 3, inicio: "08:00", fim: "12:00" }, { dia_semana: 5, inicio: "08:00", fim: "12:00" },
      ],
    },
    {
      nome: "Rafael Moreira", crm: "67890", uf: "RS", especialidades: ["Cardiologista"], duracao_min: 40,
      intervalos: [
        { dia_semana: 2, inicio: "08:00", fim: "12:00" },
        { dia_semana: 4, inicio: "14:00", fim: "18:00" },
      ],
    },
    {
      nome: "Camila Rocha", crm: "23456", uf: "RS", especialidades: ["Pediatra"], duracao_min: 20,
      intervalos: [1, 2, 3, 4, 5].map((diaSemana) => ({
        dia_semana: diaSemana, inicio: "09:00", fim: "12:00",
      })),
    },
    {
      nome: "Paulo Nunes", crm: "34567", uf: "SC", especialidades: ["Ortopedista", "Clínico geral"], duracao_min: 30,
      intervalos: [
        { dia_semana: 2, inicio: "13:00", fim: "17:00" },
        { dia_semana: 4, inicio: "08:00", fim: "12:00" },
      ],
    },
    {
      nome: "Marina Alves", crm: "45678", uf: "RS", especialidades: ["Ginecologista", "Obstetra"], duracao_min: 30,
      intervalos: [
        { dia_semana: 1, inicio: "08:00", fim: "12:00" },
        { dia_semana: 3, inicio: "14:00", fim: "18:00" },
        { dia_semana: 5, inicio: "14:00", fim: "18:00" },
      ],
    },
  ],
  (documento) => ({ crm: documento.crm, uf: documento.uf })
);

atualizarOuInserir(
  "consultas",
  [
    { _id: C(1), paciente_id: buscarPacienteId("52998224725"), medico_id: buscarMedicoId("12345", "RS"), especialidade: "Clínico geral", data: dia(1), hora: "09:00", hora_fim: "09:30", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Mariana Costa" },
    { _id: C(2), paciente_id: buscarPacienteId("11144477735"), medico_id: buscarMedicoId("67890", "RS"), especialidade: "Cardiologista", data: dia(1), hora: "14:00", hora_fim: "14:40", status: "agendada", solicitante_cancelamento: "", lembrete: { por: "Carlos Lima", em: "06/11/2026 16:20" }, criado_por: "Carlos Lima" },
    { _id: C(3), paciente_id: buscarPacienteId("39053344705"), medico_id: buscarMedicoId("23456", "RS"), especialidade: "Pediatra", data: dia(1), hora: "10:00", hora_fim: "10:20", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Juliana Prado" },
    { _id: C(4), paciente_id: buscarPacienteId("12345678909"), medico_id: buscarMedicoId("12345", "RS"), especialidade: "Clínico geral", data: dia(5), hora: "10:00", hora_fim: "10:30", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Mariana Costa" },
    { _id: C(5), paciente_id: buscarPacienteId("98765432100"), medico_id: buscarMedicoId("34567", "SC"), especialidade: "Ortopedista", data: dia(8), hora: "14:00", hora_fim: "14:30", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Carlos Lima" },
    { _id: C(6), paciente_id: buscarPacienteId("24681357928"), medico_id: buscarMedicoId("45678", "RS"), especialidade: "Ginecologista", data: dia(10), hora: "09:00", hora_fim: "09:30", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Juliana Prado" },
    { _id: C(7), paciente_id: buscarPacienteId("52998224725"), medico_id: buscarMedicoId("23456", "RS"), especialidade: "Pediatra", data: dia(-3), hora: "09:00", hora_fim: "09:20", status: "agendada", solicitante_cancelamento: "", lembrete: null, criado_por: "Mariana Costa" },
    { _id: C(8), paciente_id: buscarPacienteId("13579246828"), medico_id: buscarMedicoId("67890", "RS"), especialidade: "Cardiologista", data: dia(4), hora: "14:00", hora_fim: "14:40", status: "cancelada", solicitante_cancelamento: "Paciente", lembrete: null, criado_por: "Carlos Lima" },
  ],
  (documento) => ({ _id: documento._id })
);

print("Dados de exemplo inseridos/atualizados em agenda_medica_demo.");
