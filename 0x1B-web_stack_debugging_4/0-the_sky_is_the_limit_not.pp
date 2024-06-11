# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  # Replace the value 15 with 4096 in the /etc/default/nginx file
  command => 'sed -i "s/15/4096/" /etc/default/nginx',  
  path    => '/usr/local/bin/:/bin/'
}

# Restart the Nginx service
-> exec { 'nginx-restart':
  command => 'nginx restart',  
  path    => '/etc/init.d/'
}
