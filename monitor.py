# ==========================
# Projeto: System Monitor PRO
# Autor: Briza Oliva Ribeiro
# ==========================

import psutil
import time
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime

def carregar_env():
    if os.path.exists(".env"):
        with open(".env") as f:
            for linha in f:
                if "=" in linha:
                    chave, valor = linha.strip().split("=", 1)
                    os.environ[chave] = valor

carregar_env()

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
INTERVAL = 5
LOG_FILE = "relatorio_sistema.txt"

EMAIL_REMETENTE = os.environ.get("EMAIL_REMETENTE", "")
EMAIL_SENHA = os.environ.get("EMAIL_SENHA", "")
EMAIL_DESTINO = os.environ.get("EMAIL_DESTINO", "")

def coletar_dados():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    return cpu, memoria

def gerar_log(cpu, memoria):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] CPU: {cpu}% | Memória: {memoria}%\n"
    with open(LOG_FILE, "a") as arquivo:
        arquivo.write(linha)
    print(linha.strip())

def enviar_email_alerta(mensagem):
    try:
        msg = MIMEText(mensagem)
        msg["Subject"] = "ALERTA: Uso alto de sistema"
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = EMAIL_DESTINO
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)
            servidor.send_message(msg)
        print("[EMAIL] Alerta enviado!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

def verificar_alerta(cpu, memoria):
    alertas = []
    if cpu > CPU_THRESHOLD:
        alertas.append(f"CPU em {cpu}% (limite: {CPU_THRESHOLD}%)")
    if memoria > MEM_THRESHOLD:
        alertas.append(f"Memória em {memoria}% (limite: {MEM_THRESHOLD}%)")
    if alertas:
        mensagem = "Alerta de uso alto:\n" + "\n".join(alertas)
        print(f"[ALERTA] {mensagem}")
        enviar_email_alerta(mensagem)

if __name__ == "__main__":
    print("Monitor iniciado. Pressione Ctrl+C para encerrar.\n")
    try:
        while True:
            cpu, memoria = coletar_dados()
            gerar_log(cpu, memoria)
            verificar_alerta(cpu, memoria)
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitor encerrado.")