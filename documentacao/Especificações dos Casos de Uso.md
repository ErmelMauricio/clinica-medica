# Especificações dos Casos de Uso

## Identificação dos Atores

- **Ator 1:** Recepcionista
>Responsável pelo cadastro e atualização de dados dos pacientes, consulta de disponibilidade de horários, realização, confirmação e cancelamento de agendamentos de consultas.

- **Ator 2:** Médico
>Responsável pela realização do atendimento clínico, consulta ao prontuário do paciente, registro de diagnósticos, prescrição de medicamentos e solicitação de exames complementares.

- **Ator 3:** Paciente
>Usuário que busca atendimento na clínica, responsável por solicitar marcação de consultas e solicitar o cancelamento de seus agendamentos.


## Caso de Uso 1: Cadastrar Paciente

>Permite à **Recepcionista** registrar os dados pessoais, de contato e convênio médico de um novo paciente no sistema para habilitá-lo ao agendamento de consultas e atendimentos.

### Ator Principal:
>**Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a opção "Novo Cadastro de Paciente".
2. O sistema apresenta o formulário de cadastro solicitando os dados o paciente.
3. A **Recepcionista** preenche os dados solicitados e clica em "Salvar".
4. O sistema valida a consistência de todos os campos obrigatórios.
5. O sistema armazena os dados do paciente no banco de dados e gera o número de prontuário.

### Fluxos Alternativos:
**CPF já cadastrado no sistema:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CPF informado já pertence a outro paciente cadastrado.*
1. O sistema exibe a mensagem de erro: "CPF já cadastrado no sistema".
2. O sistema oferece a opção de abrir o cadastro existente para atualização de dados ou cancelar a operação.
3. A **Recepcionista** seleciona a opção desejada e o caso de uso é encerrado.

**Campos obrigatórios não preenchidos ou dados inválidos:**
*No passo 3 do fluxo básico, caso algum campo obrigatório esteja vazio ou com formato incorreto.*
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo segue para o passo 4 do fluxo básico.

### Requisitos Especiais:
>O tempo de resposta para validação de unicidade de CPF deve ser inferior a 2 segundos.

### Condições Prévias:
>A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.

### Condições Posteriores:
>O sistema exibe a mensagem: “Paciente cadastrado com sucesso!”.


## Caso de Uso 2: Agendar Consulta

>Permite à **Recepcionista** ou ao **Paciente** marcar uma consulta médica, selecionando a especialidade, o médico, a data e o horário desejado dentre os disponíveis na agenda. 

### Atores Principais:
>**Recepcionista** ou **Paciente** via autoatendimento.

### Fluxo Básico:
1. O ator acessa a funcionalidade "Agendar Consulta".
2. O ator localiza o paciente informando o CPF (caso o ator seja um **Paciente**, então precisará ser feito uma autenticação multi fator via sms).
3. O sistema recupera e exibe os dados do paciente.
4. O ator seleciona a especialidade médica e o médico desejado.
5. O sistema executa obrigatoriamente o caso de uso "Consultar Horários Disponíveis".
6. O ator seleciona a data e o horário pretendido na grade apresentada.
7. O ator seleciona a modalidade de pagamento (Particular ou Convênio).
8. O ator clica em "Confirmar Agendamento".

### Fluxos Alternativos:
**Paciente não cadastrado no sistema (para Recepcionista):**
*No passo 2 do fluxo básico, caso o paciente não seja localizado pelo CPF.*
1. O sistema informa: "Paciente não localizado".
2. O sistema oferece o redirecionamento imediato para o caso de uso "Cadastrar Paciente".
 
**Paciente não cadastrado no sistema (para Paciente):**
*No passo 2 do fluxo básico, caso o paciente não seja localizado pelo CPF.*
1. O sistema informa: "Paciente não localizado".
2. O sistema indica que o **Paciente** contate a **Recepcionista** para realizar o cadastro.

### Requisitos Especiais:
>- O sistema deve garantir controle de concorrência para evitar que dois atores agendem o mesmo horário simultaneamente.
>- O sistema deve registrar a data/hora e o usuário responsável pelo agendamento para fins de auditoria.

### Condições Prévias:
>O ator deve estar autenticado no sistema com credenciais ativas.

### Condições Posteriores:
>- O sistema exibe a mensagem: “Consulta agendada com sucesso”, junto da informação de data, hora e nome do médico.
>- Horário selecionado marcado como indisponível na grade do profissional.

### Ponto de Extensão:
>A verificação de horários é parte essencial e não pode ser desassociada da ação de efetuar um agendamento.


## Caso de Uso 3: Registrar Atendimento Médico

>Permite ao **Médico** registrar as informações da consulta clínica realizada com o paciente, incluindo anamnese, sintomas, exame físico, diagnóstico (CID) e conduta terapêutica no prontuário eletrônico.

### Ator Principal:
>**Médico**.

### Fluxo Básico:
1. O **Médico** visualiza a lista de pacientes com status "Aguardando Atendimento" na sua agenda do dia.
2. O **Médico** seleciona o paciente e clica em "Iniciar Atendimento".
3. O sistema abre o prontuário eletrônico do paciente, exibindo histórico médico anterior e campos para o novo registro.
4. O **Médico** registra os detalhes do atendimento em texto.
5. Caso o **Médico** precise receitar medicamentos, o sistema executa o caso de uso "Emitir Prescrição Médica".
6. Caso o **Médico** necessite de exames complementares, o sistema executa o caso de uso "Solicitar Exames".
7. O **Médico** finaliza o atendimento clicando em "Concluir Consulta".
8. O sistema valida os dados do prontuário, salva a evolução médica com carimbo eletrônico do profissional.

### Fluxo Alternativo:
**Paciente ausente (Não comparecimento):**
*No passo 2 do fluxo básico, caso o paciente chamado não compareça ao consultório.*
1. O **Médico** seleciona a opção "Registrar Não Comparecimento".
2. O sistema solicita justificativa ou confirmação da ausência.
3. O sistema atualiza o status da consulta para "Faltou" e retorna à lista de pacientes.

### Requisito Especial:
>O acesso ao prontuário deve ser restrito exclusivamente aos **Médicos**.

### Condições Prévias:
>- O paciente deve possuir uma consulta agendada. 
>- O **Médico** deve estar devidamente autenticado no sistema.

### Condições Posteriores:
>- Evolução clínica gravada permanentemente no prontuário do paciente.
>- Status da consulta alterado para "Realizada".
>- Habilita a possibilidade de imprimir receitas e encaminhamentos para exames.

### Pontos de Extensão:
- **Caso de Uso Estendido: Emitir Prescrição Médica:**
  *Ocorre apenas se o **Médico** julgar clinicamente necessário prescrever medicamentos ao paciente durante a consulta.*
   
- **Caso de Uso Estendido: Solicitar Exames:**
  *Ocorre apenas se houver necessidade clínica de exames laboratoriais ou de imagem complementares para fechamento de diagnóstico.*