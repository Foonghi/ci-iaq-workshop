def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed

def test_docker_service_is_running(host):
    dockerd = host.service("docker")
    assert dockerd.is_enabled
    assert dockerd.is_running

def test_heroapp_container_is_running(host):
    heroapp = host.docker("my-hero-app")
    assert heroapp.is_running

def test_heroapp_is_available_on_port_80(host):
    heroapp = host.socket("tcp://0.0.0.0:80")
    assert heroapp.is_listening