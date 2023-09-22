# Execute a command

exec { 'kill':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
