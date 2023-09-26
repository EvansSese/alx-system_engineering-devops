# Install and configure Nginx on ubuntu server using puppet

#update the system
exec { 'update-system':
  command => '/usr/bin/apt-get update',
}

#install nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update-system'],
}

#update index
file { ''/var/www/html/index.html':
  content => 'Hello World!',
}

# Redirect
exec { 'redirect-me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# start nginx
service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
