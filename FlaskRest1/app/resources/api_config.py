import importlib
from app.resources.api import api


class ApiConfig:
    def __init__(self, rest_app, bp_config: dict, api_prefix: str = ''):
        """
        Инициализация ApiConfig.

        :param rest_app: Flask приложение
        :param bp_config: Словарь конфигураций ресурсов {url: class_path}
        :param api_prefix: Префикс для API (например, '/api/v1')
        """
        self._rest_app = rest_app
        self._bp_config = bp_config
        self._api_prefix = api_prefix
        self._init_resources()

    def _init_resources(self):
        """Инициализирует ресурсы и добавляет их в API."""
        for url, class_path in self._bp_config.items():
            full_url = f"{self._api_prefix}{url}"
            resource_class = self._get_class(class_path)
            if resource_class:
                # Используем class_path как endpoint для уникальности
                api.add_resource(resource_class, full_url, endpoint=class_path)
            else:
                print(f"Не удалось импортировать класс: {class_path}")

    @staticmethod
    def _get_class(class_path: str):
        """Динамически импортирует класс по заданному пути.

        :param class_path: Полный путь к классу (например, 'app.api.v1.users.ApiUsers')
        :return: Класс или None, если импорт не удался
        """
        try:
            module_path, class_name = class_path.rsplit('.', 1)
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            print(f"Ошибка при импорте {class_path}: {e}")
            return None
