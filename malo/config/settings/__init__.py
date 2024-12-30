# settings/__init__.py
import os

# Carrega o módulo de configurações com base na variável de ambiente
settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'config.settings.local')

if not settings_module:
    raise ValueError("A variável de ambiente DJANGO_SETTINGS_MODULE não está definida!")

# Importa as configurações definidas
module = __import__(settings_module, globals(), locals(), ['*'])
for setting in dir(module):
    if setting.isupper():
        locals()[setting] = getattr(module, setting)
