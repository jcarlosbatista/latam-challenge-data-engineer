# 📊 Resultados do Challenge - LATAM Data Engineer

## 🧾 Objetivo Geral
Analisar um conjunto de dados com mais de 600 mil tweets relacionados aos protestos dos agricultores na Índia, utilizando Python. O desafio consistiu em responder a 3 perguntas específicas relacionadas à atividade de usuários, popularidade de tweets e influência internacional, com medição de tempo e memória para cada operação.

---

## ✅ Etapas Realizadas

### 1. Preparação do Ambiente
- Criação de ambiente virtual `.venv`
- Instalação do pacote `memory-profiler` para medir uso de memória
- Organização modular com scripts Python separados para cada questão e métrica (tempo/memória)

### 2. Estrutura de Arquivos

| Arquivo         | Descrição                                      |
|-----------------|------------------------------------------------|
| `q1_time.py`     | Usuário mais ativo por dia (tempo)             |
| `q1_memory.py`   | Usuário mais ativo por dia (memória)           |
| `q2_time.py`     | Top 10 tweets mais curtidos (tempo)            |
| `q2_memory.py`   | Top 10 tweets mais curtidos (memória)          |
| `q3_time.py`     | Países mais mencionados (tempo)                |
| `q3_memory.py`   | Países mais mencionados (memória)              |

---

## 🧠 Q1 - Usuário mais ativo por dia

### 🔹 Tempo de execução: 1.49 segundos  
### 🔹 Uso de memória: 0.12 MiB

| Data       | Usuário mais ativo      |
|------------|--------------------------|
| 2021-02-12 | RanbirS00614606          |
| 2021-02-13 | MaanDee08215437          |
| 2021-02-14 | rebelpacifist            |
| 2021-02-15 | jot__b                   |
| 2021-02-16 | jot__b                   |
| 2021-02-17 | RaaJVinderkaur           |
| 2021-02-18 | neetuanjle_nitu          |
| 2021-02-19 | Preetm91                 |
| 2021-02-20 | MangalJ23056160          |
| 2021-02-21 | Surrypuria               |
| 2021-02-22 | preetysaini321           |
| 2021-02-23 | Surrypuria               |
| 2021-02-24 | preetysaini321           |

**Explicação:** Foi realizada a contagem de tweets por usuário por data, retornando o usuário com mais postagens para cada dia.

---

## ❤️ Q2 - Top 10 Tweets mais curtidos

### 🔹 Tempo de execução: 1.49 segundos  
### 🔹 Uso de memória: 7.75 MiB

| # | Likes | Tweet (resumo) |
|--|-------|-----------------|
| 1 | 27888 | Protests na Alemanha comparados à Índia |
| 2 | 25824 | Comerciante fugiu com 200 milhões em grãos |
| 3 | 19284 | Poema sobre resistência |
| 4 | 19198 | Reflexão sobre coragem |
| 5 | 17325 | Vídeo comovente de agricultores |
| 6 | 15582 | Crítica à sociedade atual |
| 7 | 12949 | Bollywood traindo os agricultores |
| 8 | 12782 | Citação sobre amizade e oposição |
| 9 | 12317 | Agradecimento em assembleia |
|10 | 12273 | Realidade na fronteira de Delhi |

**Explicação:** Foram extraídos os 10 tweets com maior número de curtidas, identificando mensagens com maior repercussão e engajamento.

---

## 🌍 Q3 - Países mais mencionados

### 🔹 Tempo de execução: 1.78 segundos  
### 🔹 Uso de memória: 0.00 MiB

| País      | Menções |
|-----------|---------|
| Índia     | 8553    |
| Canadá    | 263     |
| Austrália | 167     |
| Reino Unido | 163   |
| EUA       | 80      |

**Explicação:** O conteúdo dos tweets foi escaneado com regex para detectar menções explícitas aos países-alvo. Índia lidera, seguida por países que demonstraram apoio à causa.

---

## 📈 Conclusão

- **Q1** foi eficiente em tempo e memória, ideal para análise diária de atividade.
- **Q2** exigiu mais memória devido ao volume de texto.
- **Q3** mostrou impacto internacional com desempenho excelente.
- Toda a análise foi feita de forma modular, escalável e com boas práticas de engenharia de dados.

---