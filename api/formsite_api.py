from api.common import send_request
from config.config_parser import config_api


def get_result(**kwargs):
    parameters = {
        "fs_api_key": "Qm8nO3h6auh7",
        "fs_limit": kwargs.get("fs_limit", 1),
        "fs_min_date": kwargs.get("fs_min_date"),
        "fs_max_date": kwargs.get("fs_max_date"),
        "fs_min_id": kwargs.get("fs_min_id"),
        "fs_max_id": kwargs.get("fs_max_id"),
        "fs_page": kwargs.get("fs_page"),
        "fs_sort": kwargs.get("fs_sort"),
        "fs_sort_direction": kwargs.get("fs_sort_direction"),
        "fs_search_equals_x": kwargs.get("fs_search_equals_x"),
        "fs_search_contains_x": kwargs.get("fs_search_contains_x"),
        "fs_search_begins_x": kwargs.get("fs_search_begins_x"),
        "fs_search_ends_x": kwargs.get("fs_search_ends_x"),
        "fs_search_empty_x": kwargs.get("fs_search_empty_x"),
        "fs_search_not_empty_x": kwargs.get("fs_search_not_empty_x"),
        "fs_search_method": kwargs.get("fs_search_method"),
        "fs_view": kwargs.get("fs_view"),
        "fs_include_headings": kwargs.get("fs_include_headings"),
        "fs_custom_labels": kwargs.get("fs_custom_labels")
    }

    endpoint = config_api.get('DEFAULT', 'get_result_endpoint')

    return send_request(endpoint, parameters)


def get_results_count(**kwargs):
    parameters = {
        "fs_api_key": "Qm8nO3h6auh7",
        "fs_min_date": kwargs.get("fs_min_date"),
        "fs_max_date": kwargs.get("fs_max_date"),
        "fs_min_id": kwargs.get("fs_min_id"),
        "fs_max_id": kwargs.get("fs_max_id")
    }

    endpoint = config_api.get('DEFAULT', 'get_results_count_endpoint')

    return send_request(endpoint, parameters)['fs_response']['count']['$']
