import requests
import json
import sys

# --- CONFIGURAÇÃO ---
# Coloque sua chave de API aqui
API_KEY = "SUA_CHAVE_AQUI" 
CIDADE = "Sao Paulo"
PAIS = "BR" # Código do país (ex: BR para Brasil)

# URL base da API do OpenWeatherMap para dados atuais
URL_BASE = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE},{PAIS}&appid={API_KEY}&units=metric&lang=pt"

def obter_previsao_tempo():
    """
    Consome a API do OpenWeatherMap, trata erros e exibe os dados.
    (Atividades 1, 2 e 3)
    """
    print(f"Buscando dados de tempo para: {CIDADE}, {PAIS}...")
    
    try:
        # Atividade 1: Fazer a requisição
        resposta = requests.get(URL_BASE, timeout=10) # Define um timeout para evitar espera infinita
        
        # Atividade 3: Tratar falhas na requisição HTTP (Códigos 4xx ou 5xx)
        resposta.raise_for_status() 
        
        # Converter a resposta JSON para um dicionário Python
        dados = resposta.json()
        
        # --- Atividade 2: Exibir informações específicas ---
        
        # Verifica se a API retornou os dados esperados
        if dados.get("cod") != 200:
            print(f"\n[ERRO DA API] Código: {dados.get('cod', 'N/A')}. Mensagem: {dados.get('message', 'Erro desconhecido')}")
            return
            
        temperatura_atual = dados["main"]["temp"]
        sensacao_termica = dados["main"]["feels_like"]
        condicao_climatica = dados["weather"][0]["description"].capitalize()
        humidade = dados["main"]["humidity"]
        velocidade_vento = dados["wind"]["speed"] # Velocidade em metros/segundo (m/s)

        print("\n====================================")
        print(f"🌤️ PREVISÃO DO TEMPO PARA {CIDADE.upper()}")
        print("====================================")
        print(f"➡️ Condição: {condicao_climatica}")
        print(f"🌡️ Temperatura Atual: {temperatura_atual:.1f}°C")
        print(f"🥵 Sensação Térmica: {sensacao_termica:.1f}°C")
        print(f"💧 Umidade do Ar: {humidade}%")
        print(f"💨 Vento: {velocidade_vento} m/s")
        print("====================================")

    except requests.exceptions.RequestException as e:
        # Atividade 3: Tratar erros de conexão (DNS, timeout, falha na rede, etc.)
        print(f"\n[ERRO DE CONEXÃO] Falha ao tentar se conectar à API: {e}")
        print("Verifique sua conexão com a internet ou a URL da API.")
    
    except json.JSONDecodeError:
        # Atividade 3: Tratar respostas inválidas (não é um JSON válido)
        print("\n[ERRO DE DADOS] A API retornou uma resposta inválida (não é JSON).")
    
    except KeyError as e:
        # Trata se algum campo essencial (como 'main' ou 'temp') estiver faltando na resposta
        print(f"\n[ERRO DE CHAVE] O dado esperado '{e}' não foi encontrado na resposta da API.")
    
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO] Ocorreu um erro: {e}")

# Chamar a função principal
if __name__ == "__main__":
    if API_KEY == "SUA_CHAVE_AQUI":
        print("🚨 ATENÇÃO: Por favor, substitua 'SUA_CHAVE_AQUI' pela sua chave de API do OpenWeatherMap.")
    else:
        obter_previsao_tempo()