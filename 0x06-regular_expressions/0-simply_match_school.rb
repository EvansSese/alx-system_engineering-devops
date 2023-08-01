#!/usr/bin/env ruby
def match_school(input)
  pattern = /School/
  matches = input.scan(pattern)
  puts matches.join
end
# Get the input argument from the command line
if ARGV.length != 1
  puts 'Usage: ruby script_name.rb <input>'
  exit 1
end
input_argument = ARGV[0]
match_school(input_argument)
