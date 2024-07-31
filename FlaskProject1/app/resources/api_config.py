from app.resources.rest_api import api

__all__ = ['ApiConfig']

FILE_NAME = 'api_config.json'
BLUEPRINT_NAME = 'blueprint_name'
URL_PREFIX = 'url_prefix'
CLASS_PATH = 'class_path'


class ApiConfig:
    def __init__(self, rest_app, bp_config):
        self._blueprints = bp_config
        self._rest_app = rest_app
        self._init_blueprints()

    def _init_blueprints(self):
        """add restful resources"""
        blueprint_urls = self._collect_urls_per_blueprint()

        for class_path, path in blueprint_urls.items():
            fn_class = self._get_class(class_path=class_path)
            api.add_resource(fn_class, *path, endpoint=class_path)

    @staticmethod
    def _get_class(class_path: str):
        """get class by its path"""
        components = class_path.split('.')
        fn_name = __import__('app')
        for comp in components:
            fn_name = getattr(fn_name, comp)
        return fn_name
        # fn_new = "app.{}".format(class_path)
        # fn_class = importlib.import_module(fn_new)
        # return fn_class

    def _collect_urls_per_blueprint(self) -> dict:
        """ set relation between blueprint (class) and correspond urls"""
        blueprint_urls = {}
        for k, v in self._blueprints.items():
            if v in blueprint_urls:
                blueprint_urls[v].append(k)
            else:
                blueprint_urls[v] = [k]
        return blueprint_urls
