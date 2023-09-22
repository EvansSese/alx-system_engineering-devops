# Execute a command

exec { 'kill':
  command     => 'pkill killmenow',
  refreshonly => true,
  provider   => shell,
}
