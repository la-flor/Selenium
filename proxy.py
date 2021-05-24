import logging
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

def get_proxy():
    req_proxy = RequestProxy(log_level=logging.ERROR)
    proxy_list = list(req_proxy.get_proxy_list())
    local_proxy = [f'{p.ip}:{p.port}' for p in proxy_list if p.country == "United States"]
    return local_proxy