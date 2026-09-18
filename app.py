from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Employee Management Application</h1>
    <h2>Welcome to DevOps + Kubernetes!</h2>
    <p>Application Version: 1.0</p>
    <p>Environment: Kubernetes</p>
    """

@app.route("/health")
def health():
    return "Application is Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
