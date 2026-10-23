# Especificações dos Casos de Uso

## Identificação do Ator

- **Ator 1:** Recepcionista
>Responsável pelo cadastro e atualização de dados dos pacientes, consulta de disponibilidade de horários, realização, confirmação e cancelamento de agendamentos de consultas, envio de lembretes de consulta aos pacientes via WhatsApp.

---
## Caso de Uso 1: Cadastrar Paciente

>Permite à **Recepcionista** registrar os dados pessoais (CPF, nome, WhatsApp e senha) de um novo paciente no sistema para habilitá-lo ao agendamento de consultas e atendimentos.

### Ator Principal:
>**Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a opção "Novo Cadastro de Paciente".
2. O sistema apresenta o formulário de cadastro solicitando os dados o paciente.
3. A **Recepcionista** preenche os dados solicitados e clica em "Salvar".
4. O sistema valida a consistência de todos os campos obrigatórios e solicita a inserção de uma senha (a **Recepcionista** solicita ao **Paciente** para inserir a senha (somente números)).
5. O sistema armazena os dados do paciente no banco de dados e gera o número de prontuário.

### Fluxos Alternativos:
**CPF já cadastrado no sistema:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CPF informado já pertence a outro paciente cadastrado.*
1. O sistema exibe a mensagem de erro: "CPF já cadastrado no sistema".
2. O sistema oferece a opção de abrir o cadastro existente, através do caso de uso "Editar Dados do Paciente" para atualização de dados ou cancelar a operação.
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

### Ponto de Extensão:
> - **Caso de Uso Estendido: Editar Dados do Paciente:**
	  *Ocorre apenas se a **Recepcionista** escolher a opção "Visualizar perfil existente" quando o sistema reconhecer que o CPF utilizado no cadastro já pertence a outro paciente cadastrado. 

---
## Caso de Uso 2: Agendar Consulta

>Permite à **Recepcionista** ou ao **Paciente** marcar uma consulta médica, selecionando a especialidade, o médico, a data e o horário desejado dentre os disponíveis na agenda. 

### Atores Principais:
>**Recepcionista** ou **Paciente** via autoatendimento.

### Fluxo Básico:
1. O ator acessa a funcionalidade "Agendar Consulta".
2. O ator localiza o paciente informando o CPF (caso o ator seja um **Paciente**, então precisará ser feito uma autenticação multifator via WhatsApp).
3. O sistema recupera e exibe os dados do paciente.
4. O ator seleciona a especialidade médica e o médico desejado (existe a opção de não selecionar um médico, assim os horários mostrados são para todos os médicos daquela especialidade.
5. O sistema mostra os horários disponíveis baseado nos filtros selecionados.
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

---
## Caso de Uso 3: Lembrete de Consulta via WhatsApp

> Permite à **Recepcionista** consultar as consultas agendadas para as próximas 48 horas e enviar ao **Paciente** um lembrete via WhatsApp, a partir de uma mensagem padrão que contém o link para cancelar a consulta.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade “Lembretes de Consulta”.
2. O sistema exibe as consultas com o status “Agendada” (não canceladas) para as próximas 48 horas, da mais próxima para a mais distante, e que ainda não tiveram o lembrete enviado.
3. A **Recepcionista** clica na consulta desejada.
4. O sistema monta a mensagem padrão (abaixo) com os dados da consulta e o link para cancelamento.
5. O sistema abre o aplicativo WhatsApp no dispositivo da **Recepcionista**, na conversa com o número de WhatsApp cadastrado do paciente, com a mensagem já preenchida.
6. O sistema altera o status do lembrete da consulta para “Lembrete enviado”, registrando data, hora e **Recepcionista** responsável, e remove a consulta da lista principal.

#### Mensagem Padrão:
> [NOME DO PACIENTE], você possui uma consulta agendada com [NOME DO MÉDICO] [ESPECIALIDADE DO MÉDICO] em [DATA E HORA DA CONSULTA AGENDADA].  
> Caso você não possa comparecer, por favor, cancele o agendamento pelo link:  
> [LINK PARA CANCELAR A CONSULTA]  
> Se você for comparecer, não precisa fazer nada. Seu médico estará te aguardando.

### Fluxos Alternativos:
**Nenhuma consulta com lembrete pendente:**  
_No passo 2 do fluxo básico, caso não existam consultas agendadas para as próximas 48 horas com lembrete pendente._
1. O sistema exibe a mensagem: “Nenhuma consulta com lembrete pendente para as próximas 48 horas”.
2. O caso de uso é encerrado.

**Lembrete já enviado por outra Recepcionista:**  
_No passo 3 do fluxo básico, caso a consulta já tenha sido marcada como “Lembrete enviado” por outra **Recepcionista** enquanto a lista estava aberta._
1. O sistema informa: “Lembrete já enviado por [NOME DA RECEPCIONISTA] em [DATA E HORA]”.
2. O sistema questiona se a **Recepcionista** quer enviar mesmo assim, se a resposta for sim, segue para o passo 4 do fluxo básico, se for não atualiza a lista e o fluxo retorna ao passo 2 do fluxo básico.

**Paciente sem número de WhatsApp cadastrado:**  
_No passo 4 do fluxo básico, caso o paciente não possua número de WhatsApp cadastrado._
1. O sistema informa: “Paciente sem número de WhatsApp cadastrado”.
2. O sistema não abre o WhatsApp e altera o status do lembrete da consulta para “Lembrete enviado”, registrando data, hora e **Recepcionista** responsável, e remove a consulta da lista principal.
3. O fluxo retorna ao passo 2 do fluxo básico.

### Requisitos Especiais:
> - O sistema deve registrar data/hora e a **Recepcionista** responsável pelo lembrete, para fins de auditoria.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - Deve existir consulta agendada, não cancelada, para as próximas 48 horas com lembrete pendente.
> - O aplicativo WhatsApp deve estar disponível no dispositivo da **Recepcionista**.

### Condições Posteriores:
> - A consulta fica com o status “Lembrete enviado” (data, hora e **Recepcionista**) e deixa de aparecer na lista principal.

### Ponto de Extensão:
> - **Caso de Uso Estendido: Cancelar Consulta:**  
> 	   *Ocorre apenas se o **Paciente** clicar no link da mensagem para cancelar a consulta.*

---

## Caso de Uso 4: Cancelar Consulta

> Permite à **Recepcionista** ou ao **Paciente** cancelar uma consulta agendada, liberando o horário na agenda do médico para novos agendamentos.

### Atores Principais:
> **Recepcionista** ou **Paciente** via autoatendimento.

### Fluxo Básico:
1. O ator acessa a funcionalidade "Cancelar Consulta".
2. O ator localiza o paciente informando o CPF (caso o ator seja um **Paciente**, será necessária autenticação multifator via WhatsApp).
3. O sistema exibe as consultas futuras do paciente que não foram canceladas.
4. O ator seleciona a consulta a ser cancelada.
5. O sistema exibe os dados da consulta (médico, data, hora) e solicita confirmação, informando que o horário voltará a ficar disponível para outro paciente.
6. O ator confirma o cancelamento.
7. O sistema altera o status da consulta para "Cancelada", marca o horário como disponível na grade do médico e registra data, hora e usuário responsável pelo cancelamento.
8. O sistema exibe a mensagem: "Consulta cancelada com sucesso! Acesso o menu 'Agendar Consulta' para fazer novo agendamento".

### Fluxos Alternativos:
**Cancelamento originado no WhatsApp:**  
_No passo 1 do fluxo básico, caso o caso de uso seja acionado pelo caso de uso "Lembrete de Consulta via WhatsApp" após o **Paciente** clicar no link enviado via WhatsApp._
1. Como o paciente já é originado do WhatsApp, nao se faz necessária a autenticação multifator tampouco a seleção de qual consulta deve ser desmarcada, portanto os passos 1 a 4 do fluxo básico são dispensados.
2. O fluxo segue a partir do passo 5 do fluxo básico.

**Paciente não localizado:**  
_No passo 2 do fluxo básico, caso o paciente não seja localizado pelo CPF._
1. O sistema informa: "Paciente não localizado".
2. O caso de uso é encerrado.

**Paciente sem consultas passíveis de cancelamento:**  
_No passo 3 do fluxo básico, caso o paciente não possua consultas futuras ativas._
1. O sistema exibe a mensagem: "Nenhuma consulta disponível para cancelamento".
2. O caso de uso é encerrado.

**Desistência do cancelamento:**  
_No passo 6 do fluxo básico, caso o ator opte por não confirmar._
1. O sistema mantém a consulta sem alteração.
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - Somente consultas futuras agendadas e que ainda não foram canceladas podem ser canceladas.
> - A consulta cancelada não é excluída do sistema; permanece com o status "Cancelada" para fins de histórico.
> - Uma consulta cancelada não pode ser reativada; um novo agendamento deve ser feito pelo caso de uso "Agendar Consulta" ou por telefone (fora do sistema).
> - O sistema deve registrar a data/hora, o usuário responsável pelo cancelamento para fins de auditoria.

### Condições Prévias:
> - O ator deve estar autenticado no sistema com credenciais ativas (quando o acesso ao caso de uso "Cancelar Consulta" for feito via caso de uso "Lembrete de Consulta via WhatsApp" a autenticação multifator não se faz necessária).
> - O paciente deve possuir consulta futura agendada e que ainda não foi cancelada.

### Condições Posteriores:
> - Consulta com status "Cancelada".
> - Horário marcado como disponível na grade do médico.
> - O sistema exibe a mensagem "Consulta cancelada com sucesso!".

---

## Caso de Uso 5: Editar Dados do Paciente

> Permite à **Recepcionista** editar os dados cadastrais de um paciente (CPF, nome, WhatsApp e senha).

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade “Editar Dados do Paciente”.
2. A **Recepcionista** informa o CPF, o nome ou o número de prontuário do paciente.
3. O sistema lista os pacientes que correspondem à busca e a **Recepcionista** seleciona o paciente desejado.
4. O sistema exibe os dados cadastrais atuais do paciente (CPF, nome e WhatsApp), com a opção de alterar a senha (a senha atual nunca é exibida).
5. A **Recepcionista** altera os dados desejados (CPF, nome e/ou WhatsApp). Caso o paciente deseje trocar a senha, o **Paciente** digita a nova senha (somente números) no campo próprio.
6. A **Recepcionista** clica em “Salvar”.
7. O sistema valida os campos e solicita confirmação: “Deseja salvar as alterações?”.
8. A **Recepcionista** confirma.
9. O sistema exibe a mensagem: “Dados do paciente atualizados com sucesso!”.

### Fluxos Alternativos:
**Paciente não localizado:**  
_No passo 2 do fluxo básico, caso nenhum paciente corresponda à busca._
1. O sistema exibe a mensagem: “Paciente não localizado”.
2. O caso de uso permanece no passo 2 do fluxo básico e permite que a **Recepcionista** informe outro critério de busca ou encerre o caso de uso.

**Campos obrigatórios não preenchidos ou dados inválidos:**  
_No passo 6 do fluxo básico, caso algum campo esteja vazio ou com formato incorreto._
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo retorna ao passo 6 do fluxo básico.

**Desistência:**  
_Entre os passos 4 e 8 do fluxo básico caso a **Recepcionista** cancele a operação ou não confirme._
1. O sistema descarta as alterações informadas e mantém os dados do paciente sem alteração.
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - Os dados cadastrais do paciente são: CPF, nome, WhatsApp e senha (todos são obrigatórios).

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O paciente deve estar cadastrado no sistema.

### Condições Posteriores:
> - Edição: os dados alterados ficam gravados, as alterações são registradas (data, hora e **Recepcionista**) e o sistema exibe a mensagem “Dados do paciente atualizados com sucesso!”.

---

## Caso de Uso 6: Cadastrar Médico

> Permite à **Recepcionista** registrar os dados profissionais (nome, CRM, UF do CRM, especialidade e horários de atendimento) de um novo médico no sistema, para que sua agenda fique disponível para agendamento de consultas.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a opção "Novo Cadastro de Médico".
2. O sistema apresenta o formulário de cadastro solicitando os dados do médico.
3. A **Recepcionista** preenche os dados solicitados (nome, CRM, UF do CRM, especialidade, dias da semana e horários de atendimento e duração de cada consulta) e clica em "Salvar".
4. O sistema valida a consistência de todos os campos obrigatórios e verifica se o CRM informado já está cadastrado.
5. O sistema armazena os dados do médico no banco de dados e gera a grade de horários do médico, com todos os horários inicialmente disponíveis.

### Fluxos Alternativos:
**CRM já cadastrado no sistema:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CRM e a UF informados já pertencem a outro médico cadastrado.*
1. O sistema exibe a mensagem de erro: "CRM já cadastrado no sistema".
2. O sistema oferece a opção de corrigir os dados informados ou cancelar a operação.
3. Se a **Recepcionista** escolher corrigir, o fluxo retorna ao passo 3 do fluxo básico. Se escolher cancelar, o caso de uso é encerrado.

**Campos obrigatórios não preenchidos ou dados inválidos:**
*No passo 3 do fluxo básico, caso algum campo obrigatório esteja vazio ou com formato incorreto (por exemplo, horário final de atendimento anterior ao horário inicial).*
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo segue para o passo 4 do fluxo básico.

### Requisitos Especiais:
> - O tempo de resposta para validação de unicidade do CRM deve ser inferior a 2 segundos.
> - Os dados cadastrais do médico são: nome, CRM, UF do CRM, especialidade e horários de atendimento (todos são obrigatórios).
> - O sistema deve registrar a data/hora e a **Recepcionista** responsável pelo cadastro, para fins de auditoria.

### Condições Prévias:
> A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.

### Condições Posteriores:
> - O sistema exibe a mensagem: "Médico cadastrado com sucesso!".
> - O médico passa a ser listado na especialidade correspondente, e seus horários passam a ficar disponíveis para os casos de uso "Agendar Consulta" e "Consultar Agenda Médica".

---
## Caso de Uso 7: Consultar Agenda Médica

> Permite à **Recepcionista** ou ao **Médico** visualizar a agenda de um médico em uma data, com os horários disponíveis e os horários ocupados por consultas agendadas.

### Atores Principais:
> **Recepcionista** ou **Médico**.

### Fluxo Básico:
1. O ator acessa a funcionalidade "Consultar Agenda Médica".
2. O sistema apresenta os filtros de consulta: especialidade, médico e data (por padrão, a data atual). Caso o ator seja um **Médico**, o sistema já preenche o filtro com o próprio médico, sem permitir alteração.
3. O ator seleciona a especialidade, o médico e a data desejados e clica em "Consultar".
4. O sistema exibe a grade de horários do médico na data selecionada, em ordem crescente de horário, indicando cada horário como "Disponível" ou "Agendado".
5. Para os horários "Agendado", o sistema exibe o nome do paciente e a modalidade de pagamento (Particular ou Convênio).
6. O ator consulta a agenda e encerra o caso de uso, ou altera a data para consultar outro dia (o fluxo retorna ao passo 4 do fluxo básico).

### Fluxos Alternativos:
**Nenhum médico cadastrado para a especialidade:**
*No passo 3 do fluxo básico, caso a especialidade selecionada não possua médicos cadastrados.*
1. O sistema exibe a mensagem: "Nenhum médico cadastrado para a especialidade selecionada".
2. O fluxo retorna ao passo 3 do fluxo básico, permitindo que o ator escolha outra especialidade.

**Médico sem atendimento na data selecionada:**
*No passo 4 do fluxo básico, caso o médico não possua horários de atendimento na data selecionada.*
1. O sistema exibe a mensagem: "O médico não atende na data selecionada".
2. O fluxo retorna ao passo 3 do fluxo básico, permitindo que o ator escolha outra data ou outro médico.

### Requisitos Especiais:
> - Este caso de uso é somente de consulta: nenhum dado da agenda é alterado.
> - O **Médico** só pode consultar a própria agenda.
> - O sistema deve exibir a agenda atualizada, refletindo agendamentos e cancelamentos feitos até o momento da consulta.

### Condições Prévias:
> - O ator deve estar autenticado no sistema com credenciais ativas.
> - O médico consultado deve estar cadastrado no sistema, com horários de atendimento definidos.

### Condições Posteriores:
> - O sistema exibe a grade de horários do médico na data selecionada.
> - Nenhum dado do sistema é alterado.

---

## Análise das Relações entre Casos de Uso

### Cadastrar Paciente ```<<extend>>``` Agendar Consulta
> Ao Agendar Consulta, caso o CPF informado não pertença a um paciente cadastrado, então o sistema oferece executar o caso de uso Cadastrar Paciente.

### Registrar Atendimento Médico ```<<include>>``` Consultar Histórico do Prontuário:
> Sempre que o médico inicia uma Registro de atendimento médico o histórico do prontuário daquele paciente já é exibido automaticamente.

### Cancelar Consulta ```<<extend>>``` Lembrete de Consulta via WhatsApp:
> No Lembrete de Consulta via WhatsApp é informado o link para que o usuário cancele a consulta, o link inicia o caso de uso Cancelar Consulta.

### Emitir Prescrição Médica ```<<extend>>``` Registrar Atendimento Médico:
> Durante uma consulta o médico irá obrigatoriamente "Registrar Atendimento Médico", enquanto faz o registro o médico "Emitir Prescrição Médica".

### Editar Dados do Paciente ```<<extend>>``` Cadastrar Paciente:
> Durante o cadastro de um novo Paciente, se o CPF utilizado no cadastro já pertence a outro paciente cadastrado, o sistema oferece a opção de seguir até o caso de uso Editar Dados do Paciente.
