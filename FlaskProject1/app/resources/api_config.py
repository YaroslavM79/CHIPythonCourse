from app.resources.rest_api import api


class ApiConfig:
    def __init__(self, bp_config: list, api_prefix=None):
        self._blueprints = bp_config
        self._api_prefix = api_prefix
        self._init_blueprints()

    def _init_blueprints(self):
        """Add blueprints and restful resources"""
        for class_path in self._blueprints:
            extended_path = f"{class_path}.view.api_bp"
            api_bp = self._get_class(extended_path)

            if self._api_prefix is not None:
                new_url_prefix = f"{self._api_prefix}{api_bp.url_prefix}"
                api.register_blueprint(api_bp, url_prefix=new_url_prefix)
            else:
                api.register_blueprint(api_bp)

    @staticmethod
    def _get_class(class_path: str):
        """Get class by its path"""
        components = class_path.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
