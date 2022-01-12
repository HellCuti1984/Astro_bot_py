from .start_handler import register_start_handler
from .help_handler import register_help_handler
from .menu_handlers import register_menu_handler
from .pagination_handler import register_pagination_handler
from .cities_handler import register_cities_handler
from .ports_handler import register_ports_handler
from .priority_cities_handler import register_pr_cities_handler
from .market_handler import register_market_handler


def register_handlers(dp):
    register_start_handler(dp)
    register_help_handler(dp)
    register_menu_handler(dp)
    register_pagination_handler(dp)
    register_cities_handler(dp)
    register_ports_handler(dp)
    register_pr_cities_handler(dp)
    register_market_handler(dp)
