from loadbalancer import loadbalancer, load_configuration

import requests
import pytest

@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client

@pytest.fixture
def config():
    return load_configuration('loadbalancer.yaml')

@pytest.mark.parametrize('execution_number', range(30))
def test_direct_mango(config, execution_number):
    for host in config["hosts"]:
        if host["host"] == "www.mango.com":
            # for server in host["servers"]:
            server = host["servers"][0]
            response = requests.get("http://{}".format(server))
            print("Direct {} took {}s".format(server, response.elapsed.total_seconds())) # For the time elapsed

# @pytest.mark.parametrize('execution_number', range(10))
# def test_direct_apple(config, execution_number):
#     for host in config["hosts"]:
#         if host["host"] == "www.apple.com":
#             for server in host["servers"]:
#                 response = requests.get("http://{}".format(server))
#                 print("Direct {} took {}s".format(server, response.elapsed.total_seconds())) # For the time elapsed

# @pytest.mark.parametrize('execution_number', range(5))
# def test_host_routing_mango(client, execution_number):
#     result = client.get('/', headers={"Host":"www.mango.com"})
#     assert b'This is the mango application.' in result.data

# @pytest.mark.parametrize('execution_number', range(5))
# def test_host_routing_apple(client, execution_number):
#     result = client.get('/', headers={"Host":"www.apple.com"})
#     assert b'This is the apple application.' in result.data

# def test_host_routing_notfound(client):
#     result = client.get('/', headers={"Host":"www.notmango.com"})
#     assert b'Not Found' in result.data
#     assert 404 == result.status_code

# @pytest.mark.parametrize('execution_number', range(5))
# def test_path_routing_mango(client, execution_number):
#     result = client.get('/mango')
#     assert b'This is the mango application.' in result.data

# @pytest.mark.parametrize('execution_number', range(5))
# def test_path_routing_apple(client, execution_number):
#     result = client.get('/apple')
#     assert b'This is the apple application.' in result.data

# def test_path_routing_notfound(client):
#     result = client.get('/notmango')
#     assert b'Not Found' in result.data
#     assert 404 == result.status_code