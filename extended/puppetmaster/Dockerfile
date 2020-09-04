FROM puppet/puppetserver

COPY files/site.pp.prod /etc/puppetlabs/code/environments/production/manifests/site.pp
COPY files/Puppetfile /etc/puppetlabs/code/environments/production

RUN apt-get update && \
      apt-get install -y vim \
      tree && \
      cp -r /etc/puppetlabs/code/environments/production/ \
      /etc/puppetlabs/code/environments/development && \
      # Install and configure eyaml
      puppetserver gem install hiera-eyaml --no-document && \
      cd /etc/puppetlabs/puppet/ && \
      eyaml createkeys && \
      mv keys eyaml

# Setup dev environment
COPY files/Puppetfile /etc/puppetlabs/code/environments/development
COPY files/site.pp.dev /etc/puppetlabs/code/environments/development/manifests/site.pp

WORKDIR /etc/puppetlabs/code/environments/development
RUN r10k puppetfile install

WORKDIR /etc/puppetlabs/code/environments/development
COPY files/webfiles modules/webfiles/

# Setup prod environment
WORKDIR /etc/puppetlabs/code/environments/production
RUN r10k puppetfile install

WORKDIR /etc/puppetlabs/code/environments/production
COPY files/webfiles modules/webfiles/
COPY files/config.yaml /etc/eyaml/config.yaml

# Create a secret
RUN /opt/puppetlabs/puppet/bin/eyaml encrypt -l 'mysql::root_password' -s 'V3ryS3cr3T!' | grep ENC | head -1 > /root/mysql_pw.yaml
