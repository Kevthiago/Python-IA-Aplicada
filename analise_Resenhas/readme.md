# Análise de Resenhas de Aplicativos com IA

Este projeto realiza a análise automática de resenhas de aplicativos utilizando inteligência artificial através da **Groq API**. O código extrai informações das resenhas, as traduz para o português (quando necessário), classifica o sentimento e gera relatórios resumidos.

---

## 🔹 Funcionalidades

-   Leitura de resenhas a partir de um arquivo `.txt`.
-   Extração de informações estruturadas de cada resenha:
    -   Usuário
    -   Resenha original
    -   Resenha em português (`resenha_pt`)
    -   Avaliação (`Positiva`, `Negativa` ou `Neutra`)
-   Contagem automática de avaliações por categoria.
-   Consolidação de todas as resenhas em uma única string formatada.
-   Integração com a API Groq para processamento de linguagem natural.

---

## 🛠️ Tecnologias e Dependências

-   **Python 3.10+**
-   **Pandas:** Para manipulação e estruturação de dados.
-   **Groq:** Cliente oficial para interagir com a Groq API.
-   **Python-dotenv:** Para gerenciamento de variáveis de ambiente.
-   **JSON:** Para processamento de dados estruturados.

---

## ⚡ Estrutura do Projeto

```bash
.
├── .env                  # Arquivo com variáveis de ambiente (GROQ_API_KEY)
├── groq_Connect.py       # Funções de integração com a Groq API
├── main.py               # Script principal de análise
├── README.md             # Este arquivo
└── resenhas_app_gpt.txt  # Arquivo de entrada com as resenhas
```

---

## 🚀 Como Usar

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

## 📊 Saída Esperada

A execução do script exibirá no terminal:

-   A lista de resenhas carregadas do arquivo.
-   A resposta bruta do modelo de IA.
-   Uma lista de dicionários Python com os dados estruturados.
-   A contagem final de avaliações.
-   As resenhas unidas em uma única string.

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

## ⚙️ Personalização

-   **Alterar modelo ou parâmetros:** Ajuste `temperature`, `max_completion_tokens`, `top_p` e `reasoning_effort` diretamente no arquivo `groq_chat.py`.
-   **Formato de saída JSON:** O prompt que define a estrutura do JSON pode ser modificado na variável `prompt` dentro do arquivo `main.py`.

---

## 📝 Observações

-   Certifique-se de que o arquivo de resenhas (`resenhas_app_gpt.txt`) esteja no mesmo diretório que o script principal.
-   A qualidade da análise depende da consistência das resenhas fornecidas.
-   Sempre valide a estrutura da saída JSON do modelo antes de utilizá-la em um ambiente de produção.

---

## 🔗 Links Úteis

-   [Documentação da Groq API](https://console.groq.com/docs)
-   [Documentação do pandas](https://pandas.pydata.org/docs/)
-   [Repositório do python-dotenv](https://github.com/theskumar/python-dotenv)

---

## ✒️ Autor

Este projeto foi desenvolvido por **Kevin Thiago**, estudante de Ciência da Computação.

Foi criado durante o curso **"Python: Inteligência Artificial Aplicada"**, como parte da carreira de **Especialista em IA** da [Alura](https://www.alura.com.br/).

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT.
