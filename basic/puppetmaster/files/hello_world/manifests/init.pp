class hello_world {
  file { '/tmp/hello.txt':
    ensure => present,
    source => 'puppet:///modules/hello_world/hello.txt',
    owner  => root,
    group  => root,
    mode   => '0755',
  }
}
