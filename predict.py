# predict.py
import sys
import joblib
import pandas as pd
from urllib.parse import urlparse

# --------------------------------------------------
# 1. Função utilitária: extrai as 9 features exigidas
# --------------------------------------------------
def extract_features(url: str) -> dict:
    """Gera um dicionário com as features esperadas pelo modelo."""
    parsed = urlparse(url)

    return {
        # 1) Comprimento da URL
        "URLURL_Length": len(url),

        # 2) Presença do caractere '@'
        "having_At_Symbol": 1 if "@" in url else 0,

        # 3) Google_Index – placeholder: 1 (indexado) / 0 (não)
        #    Sem chamada de API externa para manter o script offline.
        "Google_Index": 1,

        # 4) SSLfinal_State – 1 para HTTPS, 0 para HTTP
        "SSLfinal_State": 1 if parsed.scheme == "https" else 0,

        # 5) popUpWidnow – placeholder (0 = não, 1 = sim)
        "popUpWidnow": 0,

        # 6) DNSRecord – placeholder (1 = DNS válido)
        "DNSRecord": 1,

        # 7) age_of_domain – placeholder (1 = domínio velho, 0 = novo)
        "age_of_domain": 1,

        # 8) Statistical_report – placeholder (1 = limpo, 0 = suspeito)
        "Statistical_report": 1,
     
        #9) Web Traffic
        "web_traffic": 1,
    }


# --------------------------------------------------
# 2. Main: carrega modelo e faz a predição
# --------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <url>")
        sys.exit(1)

    url_arg = sys.argv[1]

    # Carrega o modelo treinado (caminho relativo ao Dockerfile)
    model = joblib.load("models/phishing_clf.pkl")

    # Constrói o DataFrame com uma única linha
    features = extract_features(url_arg)
    X = pd.DataFrame([features])

    # Predição
    pred = model.predict(X)[0]
    label = "Phishing" if pred == 1 else "Legitimate"

    print(f"URL analysed  : {url_arg}")
    print(f"Prediction    : {label}")
