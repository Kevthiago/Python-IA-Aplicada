# Análise de Resenhas de Aplicativos com IA

Este projeto realiza a análise automática de resenhas de aplicativos utilizando inteligência artificial através da **API da Groq**. O script lê resenhas de um arquivo de texto, as envia para um modelo de IA para extrair dados estruturados (usuário, sentimento, etc.), e, por fim, gera relatórios consolidados em múltiplos formatos.

---

## Funcionalidades

-   Leitura de resenhas a partir de um arquivo `.txt`.
-   Integração com a API da Groq para processamento de linguagem natural.
-   Extração de informações estruturadas de cada resenha em formato JSON:
    -   `usuario`
    -   `resenha original`
    -   `resenha_pt` (tradução para português)
    -   `avaliacao` (sentimento classificado como `Positiva`, `Negativa` ou `Neutra`)
-   Contagem e resumo das avaliações por categoria.
-   ** Geração de Arquivos:**
    -   Cria um arquivo **`resenhas_analisadas.csv`** com todos os dados estruturados, ideal para análise em planilhas (Excel, Google Sheets) ou outras ferramentas de dados.
    -   Cria um relatório de texto **`relatorio_analise.txt`** formatado para leitura, contendo o resumo da análise e os detalhes de cada resenha.

---

## Tecnologias e Dependências

-   **Python 3.10+**
-   **Pandas:** Para manipulação, estruturação e exportação dos dados para CSV.
-   **Groq:** Cliente oficial para interagir com a API da Groq.
-   **Python-dotenv:** Para gerenciamento de chaves de API e outras variáveis de ambiente.

---

## Estrutura do Projeto

```bash
.
├── .env                  # Arquivo com variáveis de ambiente (GROQ_API_KEY)
├── groq_Connect.py       # Funções de integração com a API da Groq
├── main.py               # Script principal de análise
├── resenhas_app_gpt.txt  # Arquivo de entrada com as resenhas (uma por linha)
├── README.md             # Este arquivo
│
└── # Arquivos gerados após a execução:
    ├── resenhas_analisadas.csv  # [ARQUIVO GERADO] Planilha com dados completos
    └── relatorio_analise.txt    # [ARQUIVO GERADO] Relatório de texto para leitura
```

---

## Como Usar

### Pré-requisitos

-   Python 3.10 ou superior instalado.
-   Uma chave de API da [Groq](https://groq.com/).

### Passos de Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/analise-resenhas-ia.git](https://github.com/seu-usuario/analise-resenhas-ia.git)
    cd analise-resenhas-ia
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install pandas groq python-dotenv
    ```
    *Obs: Para facilitar, você pode criar um arquivo `requirements.txt` com o conteúdo acima e instalar com `pip install -r requirements.txt`.*

4.  **Configure a variável de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da Groq API:
    ```ini
    GROQ_API_KEY="sua_chave_aqui"
    ```

5.  **Adicione suas resenhas:**
    Insira as resenhas no arquivo `resenhas_app_gpt.txt`, com uma resenha por linha.

6.  **Execute o script principal:**
    ```bash
    python main.py
    ```

---

## Saída Esperada

1. A execução do script exibirá no terminal:

- Confirmação de carregamento do arquivo de resenhas.
- A resposta JSON bruta recebida do modelo.
- Um resumo da contagem de avaliações (Positivas, Negativas, Neutras).
- Um relatório detalhado e formatado de cada resenha.

2. Arquivos Gerados:
   
- Na pasta do projeto, você encontrará dois novos arquivos:
    - resenhas_analisadas.csv: Uma planilha contendo as colunas usuario, resenha original, resenha_pt e avaliacao.
    - relatorio_analise.txt: Um documento de texto com um resumo claro e a lista completa de todas as resenhas analisadas,        formatadas para fácil leitura.

#### Exemplo de Saída:

```text
Contagem de avaliações:
- Positiva: 10
- Negativa: 3
- Neutra: 2

Itens unidos em uma string:
Usuário: João, Resenha: Excelente app, Avaliação: Positiva | Usuário: Maria, Resenha: Problemas na instalação, Avaliação: Negativa | ...
```

---

## Personalização

-   **Alterar modelo ou parâmetros:** Ajuste `temperature`, `max_completion_tokens`, `top_p` e `reasoning_effort` diretamente no arquivo `groq_Connect.py`.
-   **Formato de saída JSON:** O prompt que define a estrutura do JSON pode ser modificado na variável `prompt` dentro do arquivo `main.py`.

---

## Observações

-   Certifique-se de que o arquivo de resenhas (`resenhas_app_gpt.txt`) esteja no mesmo diretório que o script principal.
-   A qualidade da análise depende da consistência das resenhas fornecidas.
-   Sempre valide a estrutura da saída JSON do modelo antes de utilizá-la em um ambiente de produção.

---

## Links Úteis

-   [Documentação da Groq API](https://console.groq.com/docs)
-   [Documentação do pandas](https://pandas.pydata.org/docs/)
-   [Repositório do python-dotenv](https://github.com/theskumar/python-dotenv)

---

## Autor

Este projeto foi desenvolvido por **Kevin Thiago**, estudante de Ciência da Computação.

Foi criado durante o curso **"Python: Inteligência Artificial Aplicada"**, como parte da carreira de **Especialista em IA** da [Alura](https://www.alura.com.br/).

---

## Licença

Este projeto está licenciado sob a Licença MIT.
