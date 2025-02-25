from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_restx import Api
from ipss_utils.ipss_db import IpssDb
from ipss_utils.ipss_api_doc import authorization_api_doc
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from ipss_utils.redis.ipss_redis import IpssRedis
from flask_redis import Redis

db_client = SQLAlchemy()
db_cache = Cache()
redis = Redis()
ipss_redis = IpssRedis()
rest_api = Api(
    title="Customer API",
    doc="/customer/api-docs",
    authorizations=authorization_api_doc,
    security='api_key',
    base_url="/customer",
    url_scheme="http"
)
ipss_db = IpssDb()


def create_app(config):
    app = Flask(
        __name__
    )
    app.config.from_object(config)

    db_client.init_app(app)
    db_cache.init_app(app)
    redis.init_app(app)
    ipss_redis.init_app(app, redis)
    # Registering routes
    rest_api.init_app(app)
    ipss_db.init_app(app, db_client)

    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[FlaskIntegration()]
    )

    with app.app_context():
        # Register route blueprints
        from .api.customer import customer_api_route
        rest_api.add_namespace(customer_api_route)
        from .api.customer_csv import csv_customer_api_route
        rest_api.add_namespace(csv_customer_api_route)
        return app
