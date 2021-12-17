import app as serve
import os

if __name__ == "__main__":
    serve.app.run(debug=False, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
