# Clínica Médica

> A motivação para o desenvolvimento deste projeto é a entrega do trabalho de grau 2 do segundo semestre de 2026 da cadeira de Laboratório de Engenharia de Software do Unilasalle Canoas.

### Componentes do Grupo:
- Arthur
- Davi
- Graziela
- Mauricio


## Definição do Sistema

### Qual é o objetivo do sistema?

O Sistema de Gestão de Clínica Médica tem como objetivo gerir o processo de agendamento de consultas, o cadastro e manutenção de dados dos pacientes, o registro de atendimentos clínicos e a emissão de prescrições médicas e solicitações de exames.

### Quem utilizará o sistema?

O sistema será utilizado por três perfis de usuários: Recepcionista, Médico e Paciente.

### Qual problema o sistema pretende resolver?

O sistema pretende resolver a lentidão e desorganização decorrente de controles manuais em papel, eliminar conflitos de horários na agenda dos profissionais de saúde, evitar a perda de históricos clínicos dos pacientes e reduzir o tempo de espera no atendimento e na emissão de receitas.

> ### Casos de Uso

Requisitos Funcionais e Não Funcionais 
1. Conceitos
Requisitos funcionais (RF): descrevem as funções e os serviços que o sistema deve oferecer.
Requisitos não funcionais (RNF): descrevem critérios de qualidade, segurança, desempenho e restrições do sistema.
2. Cadastrar Paciente
Ator principal: Recepcionista
Requisitos funcionais (RF)
    • RF01 — O sistema deve permitir que a recepcionista cadastre um paciente com dados pessoais, contato e informações de convênio, quando houver.
    • RF02 — O sistema deve validar os campos obrigatórios e o formato dos dados informados.
    • RF03 — O sistema deve verificar se o CPF já está cadastrado e impedir duplicidade de pacientes pelo mesmo CPF.
    • RF04 — O sistema deve gerar um número de prontuário para o novo paciente.
    • RF05 — O sistema deve confirmar o sucesso do cadastro e permitir a atualização dos dados de um paciente existente.
Requisitos não funcionais (RNF)
    • RNF01 — A validação de unicidade do CPF deve responder em menos de 2 segundos, conforme especificado no trabalho original.
    • RNF02 — Somente usuários autenticados e autorizados podem cadastrar ou alterar dados de pacientes.
    • RNF03 — Os dados pessoais devem ser armazenados com proteção contra acesso, alteração ou divulgação não autorizados.
    • RNF04 — As mensagens de erro devem ser claras e indicar quais campos precisam de correção.
3. Agendar Consulta
Atores principais: Recepcionista ou Paciente autenticado
Requisitos funcionais (RF)
    • RF06 — O sistema deve permitir selecionar paciente, especialidade médica, médico, data e horário disponíveis.
    • RF07 — O sistema deve consultar a agenda e exibir os horários disponíveis para o médico selecionado.
    • RF08 — O sistema deve permitir informar a modalidade de pagamento: particular ou convênio.
    • RF09 — O sistema deve validar os dados e registrar o agendamento, vinculando-o ao paciente e ao médico.
    • RF10 — O sistema deve impedir que duas consultas sejam marcadas para o mesmo médico no mesmo horário.
    • RF11 — O sistema deve exibir a confirmação do agendamento com data, horário e nome do médico.
    • RF12 — O sistema deve registrar a data, a hora e o usuário responsável pelo agendamento.
Requisitos não funcionais (RNF)
    • RNF05 — O controle de concorrência deve impedir conflitos de agenda mesmo quando usuários tentarem reservar o mesmo horário simultaneamente.
    • RNF06 — A consulta de horários e a conclusão do agendamento devem ocorrer em tempo adequado para o uso durante o atendimento da recepção.
    • RNF07 — O acesso ao autoatendimento do paciente deve exigir autenticação; quando aplicável, deve utilizar verificação adicional, conforme descrito no trabalho original.
    • RNF08 — As operações de agendamento devem manter a integridade dos dados mesmo diante de falhas ou interrupções.
4. Cancelar Consulta
Atores principais: Recepcionista ou Paciente autenticado
Requisitos funcionais (RF)
    • RF13 — O sistema deve permitir localizar uma consulta agendada por paciente, data ou identificador da consulta.
    • RF14 — O sistema deve permitir que a recepcionista cancele uma consulta e que o paciente solicite o cancelamento de suas próprias consultas.
    • RF15 — Antes de concluir o cancelamento, o sistema deve solicitar confirmação da ação.
    • RF16 — Após o cancelamento, o sistema deve atualizar o status da consulta para “Cancelada”.
    • RF17 — O sistema deve liberar o horário cancelado na agenda do médico.
    • RF18 — O sistema deve registrar a data, a hora e o usuário responsável pelo cancelamento.
Requisitos não funcionais (RNF)
    • RNF09 — O sistema deve impedir que pacientes cancelem consultas pertencentes a outras pessoas.
    • RNF10 — O cancelamento deve atualizar o status e a disponibilidade do horário de forma consistente.
    • RNF11 — O sistema deve manter registro de auditoria dos cancelamentos para consulta posterior por usuários autorizados.
    • RNF12 — A confirmação e o resultado do cancelamento devem ser apresentados em mensagens claras.
5. Registrar Atendimento Médico
Ator principal: Médico
Requisitos funcionais (RF)
    • RF19 — O sistema deve permitir que o médico acesse a lista de consultas previstas e selecione o paciente a atender.
    • RF20 — O sistema deve permitir registrar anamnese, sintomas, exame físico, diagnóstico (CID), evolução e conduta terapêutica.
    • RF21 — O sistema deve permitir vincular prescrições médicas e solicitações de exames ao atendimento, quando necessário.
    • RF22 — O sistema deve validar e salvar o registro clínico no prontuário do paciente.
    • RF23 — Ao concluir o atendimento, o sistema deve alterar o status da consulta para “Realizada”.
    • RF24 — O sistema deve registrar a identificação do profissional responsável e a data e hora do registro.
Requisitos não funcionais (RNF)
    • RNF13 — O prontuário e o registro clínico devem ser acessíveis apenas a profissionais autorizados, de acordo com suas permissões.
    • RNF14 — O sistema deve preservar a confidencialidade, integridade e rastreabilidade das informações clínicas.
    • RNF15 — O sistema deve evitar a perda de registros confirmados e manter cópias de segurança periódicas.
    • RNF16 — A interface deve organizar os campos clínicos de forma legível, reduzindo erros de preenchimento.
6. Registro de Pagamento ou Consulta a Convênio
Ator principal: Recepcionista
Requisitos funcionais (RF)
    • RF25 — O sistema deve permitir consultar a modalidade de pagamento informada no agendamento: particular ou convênio.
    • RF26 — Quando a modalidade for convênio, o sistema deve permitir consultar os dados do convênio e do plano associados ao paciente.
    • RF27 — O sistema deve permitir registrar um pagamento particular, incluindo valor, data, forma de pagamento e consulta relacionada.
    • RF28 — O sistema deve permitir registrar o status do pagamento, como “Pendente”, “Pago” ou “Estornado”, conforme as operações autorizadas.
    • RF29 — O sistema deve apresentar uma confirmação após o registro do pagamento e permitir consultar o registro posteriormente.
    • RF30 — O sistema deve informar quando os dados do convênio estiverem ausentes ou quando não for possível confirmar a cobertura.
Requisitos não funcionais (RNF)
    • RNF17 — Informações financeiras devem ser acessíveis somente a usuários autorizados.
    • RNF18 — Os valores, datas e status financeiros devem ser armazenados com precisão e consistência.
    • RNF19 — O sistema deve manter histórico auditável das alterações nos registros de pagamento.
    • RNF20 — Se houver integração com operadora de convênio, o sistema deve informar falhas de comunicação sem indicar uma autorização que não foi confirmada.
7. Consultar Histórico do Prontuário
Ator principal: Médico
Requisitos funcionais (RF)
    • RF31 — O sistema deve permitir localizar o prontuário de um paciente identificado.
    • RF32 — O sistema deve exibir os atendimentos anteriores registrados para o paciente, incluindo datas, evoluções, diagnósticos e condutas disponíveis.
    • RF33 — O sistema deve permitir consultar prescrições e solicitações de exames vinculadas ao histórico, quando registradas.
    • RF34 — O sistema deve organizar os registros em ordem cronológica e permitir identificar a data e o profissional responsável por cada atendimento.
    • RF35 — O sistema deve permitir retornar do histórico para o atendimento atual sem perder os dados ainda não salvos, quando houver.
Requisitos não funcionais (RNF)
    • RNF21 — O acesso ao histórico deve ser restrito a profissionais autenticados e autorizados.
    • RNF22 — O histórico deve ser apresentado de forma legível e organizada, com identificação clara de datas e profissionais.
    • RNF23 — A consulta deve preservar os registros originais, sem permitir alterações acidentais durante a visualização.
    • RNF24 — O sistema deve registrar acessos ao prontuário para fins de auditoria, conforme as permissões e políticas da clínica.
8. Confirmar Consulta
Atores principais: Recepcionista ou Paciente autenticado
Requisitos funcionais (RF)
    • RF36 — O sistema deve exibir as consultas agendadas que ainda aguardam confirmação.
    • RF37 — O sistema deve permitir confirmar uma consulta selecionada, após verificar a identidade do usuário e sua permissão.
    • RF38 — O sistema deve atualizar o status da consulta para “Confirmada”.
    • RF39 — O sistema deve apresentar ao usuário a data, o horário, o médico e o resultado da confirmação.
    • RF40 — O sistema deve registrar a data e a hora da confirmação e quem realizou a operação.
    • RF41 — O sistema deve impedir a confirmação de consultas inexistentes, canceladas ou já realizadas.
Requisitos não funcionais (RNF)
    • RNF25 — O sistema deve permitir que somente o paciente relacionado à consulta ou um funcionário autorizado realize a confirmação.
    • RNF26 — A atualização do status deve ser consistente e refletida na agenda sem criar duplicidade de consultas.
    • RNF27 — A confirmação deve produzir retorno claro ao usuário após a conclusão da operação.
    • RNF28 — Os registros de confirmação devem ser protegidos contra alteração não autorizada e estar disponíveis para auditoria.
> - Cadastrar Paciente
> - Agendar Consulta / Cancelar Consulta
> - Registrar Atendimento Médico
> - Registro de Pagamento (ou consulta a convênio)
> - Consultar histórico do prontuário
> - Confirmar consulta
