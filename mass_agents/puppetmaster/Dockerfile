FROM puppet/puppetserver

RUN apt-get update && \
      apt-get install -y vim \
      tree && \
      mkdir -p /etc/puppetlabs/code/environments/production/modules/hello_world/files && \
      mkdir -p /etc/puppetlabs/code/environments/production/modules/hello_world/manifests && \
      mkdir /etc/eyaml && \
      # Install and configure eyaml
      puppetserver gem install hiera-eyaml && \
      cd /etc/puppetlabs/puppet/ && \
      eyaml createkeys && \
      mv keys eyaml 

# Get everything into place for the Puppet Master
COPY files/site.pp /etc/puppetlabs/code/environments/production/manifests
COPY files/hello_world/ /etc/puppetlabs/code/environments/production/modules/hello_world
COPY files/config.yaml /etc/eyaml/config.yaml
