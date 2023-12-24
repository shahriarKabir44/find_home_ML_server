from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pandas as pd
import joblib

hostName = "localhost"
serverPort = 8080


def predict(data):
    # X = df.drop('Loan_Status', axis=1)
    df = pd.DataFrame.from_dict(data, orient='index')
    model = joblib.load('loan_status_predict')
    result = model.predict(df)

    if result.any() == 1:
        return {"outcome": 1}
    else:
        return {"outcome": 0}


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        # Set response headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'Data received successfully'}
        self.wfile.write(bytes(json.dumps(response), 'utf-8'))

    def useCORS(self):
        self.send_response(200, "OK")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header('Content-Type', 'application/json')

        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header('Content-Type', 'application/json')

        self.end_headers()

    def do_POST(self):
        self.useCORS()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        json_data = json.loads(post_data.decode('utf-8'))

        response = (predict(json_data))

        self.wfile.write(bytes(json.dumps(response), 'utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
