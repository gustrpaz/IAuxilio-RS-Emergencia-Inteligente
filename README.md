# IAuxílio RS: Emergência Inteligente

O projeto **IAuxílio RS: Emergência Inteligente** é uma aplicação prática da inteligência artificial para lidar com situações de emergência, especialmente as enchentes ocorridas recentemente no Rio Grande do Sul.

## Objetivo
O objetivo principal é utilizar a inteligência artificial para gerar modelos de chamados com informações cruciais para diferentes níveis de emergência. Isso é feito fornecendo exemplos de entradas (relatos da situação) e saídas (instruções para lidar com a emergência).

## Funcionamento
Cada entrada descreve uma situação específica, desde grupos isolados em telhados até alagamentos em ruas, com diferentes níveis de gravidade e necessidade de intervenção. Com base nessas entradas, a IA gera respostas detalhadas, incluindo título, síntese da situação, prioridade, localização, recursos necessários e ações a serem tomadas.

Por exemplo, para uma situação de emergência máxima (Prioridade nível 5), como um grupo isolado em um telhado após inundações, a IA gerará um chamado urgente para resgate aéreo, destacando os recursos necessários e as ações a serem realizadas para salvar as vítimas.

Já para emergências de menor gravidade (Prioridade nível 1), como um bueiro entupido em uma rua, a IA gerará um chamado de manutenção preventiva, com recursos e ações adequadas para resolver o problema com baixa prioridade.

## Benefícios
Essa abordagem permite uma resposta mais eficiente e direcionada a situações de emergência, otimizando os recursos disponíveis e garantindo uma resposta adequada a cada nível de gravidade da situação.

Este repositório contém os arquivos e códigos necessários para executar a aplicação IAuxílio RS: Emergência Inteligente.

## Como utilizar com Google Colab

### Requisitos:
- Conta no Google Colab
- Navegador web compatível
- API Key do Gemini: Você precisará gerar uma API Key para usar o Gemini. As instruções sobre como gerar uma API Key podem ser encontradas na documentação do Gemini: [Documentação do Gemini](https://ai.google.dev/gemini-api/docs)

### Passo a passo:

1. Acesse o notebook do projeto:
   - Abra o navegador web e acesse o seguinte link: [Google Colab](https://colab.research.google.com/)
   - Substitua `https://colab.research.google.com/` pelo link do seu notebook no Colab.
     
2. Conecte ao Google Drive:
   - Se necessário, conecte-se à sua conta do Google Drive para acessar os arquivos do projeto.
   - No menu do Colab, clique em "Arquivo" e depois em "Conectar ao Drive".
   - Siga as instruções na tela para autorizar o Colab a acessar seus arquivos.
     
3. Obtenha sua API Key do Gemini:
   - Siga as instruções na documentação do Gemini para gerar uma API Key: [Documentação do Gemini](https://ai.google.dev/gemini-api/docs)
   - Anote sua API Key com segurança.
     
4. Configure a variável de ambiente:
   - No Colab, clique no ícone de chave inglesa no canto superior direito da tela.
   - Selecione "Configurações da Conta".
   - Na guia "Segurança", clique em "Criar segredo".
   - No campo "Nome", digite SECRET_KEY.
   - No campo "Valor", cole sua API Key do Gemini.
   - Clique em "Criar".
     
5. Execute o notebook:
   - Execute os blocos de códigos clicando no botão de play.
   - O notebook será executado célula por célula.
   - Aguarde a execução de todas as células antes de continuar.
     
6. Interaja com o prompt de conversação:
   - Na última célula do notebook, você encontrará instruções sobre como interagir com o prompt de conversação.
   - Digite suas mensagens e pressione Enter para enviar.
   - O Gemini responderá às suas mensagens.

### Dicas:
- Experimente diferentes prompts, insira relatos pensando no cenário de urgência e necessidade.
- O Gemini ainda está em desenvolvimento, então suas respostas podem não ser sempre perfeitas.

## Recursos adicionais:
- [Documentação do Gemini](https://ai.google.dev/gemini-api/docs)
- [Exemplos de prompts de conversação](https://ai.google.dev/gemini-api/docs)
- [Comunidade do Gemini](https://ai.google.dev/gemini-api/docs)
Este texto pode ser copiado e colado diretamente em um arquivo README.md no se

Esperamos que o IAuxílio RS: Emergência Inteligente possa ser útil e auxiliar nas operações de socorro durante situações de emergência no Rio Grande do Sul.
