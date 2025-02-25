from Compliance.customer.app import create_app
from Compliance.customer.config import Config

app = create_app(Config)


if __name__ == "__main__":
    app.run()
