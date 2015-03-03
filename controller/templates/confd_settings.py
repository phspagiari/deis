# security keys and auth tokens
SECRET_KEY = '{{ .deis_controller_secretKey }}'
BUILDER_KEY = '{{ .deis_controller_builderKey }}'

# scheduler settings
SCHEDULER_MODULE = 'scheduler.{{ or (.deis_controller_schedulerModule) "fleet" }}'
SCHEDULER_TARGET = '{{ or (.deis_controller_schedulerTarget) "/var/run/fleet.sock" }}'
try:
    SCHEDULER_OPTIONS = dict('{{ or (.deis_controller_schedulerOptions) "{}" }}')
except:
    SCHEDULER_OPTIONS = {}

# base64-encoded SSH private key to facilitate current version of "deis run"
SSH_PRIVATE_KEY = """{{ or (.deis_platform_sshPrivateKey) "" }}"""

# platform domain must be provided
DEIS_DOMAIN = '{{ .deis_platform_domain }}'

# use the private registry module
REGISTRY_MODULE = 'registry.private'
REGISTRY_URL = '{{ .deis_registry_protocol }}://{{ .deis_registry_host }}:{{ .deis_registry_port }}'  # noqa
REGISTRY_HOST = '{{ .deis_registry_host }}'
REGISTRY_PORT = '{{ .deis_registry_port }}'

# default to sqlite3, but allow postgresql config through envvars
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{ .deis_database_engine }}',
        'NAME': '{{ .deis_database_name }}',
        'USER': '{{ .deis_database_user }}',
        'PASSWORD': '{{ .deis_database_password }}',
        'HOST': '{{ .deis_database_host }}',
        'PORT': '{{ .deis_database_port }}',
    }
}

# move log directory out of /app/deis
DEIS_LOG_DIR = '/data/logs'

{{ if .deis_controller_registrationEnabled }}
REGISTRATION_ENABLED = bool({{ .deis_controller_registrationEnabled }})
{{ end }}

{{ if .deis_controller_webEnabled }}
WEB_ENABLED = bool({{ .deis_controller_webEnabled }})
{{ end }}

UNIT_HOSTNAME = '{{ or (.deis_controller_unitHostname) "default" }}'

# AUTH
# LDAP
LDAP_ENDPOINT = '{{ .deis_controller_auth_ldap_endpoint }}'
BIND_DN = '{{ .deis_controller_auth_ldap_bind_dn }}'
BIND_PASSWORD = '{{ .deis_controller_auth_ldap_bind_password }}'
USER_BASEDN = '{{ .deis_controller_auth_ldap_user_basedn }}'
USER_FILTER = '{{ .deis_controller_auth_ldap_user_filter }}'
GROUP_BASEDN = '{{ .deis_controller_auth_ldap_group_basedn }}'
GROUP_FILTER = '{{ .deis_controller_auth_ldap_group_filter }}'
GROUP_TYPE = '{{ .deis_controller_auth_ldap_group_type }}'
