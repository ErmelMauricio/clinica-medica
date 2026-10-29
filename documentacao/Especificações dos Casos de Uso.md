# Especificações dos Casos de Uso

## Identificação do Ator

- **Ator 1:** Recepcionista
>Responsável pelo cadastro e atualização de dados dos pacientes, consulta de disponibilidade de horários, cadastro de novos médicos na agenda, cancelamento de consultas agendadas, envio de lembretes de consulta aos pacientes via WhatsApp e atualizações pontuais na agenda dos médicos.

---
## Caso de Uso 1: Cadastrar Paciente

>Permite à **Recepcionista** registrar os dados pessoais (CPF, nome, sobrenome 1, sobrenome 2, nome social, sexo, genero, telefone 1 (WhatsApp), telefone 2 e email) de um novo paciente no sistema para habilitá-lo ao agendamento de consultas.

### Ator Principal:
>**Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a opção "Novo Cadastro de Paciente".
2. O sistema apresenta o formulário de cadastro solicitando os dados o paciente.
3. A **Recepcionista** preenche os dados solicitados e clica em "Salvar".
4. O sistema valida o CPF.
5. O sistema armazena os dados do paciente no banco de dados.

### Fluxos Alternativos:
**CPF já cadastrado no sistema:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CPF informado já pertence a outro paciente cadastrado.*
1. O sistema exibe a mensagem de erro: "CPF já cadastrado no sistema".
2. O caso de uso se encerra.

**CPF inválido:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CPF informado é inválido.*
1. O sistema exibe a mensagem de erro: "CPF inválido, digite um CPF válido".
2. O caso de uso retorna para o passo 3 do fluxo base.

**Campos obrigatórios não preenchidos ou dados inválidos:**
*No passo 3 do fluxo básico, caso algum campo obrigatório esteja vazio ou com formato incorreto.*
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo segue para o passo 4 do fluxo básico.
### Requisitos Especiais:
>- O tempo de resposta para validação de unicidade de CPF deve ser inferior a 2 segundos.
>- Os campos obrigatórios são CPF, nome, sobrenome 1, sexo e telefone 1.

### Condições Prévias:
>A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.

### Condições Posteriores:
>O sistema exibe a mensagem: “Paciente cadastrado com sucesso!”.

---
## Caso de Uso 2: Agendar Consulta

>Permite à **Recepcionista** marcar uma consulta médica para um paciente, selecionando a especialidade, o médico, a data e o horário desejado dentre os disponíveis na agenda. 

### Ator Principal:
>**Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade "Agendar Consulta".
2. A **Recepcionista** localiza o paciente informando o CPF ou o nome.
3. O sistema recupera e exibe os dados do paciente.
4. A **Recepcionista** seleciona a especialidade médica e o médico desejado (existe a opção de não selecionar um médico, assim os horários mostrados são para todos os médicos daquela especialidade.
5. O sistema mostra os horários disponíveis baseado nos filtros selecionados.
6. A **Recepcionista** seleciona a data e o horário pretendido na agenda apresentada.
7. A **Recepcionista** clica em "Confirmar Agendamento".

### Fluxos Alternativos:
**Paciente não cadastrado no sistema:**
*No passo 2 do fluxo básico, caso o paciente não seja localizado.*
1. O sistema informa: "Paciente não localizado".
2. O caso de uso permanece no passo 2 do fluxo básico aguardando uma nova pesquisa.

### Requisitos Especiais:
>- O sistema deve garantir controle de concorrência para evitar que duas **Recepcionistas** agendem o mesmo horário simultaneamente.
>- O sistema deve registrar a data/hora e a **Recepcionista** responsável pelo agendamento para fins de auditoria.

### Condições Prévias:
>- A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
>- O paciente deve estar cadastrado no sistema.

### Condições Posteriores:
>- O sistema exibe a mensagem: “Consulta agendada com sucesso”, junto da informação de data, hora e nome do médico.
>- Horário selecionado marcado como indisponível na agenda do médico.

---
## Caso de Uso 3: Lembrete de Consulta via WhatsApp

> Permite à **Recepcionista** consultar as consultas agendadas para as próximas 48 horas e enviar ao Paciente um lembrete via WhatsApp, a partir de uma mensagem padrão. O intuito desta interação é ter atrito mínimo, ou seja, o cliente só irá interagir com a mensagem caso queira cancelar, do contrário apenas servirá como lembrete.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade “Lembretes de Consulta”.
2. O sistema exibe as consultas com o status “Agendada” para as próximas 48 horas, da mais próxima para a mais distante, e que ainda não tiveram o lembrete enviado.
3. A **Recepcionista** clica na consulta desejada.
4. O sistema monta a mensagem padrão (abaixo) com os dados da consulta.
5. O sistema abre o aplicativo WhatsApp no dispositivo da **Recepcionista**, na conversa com o número de WhatsApp cadastrado do paciente, com a mensagem já preenchida.
6. O sistema altera o status do lembrete da consulta para “Lembrete enviado”, registrando data, hora e **Recepcionista** responsável, e remove a consulta da lista principal.

#### Mensagem Padrão:
> [NOME DO PACIENTE], você possui uma consulta agendada com [NOME DO MÉDICO] [ESPECIALIDADE DO MÉDICO] em [DATA E HORA DA CONSULTA AGENDADA].  
> Caso você não possa comparecer, por favor, entre em contato com a clínica para cancelar o agendamento.  
> Se você for comparecer, não precisa fazer nada. Seu médico estará te aguardando.

### Fluxos Alternativos:
**Nenhuma consulta com lembrete pendente:**  
*No passo 2 do fluxo básico, caso não existam consultas agendadas para as próximas 48 horas com lembrete pendente.*
1. O sistema exibe a mensagem: “Nenhuma consulta com lembrete pendente para as próximas 48 horas”.
2. O caso de uso é encerrado.

**Lembrete já enviado por outra Recepcionista:**  
*No passo 3 do fluxo básico, caso a consulta já tenha sido marcada como “Lembrete enviado” por outra **Recepcionista** enquanto a lista estava aberta.*
1. O sistema informa: “Lembrete já enviado por [NOME DA RECEPCIONISTA] em [DATA E HORA]”.
2. O sistema questiona se a **Recepcionista** quer enviar mesmo assim, se a resposta for "sim", segue para o passo 4 do fluxo básico, se for "não" atualiza a lista e o caso de uso retorna ao passo 2 do fluxo básico.

**Paciente sem número de WhatsApp cadastrado:**  
*No passo 4 do fluxo básico, caso o telefone 1 do paciente não seja atrelado a um WhatsApp.*
1. Esta função tem como intenção servir como um lembre extra, portanto não faz parte do escopo do sistema qualquer outro tipo de lembrete em casos que o cliente não possa ser lembrado via WhatsApp, sendo assim, o sistema montará a mensagem, abrirá o aplicativo do WhatsApp no dispositivo da **Recepcionista**, mas não encontrará o contato.
2. O fluxo retorna ao passo 2 do fluxo básico.

### Requisitos Especiais:
> - O sistema deve registrar data/hora e a **Recepcionista** responsável pelo lembrete, para fins de auditoria.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - Deve existir consulta agendada, para as próximas 48 horas com lembrete pendente.
> - O aplicativo WhatsApp deve estar disponível no dispositivo da **Recepcionista**.

### Condições Posteriores:
> - A consulta fica com o status “Lembrete enviado” (registrando data, hora e **Recepcionista**) e deixa de aparecer na lista principal.

---

## Caso de Uso 4: Cancelar Consulta

> Permite à **Recepcionista** cancelar uma consulta agendada, liberando o horário na agenda do médico para novos agendamentos.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade "Cancelar Consulta".
2. A **Recepcionista** localiza o paciente informando o CPF ou nome do paciente.
3. O sistema exibe as consultas futuras do paciente que não foram canceladas.
4. A **Recepcionista** seleciona a consulta a ser cancelada.
5. O sistema exibe os dados da consulta (médico, data, hora) e solicita confirmação.
6. A **Recepcionista** confirma o cancelamento.
7. O sistema altera o status da consulta para "Cancelada", disponibiliza aquele horário na agenda daquele médico e registra data, hora e **Recepcionista** responsável pelo cancelamento.

### Fluxos Alternativos:
**Paciente não localizado:**  
_No passo 2 do fluxo básico, caso o paciente não seja localizado._
1. O sistema informa: "Paciente não localizado".
2. O caso de uso retorna para o passo 2 do fluxo base.

**Paciente sem consultas passíveis de cancelamento:**  
_No passo 3 do fluxo básico, caso o paciente não possua consultas futuras ativas._
1. O sistema exibe a mensagem: "Nenhuma consulta disponível para cancelamento".
2. O caso de uso é encerrado.

**Desistência do cancelamento:**  
_No passo 6 do fluxo básico, caso a **Recepcionista** opte por não confirmar._
1. O sistema mantém a consulta sem alteração.
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - Somente consultas futuras podem ser canceladas.
> - A consulta cancelada não é excluída do sistema; permanece com o status "Cancelada" para fins de histórico.
> - Uma consulta cancelada não pode ser reativada; um novo agendamento deve ser feito pelo caso de uso "Agendar Consulta".
> - O sistema deve registrar a data/hora e a **Recepcionista** responsável pelo cancelamento para fins de auditoria.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O paciente deve possuir consulta futura agendada.

### Condições Posteriores:
> - Consulta com status "Cancelada".
> - Horário marcado como disponível na agenda do médico.
> - O sistema exibe a mensagem "Consulta cancelada com sucesso!".

---

## Caso de Uso 5: Editar Dados do Paciente

> Permite à **Recepcionista** editar os dados cadastrais de um paciente (CPF, nome, sobrenome 1, sobrenome 2, nome social, sexo, genero, telefone 1 (WhatsApp), telefone 2 e email).

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade “Editar Dados do Paciente”.
2. A **Recepcionista** informa o CPF ou o nome do paciente.
3. O sistema lista os pacientes que correspondem à busca e a **Recepcionista** seleciona o paciente desejado.
4. O sistema exibe os dados cadastrais atuais do paciente.
5. A **Recepcionista** altera os dados desejados.
6. A **Recepcionista** clica em “Salvar”.
7. O sistema valida os campos e solicita confirmação: “Deseja salvar as alterações?”.
8. A **Recepcionista** confirma.

### Fluxos Alternativos:
**Paciente não localizado:**  
*No passo 2 do fluxo básico, caso nenhum paciente corresponda à busca.*
1. O sistema exibe a mensagem: “Paciente não localizado”.
2. O caso de uso permanece no passo 2 do fluxo básico e permite que a **Recepcionista** informe outro critério de busca ou encerre o caso de uso.

**Campos obrigatórios não preenchidos ou dados inválidos:**  
*No passo 7 do fluxo básico, caso algum campo esteja vazio ou com formato incorreto.*
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo retorna ao passo 7 do fluxo básico.

**Desistência:**  
*Entre os passos 4 e 8 do fluxo básico caso a **Recepcionista** cancele a operação ou não confirme.*
1. O sistema descarta as alterações informadas e mantém os dados do paciente sem alteração.
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - Os campos obrigatórios são CPF, nome, sobrenome 1, sexo e telefone 1.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O paciente deve estar cadastrado no sistema.

### Condições Posteriores:
> - Edição: os dados alterados ficam gravados
> - As alterações são registradas (data, hora e **Recepcionista**)
> - O sistema exibe a mensagem “Dados do paciente atualizados com sucesso!”.

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
5. O sistema armazena os dados do médico no banco de dados e gera a grade de horários do médico.

### Fluxos Alternativos:
**CRM já cadastrado no sistema:**
*No passo 4 do fluxo básico, caso o sistema identifique que o CRM e a UF informados já pertencem a outro médico cadastrado.*
1. O sistema exibe a mensagem de erro: "CRM já cadastrado no sistema".
2. O sistema oferece a opção de corrigir os dados informados ou cancelar a operação.
3. Se a **Recepcionista** escolher corrigir, o fluxo retorna ao passo 3 do fluxo básico. Se escolher cancelar, o caso de uso é encerrado.

**Campos obrigatórios não preenchidos ou dados inválidos:**
*No passo 3 do fluxo básico, caso algum campo obrigatório esteja vazio ou com formato incorreto.*
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
## Caso de Uso 7: Alterar Agenda Médica

> Permite à **Recepcionista** registrar ausências ou novos horários disponíveis na agenda de um médico (dias ou intervalos de horário em que ele não atenderá, ou que passará a atender), informadas formalmente pelo médico fora do sistema, bloqueando ou disponibilizando esses horários para novos agendamentos. Também permite remover ausências registradas.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade “Alterar Agenda Médica”.
2. A **Recepcionista** informa o nome do médico.
3. O sistema lista os médicos que correspondem à busca (nome, especialidade e CRM) e a **Recepcionista** seleciona o médico desejado.
4. O sistema exibe os dados do médico, as ausências futuras já registradas (com a opção “Remover”), o formulário para registrar nova ausência e a opção “Adicionar horários de atendimento”.
5. A **Recepcionista** informa o motivo da ausência e adiciona um ou mais períodos. Para cada período, informa a data inicial e a data final (a mesma data, no caso de um único dia) e define se é o dia inteiro ou um intervalo de horário (hora inicial e hora final). Opcionalmente, marca a opção “Permanente” no período, alterando assim permanentemente a agenda daquele médico.
6. A **Recepcionista** clica em “Registrar Ausência”.
7. O sistema valida os campos informados.
8. O sistema verifica se existe consulta agendada em algum horário abrangido pelos períodos informados.
9. O sistema solicita confirmação: “Deseja bloquear os horários informados na agenda do médico?”.
10. A **Recepcionista** confirma.
11. O sistema registra a ausência, marca como indisponíveis os horários da agenda do médico abrangidos pelos períodos e registra data, hora e **Recepcionista** responsável pela alteração.

### Fluxos Alternativos:
**Médico não localizado:**  
*No passo 3 do fluxo básico, caso nenhum médico corresponda à busca.*
1. O sistema exibe a mensagem: “Médico não localizado”.
2. O caso de uso retorna ao 2 do fluxo básico e permite que a **Recepcionista** informe outro nome ou encerre o caso de uso.

**Campos obrigatórios não preenchidos ou dados inválidos:**  
*No passo 7 do fluxo básico, caso o motivo esteja vazio, nenhum período tenha sido informado, alguma data não seja futura, a hora final não seja posterior à hora inicial, ou os períodos se sobreponham entre si ou a ausências já registradas.*
1. O sistema bloqueia a gravação.
2. O sistema destaca visualmente os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo retorna ao passo 5 do fluxo básico.

**Conflito com consultas agendadas:**  
*No passo 8 do fluxo básico (ou no passo 11, caso uma consulta seja agendada durante a confirmação), caso exista consulta agendada que coincida, total ou parcialmente, com algum período informado.*
1. O sistema bloqueia o registro da ausência, sem alterar a agenda do médico.
2. O sistema exibe uma mensagem informando as datas e os horários das consultas em conflito.
3. A **Recepcionista** ajusta os períodos (o fluxo retorna ao passo 5 do fluxo básico) ou encerra o caso de uso para cancelar as consultas pelo caso de uso “Cancelar Consulta” e repetir o registro depois.

**Remover ausência:**  
*No passo 4 do fluxo básico, caso a **Recepcionista** selecione a opção “Remover” em uma ausência registrada.*
1. O sistema exibe os dados da ausência (período, horário e motivo) e solicita confirmação: “Deseja remover esta ausência? Os horários voltarão a ficar disponíveis para agendamento.”.
2. A **Recepcionista** confirma a remoção.
3. O sistema remove a ausência, marca como disponíveis os horários futuros da agenda do médico antes bloqueados por ela e registra data, hora e **Recepcionista** responsável pela alteração.
4. O sistema exibe a mensagem: “Ausência removida com sucesso!”.
5. O caso de uso é encerrado.

**Adicionar horários de atendimento:**  
*No passo 4 do fluxo básico, caso a **Recepcionista** selecione a opção “Adicionar horários de atendimento”.*
1. O sistema exibe o formulário de inclusão de horários.
2. A **Recepcionista** adiciona um ou mais períodos. Para cada período, informa a data inicial e a data final (a mesma data, no caso de um único dia) e o intervalo de horário de atendimento (hora inicial e hora final).
3. A **Recepcionista** clica em “Adicionar Horários”.
4. O sistema valida os campos informados. Opcionalmente, a **Recepcionista** pode marcar a opção “Permanente” no período, alterando assim permanentemente a agenda daquele médico.
5. O sistema solicita confirmação: “Deseja incluir os horários informados na agenda do médico?”.
6. A **Recepcionista** confirma.
7. O sistema gera os horários na agenda do médico, conforme a duração de consulta cadastrada para ele, marca-os como disponíveis e registra data, hora e **Recepcionista** responsável pela alteração.
8. O sistema exibe a mensagem: “Horários incluídos com sucesso!”.
9. O caso de uso é encerrado.
   
**Dados inválidos na inclusão de horários:**  
*No passo 4 do fluxo alternativo “Adicionar horários de atendimento”, caso nenhum período tenha sido informado, alguma data não seja futura, a hora final não seja posterior à hora inicial, os períodos se sobreponham entre si, ou algum período coincida, total ou parcialmente, com horários em que o médico já atende ou com uma ausência registrada.*
1. O sistema bloqueia a gravação.
2. O sistema exibe mensagem descritiva indicando os períodos inconsistentes e o motivo (horário já existente na agenda ou ausência registrada).
3. A **Recepcionista** corrige as informações e o fluxo retorna ao passo 2 do fluxo alternativo “Adicionar horários de atendimento”.

**Desistência:**  
*Entre os passos 5 e 10 do fluxo básico, ou em qualquer passo dos fluxos alternativos “Remover ausência” e “Adicionar horários de atendimento”, caso a **Recepcionista** cancele a operação ou não confirme.*
1. O sistema descarta as informações e mantém a agenda do médico sem alteração.
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - A ausência é informada formalmente pelo médico por meio externo ao sistema (por exemplo, e-mail). O sistema não solicita anexo nem outra forma de comprovação.
> - Somente datas futuras podem ser alteradas.
> - É permitido registrar ausência em datas em que o médico já não atende.
> - Período “Permanente”: o bloqueio ou inclusão vale a partir da data inicial, repetindo-se toda semana no mesmo dia da semana e horário, sem data final, ou seja, passa a ser um novo horário a mais ou a menos na agenda daquele médico, permanentemente.
> - O sistema deve garantir controle de concorrência para evitar que uma ausência seja registrada e uma consulta seja agendada no mesmo horário simultaneamente.
> - Horários bloqueados não são oferecidos no caso de uso “Agendar Consulta”.
> - Somente ausências com datas futuras podem ser removidas.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O médico deve estar cadastrado no sistema.

### Condições Posteriores:
> - Registro: os horários abrangidos ficam indisponíveis na agenda do médico, a alteração é registrada (data, hora e **Recepcionista**). O sistema exibe a mensagem “Ausência registrada com sucesso!”.
> - Remoção: os horários futuros voltam a ficar disponíveis, a alteração é registrada e o sistema exibe a mensagem “Ausência removida com sucesso!”.
> - Inclusão: os novos horários ficam disponíveis na agenda do médico e no caso de uso “Agendar Consulta”, a alteração é registrada (data, hora e **Recepcionista**) e o sistema exibe a mensagem “Horários incluídos com sucesso!”.

---