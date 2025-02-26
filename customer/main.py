from customer.customer.app import create_app
from customer.customer.config import Config

app = create_app(Config)


if __name__ == "__main__":
    app.run()
