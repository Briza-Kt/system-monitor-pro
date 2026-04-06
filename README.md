# System Monitor PRO

Script Python para monitoramento de CPU e memória em tempo real, com geração de logs e alertas por email.

## Funcionalidades
- Monitoramento contínuo de CPU e RAM a cada 5 segundos
- Geração de log com timestamp em arquivo .txt
- Alerta por email quando uso ultrapassa o limite configurado
- Credenciais protegidas via variáveis de ambiente (.env)

## Tecnologias
- Python 3
- psutil
- smtplib (biblioteca nativa)

## Como usar

### 1. Clone o repositório
git clone https://github.com/Briza-Kt/system-monitor-pro.git
cd system-monitor-pro

### 2. Crie o ambiente virtual e instale a dependência
python3 -m venv venv
source venv/bin/activate
pip install psutil

### 3. Configure o .env
Crie um arquivo .env na raiz do projeto:
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_app_password_gmail
EMAIL_DESTINO=destino@gmail.com

### 4. Execute
python3 monitor.py

## Exemplo de saída
[2026-04-06 20:17:14] CPU: 12.5% | Memória: 54.3%
[2026-04-06 20:17:19] CPU: 8.2% | Memória: 54.3%

## Configurações
No topo do monitor.py você pode ajustar:
- CPU_THRESHOLD: limite de CPU para disparo do alerta (padrão: 80%)
- MEM_THRESHOLD: limite de memória (padrão: 80%)
- INTERVAL: intervalo entre leituras em segundos (padrão: 5)