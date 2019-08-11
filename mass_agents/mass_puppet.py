#!/usr/bin/python3
import subprocess

import time

number_agents = 21


def run_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return output


# Generate the code for the puppet agents
def create_agents():
    agents = ''
    for i in range(2, number_agents):
        agents += (f"""
  puppetagent-{i}:
    build:
      context: ./puppetagent
      dockerfile: Dockerfile
    container_name: massagents-puppetagent-{i}
    hostname: agent{i}.demo.com
    stdin_open: true
    tty: true
    networks:
      massagents-puppet-net:
        ipv4_address: 172.30.0.{i}
    extra_hosts:
      - 'puppet.demo.com:172.30.0.254'
""")

    with open("docker-compose.yml", "a") as compose_file:
        compose_file.write(agents)


# Generate the code for the network
def create_network():
    network = (f"""
networks:
  massagents-puppet-net:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.30.0.0/24
""")
    with open("docker-compose.yml", "a") as compose_file:
        compose_file.write(network)


def build_compose():
    run_cmd("docker-compose build")


def run_compose():
    run_cmd("docker-compose up -d")


def create_secret():
    run_cmd(
        f"docker exec -it massagents-puppetmaster /bin/bash -c 'eyaml encrypt -l 'mysql::root_password' -s 'V3ryS3cr3T!' |grep ENC | head -1 > /root/mysql_pw.yaml'")


def enroll_agents():
    time.sleep(40)
    for i in range(2, number_agents):
        print(f"Enrolling massagents-puppetagent-{i}")
        run_cmd(f"docker exec -it massagents-puppetagent-{i} /bin/bash -c 'puppet agent -t --waitforcert=120'")


def create_pwn_script():
    for i in range(2, number_agents):
        with open("pwn.sh", "a") as pwn_file:
            pwn_file.write(f"docker exec -it massagents-puppetagent-{i} /bin/bash -c 'puppet agent -t --waitforcert=120'\n")


def main():
    print(f"Creating {number_agents - 2} puppet agents")
    create_agents()
    create_network()
    build_compose()
    run_compose()
    create_secret()
    enroll_agents()
    create_pwn_script()


if __name__ == '__main__':
    main()
