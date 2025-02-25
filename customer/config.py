import os


class Config:
  
    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = "redis"
    CACHE_REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = os.getenv("REDIS_DB_URL", "redis://default:redispw@localhost:49153")
    CACHE_DEFAULT_TIMEOUT = 500
    SQLALCHEMY_DATABASE_URI = os.getenv("COMMON_DB_URL","postgresql+psycopg2://ipss_dev:AT4eqHUYr98475fhdNcuaRsDev@142.93.209.90:5433/ipss_dev")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True
    }
    SQLALCHEMY_ECHO = True
    IS_WORKER = False
    IPSS_PERMISSIONS = [{
        'module_name': "CRM Customer",
        'module_group': "Lead's Activities",
        'module_id': "crm_customer",
        'module_description': "Configuration of customers.Usually this type of system congiurations   "
                              "can be given to any user of the CRM system ",
        'project_id': "ipss_crm",
        'permissions': ['list', 'view', 'add', 'edit', 'delete', 'import', 'export']

    },
        {
            'module_name': "Vendor Configuration",
            'module_group': "Configuration",
            'module_id': "vendor_asset",
            'module_description': "Configuration of customers.Usually this type of system congiurations   "
                                  "can be given to any user of the CRM system ",
            'project_id': "Asset Management",
            'permissions': ['list', 'view', 'add', 'edit', 'delete']

        },
        {
            'module_name': "Service Provider Configuration",
            'module_group': "Configuration",
            'module_id': "service_provider_asset",
            'module_description': "Configuration of customers.Usually this type of system congiurations   "
                                  "can be given to any user of the CRM system ",
            'project_id': "Asset Management",
            'permissions': ['list', 'view', 'add', 'edit', 'delete']

        }
    ]
