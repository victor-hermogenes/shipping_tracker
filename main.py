import PySimpleGUI as sg
import requests

# Função para fazer a solicitação à API de rastreamento
def get_tracking_info(tracking_number):
    api_key = "SUA_CHAVE_DE_API_AQUI"
    url = f"https://api.transportadora.com/rastreamento/{tracking_number}?api_key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        tracking_data = response.json()
        return tracking_data
    else:
        return None

# Layout da interface gráfica
theme = sg.theme("DarkAmber")
layout = [
    [sg.Text("Digite o número de rastreamento:"), sg.InputText(key="tracking_number")],
    [sg.Button("Rastrear"), sg.Button("Sair")],
    [sg.Output(size=(40, 10))]
]

# Criar a janela
window = sg.Window("Rastreamento de Frete", layout)

# Loop para receber e processar eventos
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Rastrear":
        tracking_number = values["tracking_number"]
        tracking_info = get_tracking_info(tracking_number)
        
        if tracking_info:
            print("Informações de Rastreamento:")
            for status in tracking_info["status"]:
                print(f"Data: {status['date']}, Local: {status['location']}, Status: {status['status']}")
        else:
            print("Não foi possível obter informações de rastreamento.")
            
# Fechar a janela ao sair
window.close()