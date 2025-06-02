
# Teste de Performance da API ViaCEP com Apache JMeter
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![LinkedIn](https://img.shields.io/badge/-Apache_Jmeter-D22128?style=for-the-badge&logo=linkedin&logoColor=F04178)

Este projeto tem como objetivo realizar testes de desempenho em uma API REST de consulta ao [ViaCEP](https://viacep.com.br/), criada com **Python e Flask**, utilizando o **Apache JMeter** para medir métricas como tempo de resposta, taxa de transferência, porcentagem de erro, conexões ativas e pico de conexões.

---
## Ferramentas Utilizadas

- **Python 3.x**
- **Flask**
- **Apache JMeter** 5.x
- Plugin: **Ultimate Thread Group** (`jp@gc`)
- Plugin: **Active Threads Over Time**

---

## API REST (Flask)

A API desenvolvida em Python tem como objetivo redirecionar requisições para o serviço do ViaCEP e retornar os dados em formato JSON. Abaixo está o código:

```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/cep/<cep>')
def consultar_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'Erro': 'CEP não foi encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Cenário de Teste

### Objetivo

Avaliar a capacidade de resposta da API sob carga crescente de usuários simultâneos, identificando gargalos, erros ou tempos de espera excessivos.

---

### Endpoint testado

O endpoint da API REST desenvolvida em Flask é:

http://localhost:5000/cep/44032221

Essa rota consome os dados da API pública ViaCEP e retorna o resultado em formato JSON.

---

### ⚙️ Configuração do Thread Group

| Start Threads Count | Initial Delay (s) | Startup Time (s) | Hold Load For (s) | Shutdown Time (s) |
|--------|---------|----------------|----------------|----------|
| 50     | 0     | 25            | 20            |5        |
| 100    | 25     | 25            | 20            | 10        |

---

**Imagem do Ultimate Thread Group**  

![Ultimate Thread Group](imagens/jp%40gc%20-%20Ultimate%20Thread%20Group.png)
`jp@gc - Ultimate Thread Group.png`

## Evolução dos Usuários Ativos

O gráfico a seguir representa a variação no número de conexões simultâneas (Active Threads) durante o teste:

**Imagem do gráfico "Active Threads Over Time"** 

![Gráfico de Threads](imagens/jp%40gc%20-%20Active%20Threads%20Over%20Time.png)
`jp@gc - Active Threads Over Time.png`

### Pico de Conexões Ativas

O número de Active Threads atingiu o pico de 135 conexões simultâneas, aproximadamente aos 50 segundos. Após isso, iniciou-se a desaceleração e finalização do teste, conforme a configuração da carga.

---

## Resultados

### Relatório Resumido

**Imagem do Summary Report**  

![Relatório Summary](imagens/Summary%20Report.png)
`Summary Report.png`

**Principais métricas obtidas:**

- **Total de Requisições:** 1608  
- **Tempo Médio de Resposta:** 3777 ms  
- **Erro (%):** 6,16% 
- **Throughput:** 18,9 requisições/segundo  
- **Recebimento:** 84,75 KB/s  
- **Envio:** 2,28 KB/s
- Desvio Padrão: 4805,66 ms
- Tamanho Médio da Resposta: 4602,9 bytes

---

### Relatório Detalhado (Aggregate Report)

**Imagem do Aggregate Report**  

![Relatório Aggregate](imagens/Aggregate%20Report.png)
`Aggregate Report.png`

- Tempo Mínimo: 1036 ms
- Tempo Máximo: 20046 ms
- Mediana: 1313 ms
- 90 Percentil: 8432 ms
- 95 Percentil: 19850 ms
- 99 Percentil: 19979 ms

A mediana de 1313 ms indica que 50% das requisições foram respondidas em até esse tempo. No entanto, os percentis superiores revelam grandes variações e picos de latência, com 1% das requisições ultrapassando 19 segundos.

---

## Resumo Técnico da Atividade

### Tempo de Resposta
- **Tempo Médio**: 3777 ms
- **Tempo Mínimo**: 1036 ms
- **Tempo Máximo**: 20046 ms
- **Mediana**: 1313 ms
- **Percentil 90**: 8432 ms
- **Percentil 95**: 19850 ms
- **Percentil 99**: 19979 ms

### Taxa de Transferência (Throughput)
- **Throughput**: 18,9 requisições por segundo
- **Recebimento**: 84,75 KB/s
- **Envio**: 2,28 KB/s

### Erro Percentual
- **Erro Total**: 6,16% das requisições apresentaram falhas

### Conexões Ativas
- **Quantidade ativa durante o teste**: Variação observada no gráfico “Active Threads Over Time”
- **Indicador de carga simultânea**: Utilizado o plugin jp@gc - Active Threads Over Time

### Pico de Conexões
- **Pico observado**: 135 conexões simultâneas
- **Momento de maior carga**: Aproximadamente aos 50 segundos de teste

---

## Análise

A API, desenvolvida com Flask, apresentou respostas estáveis em termos médios, mas demonstrou **limitações sob picos de carga**, como:

- Tempos de resposta variando amplamente  
- Latências altas em percentis superiores
- Pequena taxa de erros (6,16%) — ainda assim relevante, dado o baixo volume de requisições

A **dependência de um serviço externo (ViaCEP)** também é um fator que pode ter impactado o desempenho e causado lentidão nos tempos de resposta.

---

## Conclusão

A API é funcional em ambientes com baixa carga, mas não está otimizada para uso com muitos acessos simultâneos.
O uso do Apache JMeter mostrou-se altamente eficaz neste contexto. Como ferramenta open source, ele oferece um conjunto robusto de recursos para simular múltiplos usuários simultâneos, configurar diferentes padrões de carga (como ramp-up e pico), além de fornecer relatórios detalhados sobre tempos de resposta, throughput, erros e utilização de recursos.

---

## Anexos
- Código-fonte da API
- Plano de Teste JMeter (.jmx)
- Prints dos Relatórios (.png)
