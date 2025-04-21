from flask import Flask # type: ignore
from prometheus_flask_exporter import PrometheusMetrics # type: ignore
import logging

# Configurar logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Inicializar o aplicativo Flask
app = Flask(__name__)

# Configurar o exportador de métricas
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Monitoring Docker App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)