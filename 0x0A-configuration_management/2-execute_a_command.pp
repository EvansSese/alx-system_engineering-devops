# Execute a command

exec { 'kill':
  command     => 'pkill killmenow',
  refreshonly => true,
  subscribe   => Service[bash],
}
