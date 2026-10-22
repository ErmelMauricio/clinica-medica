# Especificações dos Casos de Uso

## Identificação dos Atores

- **Ator 1:** Recepcionista
>Responsável pelo cadastro e atualização de dados dos pacientes, consulta de disponibilidade de horários, realização, confirmação e cancelamento de agendamentos de consultas, envio de lembretes de consulta aos pacientes via WhatsApp.

- **Ator 2:** Médico
>Responsável pela realização do atendimento clínico, consulta ao prontuário do paciente, registro de diagnósticos e prescrição de medicamentos.

- **Ator 3:** Paciente
>Usuário que busca atendimento na clínica, responsável por solicitar marcação de consultas e solicitar o cancelamento de seus agendamentos.

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
## Caso de Uso 3: Registrar Atendimento Médico

>Permite ao **Médico** registrar as informações da consulta clínica realizada com o paciente, incluindo anamnese, sintomas, diagnóstico (CID) e prescrição médica no prontuário eletrônico.

### Ator Principal:
>**Médico**.

### Fluxo Básico:
1. O **Médico** visualiza a lista de pacientes com status "Aguardando Atendimento" na sua agenda do dia.
2. O **Médico** seleciona o paciente e clica em "Iniciar Atendimento".
3. O sistema registra o acesso ao prontuário no Histórico de Acessos ao Prontuário daquele paciente (nome do **Médico**, data e hora) e abre o prontuário eletrônico do paciente, exibindo histórico médico anterior e campos para o novo registro.
4. O **Médico** registra os detalhes do atendimento em texto.
5. Caso o **Médico** precise receitar medicamentos, solicitar exames ou conduta terapêutica, o sistema executa o caso de uso "Emitir Prescrição Médica".
6. O **Médico** finaliza o atendimento clicando em "Concluir Consulta".
7. O sistema valida os dados do prontuário, salva a evolução médica com os dados do médico que efetuou o atendimento.

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
>- Habilita a possibilidade de imprimir a prescrição.
>- O acesso ao prontuário fica registrado no Histórico de Acessos ao Prontuário do paciente (médico, data e hora).

### Ponto de Extensão:
> - **Caso de Uso Estendido: Emitir Prescrição Médica:**
	  *Ocorre apenas se o **Médico** julgar clinicamente necessário prescrever medicamentos ao paciente durante a consulta.*

---

## Caso de Uso 4: Registrar Pagamento

> Permite que a **Recepcionista** registre como o pagamento de uma consulta agendada foi realizado: para atendimento particular, a forma de pagamento e o comprovante anexado. Em caso de convênio, a operadora e o número da carteirinha.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico (Particular):
1. A **Recepcionista** acessa a funcionalidade "Registrar Pagamento".
2. A **Recepcionista** localiza o paciente informando o CPF.
3. O sistema exibe as consultas agendadas do paciente com pagamento pendente.
4. A **Recepcionista** seleciona a consulta desejada.
5. O sistema exibe os dados da consulta (paciente, médico, data, hora) e a modalidade de pagamento "Particular".
6. A **Recepcionista** seleciona a forma de pagamento (Pix, Débito ou Crédito) e anexa o comprovante (print ou foto).
7. Caso o paciente tenha pago com mais de uma forma, a **Recepcionista** repete o passo 6 para cada forma adicional.
8. A **Recepcionista** clica em "Registrar Pagamento".
9. O sistema valida os dados e armazena os registros e comprovantes, vinculando-os à consulta.

### Fluxos Alternativos:
**Pagamento via Convênio:**  
_No passo 5 do fluxo básico, a recepcionista pode selecionar também a opção "Convênio" como modalidade de pagamento._
1. O sistema solicita a operadora e o número da carteirinha.
2. A **Recepcionista** preenche os dados e clica em "Registrar Pagamento".
3. O sistema valida os campos e armazena os dados do convênio vinculados à consulta.
4. O fluxo segue para o passo 9 do fluxo básico (condições posteriores).

**Paciente sem consultas pendentes de pagamento:**  
_No passo 3 do fluxo básico, caso o paciente não possua consulta agendada com pagamento pendente._
1. O sistema exibe a mensagem: "Nenhuma consulta com pagamento pendente encontrada".
2. O caso de uso é encerrado.

**Comprovante não anexado ou arquivo inválido:**  
_No passo 6 ou 8 do fluxo básico, caso nenhum comprovante tenha sido anexado a uma forma de pagamento, ou o arquivo esteja em formato não permitido._
1. O sistema bloqueia a gravação.
2. O sistema exibe mensagem descritiva do problema.
3. A **Recepcionista** corrige o anexo e o fluxo retorna ao passo 6 do fluxo básico.

**Dados do convênio ausentes ou inválidos:**  
_No passo 2 do fluxo alternativo "Pagamento via Convênio", caso operadora ou número da carteirinha estejam vazios._
1. O sistema bloqueia a gravação.
2. O sistema destaca os campos inconsistentes com mensagem descritiva.
3. A **Recepcionista** corrige as informações e o fluxo retorna ao passo 2 do fluxo alternativo.

### Requisitos Especiais:
> - Na modalidade de pagamento "Particular" o sistema deve permitir mais de uma forma de pagamento e mais de um comprovante por consulta.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O paciente deve possuir consulta agendada e com pagamento pendente.

### Condições Posteriores:
> - O sistema exibe a mensagem: "Pagamento registrado com sucesso!".
> - A consulta é marcada com o status de pagamento "Registrado".
> - Comprovantes (particular) ou dados de convênio (operadora e carteirinha) ficam vinculados à consulta.
> - O sistema deve registrar data/hora e usuário responsável pelo registro, para fins de auditoria.

---

## Caso de Uso 5: Consultar Histórico do Prontuário

> Permite ao **Médico** consultar o histórico clínico de um paciente com consulta agendada com ele, ou atendido por ele nas últimas duas semanas, visualizando diagnósticos, prescrições médicas de atendimentos anteriores, com filtros por médico, data e especialidade.

### Ator Principal:
> **Médico**.

### Fluxo Básico:
1. O **Médico** acessa a funcionalidade "Consultar Histórico do Prontuário".
2. O sistema exibe a lista de pacientes com consulta agendada com o **Médico** ou atendidos por ele nos últimos 14 dias.
3. O **Médico** seleciona o paciente desejado.
4. O sistema registra o acesso no histórico de acessos do paciente (nome do médico, data e hora).
5. O sistema exibe o histórico do paciente em ordem cronológica decrescente, contendo diagnósticos e prescrições médicas anteriores, cada item identificado com o médico, a especialidade e a data.
6. O **Médico** consulta as informações e encerra a visualização.

### Fluxos Alternativos:
**Aplicar filtros de pesquisa:**  
_No passo 5 do fluxo básico, caso o **Médico** deseje refinar o histórico exibido._
1. O **Médico** informa um ou mais filtros: médico, período (data) e especialidade médica.
2. O sistema atualiza a listagem exibindo apenas os registros que atendem aos filtros.
3. O fluxo retorna ao passo 6 do fluxo básico.

**Nenhum registro encontrado:**  
_No passo 5 do fluxo básico ou no passo 2 do fluxo alternativo "Aplicar filtros de pesquisa", caso o paciente não possua histórico ou nenhum registro atenda aos filtros._
1. O sistema exibe a mensagem: "Nenhum registro encontrado".
2. O **Médico** pode alterar os filtros ou encerrar o caso de uso.

**Médico sem pacientes elegíveis:**  
_No passo 2 do fluxo básico, caso o **Médico** não possua pacientes com consulta agendada nem atendidos nos últimos 14 dias._
1. O sistema exibe a mensagem: "Nenhum paciente disponível para consulta de prontuário".
2. O caso de uso é encerrado.

### Requisitos Especiais:
> - O acesso ao prontuário deve ser restrito exclusivamente aos **Médicos**.
> - O **Médico** só pode acessar o prontuário de pacientes com consulta agendada com ele ou atendidos por ele há no máximo 14 dias (contados a partir de consultas com status "Realizada").
> - O histórico clínico é somente leitura: nenhum registro pode ser alterado ou excluído por este caso de uso.

### Condições Prévias:
> - O **Médico** deve estar autenticado no sistema com credenciais ativas.
> - O paciente deve possuir consulta agendada com o **Médico** ou ter sido atendido por ele nos últimos 14 dias.

### Condição Posterior:
> - O acesso fica registrado no histórico de acessos do paciente (médico, data e hora).

---

## Caso de Uso 6: Exportar Histórico de Acessos ao Prontuário

> Permite à **Recepcionista** exportar em PDF o histórico de acessos ao prontuário de um paciente, para fins de auditoria. O sistema não permite visualizar o histórico de acesso antes de exportar.

### Ator Principal:
> **Recepcionista**.

### Fluxo Básico:
1. A **Recepcionista** acessa a funcionalidade "Exportar Histórico de Acessos ao Prontuário".
2. A **Recepcionista** insere o CPF do paciente.
3. O sistema recupera os dados do paciente.
4. A **Recepcionista** clica em "Exportar PDF".
5. O sistema registra a exportação no histórico de acessos do paciente (nome da **Recepcionista**, data e hora).
6. O sistema gera o PDF com todos os registros do histórico de acessos do paciente (nome do médico ou da recepcionista, data e hora de cada acesso ou exportação, incluindo a exportação atual) e disponibiliza o download.

### Fluxos Alternativos:
**Paciente não encontrado:**  
_No passo 2 do fluxo básico, caso o CPF não corresponda a nenhum paciente cadastrado._
1. O sistema exibe a mensagem: "Paciente não localizado".
2. O caso de uso permanece no passo 2 do fluxo básico e permite que a recepcionista insira outro CPF ou encerre o caso de uso.

### Requisitos Especiais:
> - A exportação é restrita exclusivamente à **Recepcionista**.
> - O formato de exportação é PDF.
> - O histórico de acessos não pode ser visualizado em tela, somente exportado.
> - Toda exportação deve ser registrada no histórico de acessos com o nome da **Recepcionista**, data e hora.
> - O PDF não deve conter diagnósticos nem prescrições, apenas os dados de acesso.
> - O histórico de acessos é somente leitura: nenhum registro pode ser alterado ou excluído.

### Condições Prévias:
> - A **Recepcionista** deve estar autenticada no sistema com credenciais ativas.
> - O paciente deve estar cadastrado no sistema.

### Condições Posteriores:
> - A exportação fica registrada no histórico de acessos do paciente (recepcionista, data e hora).
> - O arquivo PDF é disponibilizado para download.

---

## Caso de Uso 7: Lembrete de Consulta via WhatsApp

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

## Caso de Uso 8: Cancelar Consulta

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

## Caso de Uso 9: Emitir Prescrição Médica

> Permite ao **Médico**, durante um atendimento, emitir uma prescrição médica (receita simples ou controlada) descrevendo os medicamentos, exame físico e conduta terapêutica, e imprimi-la.

#### Ator Principal:
> **Médico**.

#### Fluxo Básico:
1. O **Médico**, durante o atendimento "Registrar Atendimento Médico", aciona a opção “Emitir Prescrição Médica”.
2. O sistema solicita o tipo de receita: “Simples” ou “Controlada”.
3. O **Médico** seleciona o tipo de receita.
4. O sistema exibe o formulário da prescrição com os dados do paciente, a data de emissão e o campo de texto livre para o conteúdo clínico.
5. O **Médico** descreve por extenso os medicamentos e demais orientações no campo de texto.
6. O **Médico** clica em “Gerar Prescrição”.
7. O sistema valida o preenchimento do conteúdo, gera o documento e registra a prescrição no prontuário, vinculada ao atendimento (tipo, data de emissão, médico e conteúdo).
8. O sistema exibe o documento gerado indicando a impressão.
9. O **Médico** imprime o documento.
10. O caso de uso é encerrado e o fluxo retorna ao "Registrar Atendimento Médico". Caso precise emitir outra prescrição, o **Médico** repete o fluxo a partir do passo 1.

#### Fluxos Alternativos:
**Prescrição manuscrita (conteúdo em branco):**  
_No passo 5 do fluxo básico, caso o **Médico** prefira escrever o conteúdo à mão após a impressão._
1. O **Médico** clica em “Gerar com conteúdo em branco”, sem preencher o campo de texto.
2. O sistema gera o documento com os demais dados (clínica, paciente, data de emissão e campo do médico conforme o tipo de receita) e uma área em branco para escrita à mão.
3. O sistema registra a emissão no prontuário com a indicação “conteúdo manuscrito” (isto não é impresso na prescrição).
4. O fluxo segue para o passo 8 do fluxo básico.

**Desistência da prescrição:**  
_Entre os passos 2 e 6 do fluxo básico, caso o **Médico** cancele a operação._
1. O sistema descarta os dados informados, sem registrar nenhuma prescrição.
2. O fluxo retorna ao "Registrar Atendimento Médico".

#### Requisitos Especiais:
> - O caso de uso só pode ser acionado a partir do "Registrar Atendimento Médico" portanto é restrito exclusivamente ao **Médico**.
> - O sistema deve permitir mais de uma prescrição por atendimento.
> - O documento deve conter: dados da clínica, dados do paciente, data de emissão e conteúdo clínico descrito pelo **Médico**.
> - **Receita simples:** o sistema preenche automaticamente o nome e o CRM do médico (cadastrados no sistema) em um campo específico, deixando espaço para a assinatura manual após a impressão.
> - **Receita controlada:** o documento deixa espaço para o carimbo e a assinatura do médico, sem preenchimento automático.
> - Após gerada, a prescrição não pode ser editada nem excluída. Para corrigir, o **Médico** deve emitir uma nova.

#### Condições Prévias:
> - O **Médico** deve estar autenticado no sistema com credenciais ativas.
> - O atendimento deve estar em andamento ("Registrar Atendimento Médico" iniciado e ainda não concluído).

#### Condições Posteriores:
> - A prescrição fica registrada no prontuário, vinculada ao atendimento (tipo, data de emissão e médico).
> - O documento fica disponível para impressão.
> - A prescrição registrada não pode mais ser alterada.

---

## Caso de Uso 10: Editar Dados do Paciente

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