import os

# URL do site que deseja abrir
url = "https://pbs.twimg.com/media/EZH1UN-WoAAPPdz?format=jpg&name=medium"

# Nome do agendamento
task_name = "AbrirNavegadorPadrao"

# Intervalo de repetição (em minutos)
interval = 1

# Cria o comando para agendar a tarefa usando "cmd /c start" para garantir que o comando seja executado corretamente
command = f'schtasks /create /tn "{task_name}" /tr "cmd /c start {url}" /sc minute /mo {interval} /f'
    
# Executa o comando no sistema
os.system(command)

print(f"Tarefa '{task_name}' agendada para abrir {url} a cada {interval} minutos.")