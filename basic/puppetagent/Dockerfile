FROM centos:7

RUN rpm -Uvh https://yum.puppetlabs.com/puppet/puppet-release-el-7.noarch.rpm  && \
      yum -y install yum-utils iproute puppet-agent vim wget && \
      yum-config-manager --enable centosplus >& /dev/null && \
      yum clean all && \
      ln -s /opt/puppetlabs/bin/puppet /usr/bin/puppet && \
      echo server = puppet.demo.com >> /etc/puppetlabs/puppet/puppet.conf

ENTRYPOINT /bin/bash
