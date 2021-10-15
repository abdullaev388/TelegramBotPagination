from .pagination_handler import register_pagination_handler
from .start_handler import register_start_handler


def register_handlers(dp):
    register_start_handler(dp)
    register_pagination_handler(dp)
