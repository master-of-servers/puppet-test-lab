class webfiles {
  file { '/var/www/html':
    ensure => directory,
    owner => 'root',
    group => 'root',
  }
  file { '/var/www/html/index.html':
    mode => "0644",
    owner => 'root',
    group => 'root',
    source => 'puppet:///modules/webfiles/index.html',
  }
}
