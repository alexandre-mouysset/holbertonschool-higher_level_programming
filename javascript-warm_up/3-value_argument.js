#!/usr/bin/node

const first_arg = Process.argv.slice(2);

if ([first_arg]) {
  console.log(first_arg);
} else {
  console.log('No argument');
}