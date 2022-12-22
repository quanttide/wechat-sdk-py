# -*- coding: utf-8 -*-


from dynaconf import Dynaconf


settings = Dynaconf(
    settings_files=['settings.toml'],
    environments=True,
    load_dotenv=True,
    env_prefix='WXCLOUDRUN',
)
