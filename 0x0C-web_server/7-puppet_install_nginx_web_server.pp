#Install Nginx web server (w/ Puppet)

class nginx_setup {
  # Ensure nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Create a default page for nginx
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  # Ensure nginx is listening on port 80
  file_line { 'listen_port':
    path => '/etc/nginx/sites-enabled/default',
    line => '    listen 80 default_server;',
    require => Package['nginx'],
  }

  # Configure a 301 redirect for /redirect_me
  file_line { 'redirect':
    path => '/etc/nginx/sites-enabled/default',
    line => '    rewrite ^/redirect_me https://www.google.com permanent;',
    require => Package['nginx'],
  }

  # Ensure nginx is running and enabled to start on boot
  service { 'nginx':
    ensure => running,
    enable => true,
    require => [Package['nginx'], File['/var/www/html/index.html'], File_line['listen_port'], File_line['redirect']],
  }
}
