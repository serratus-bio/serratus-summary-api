SQLALCHEMY_DATABASE_URI = 'postgresql+auroradataapi://:@/summary'
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'aurora_cluster_arn': 'arn:aws:rds:us-east-1:797308887321:cluster:serratus-aurora',
        'secret_arn': 'arn:aws:secretsmanager:us-east-1:797308887321:secret:rds-db-credentials/cluster-KOFPN4Q2TKDBO5FHY6QO5M3S7Q/reader-TCMI1n'
    }
}
SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False

CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 0
