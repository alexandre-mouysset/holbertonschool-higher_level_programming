#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));
let result;

if (args.length < 2) {
  result = 0;
} else {
  let first = -Infinity;
  let second = -Infinity;

  for (const n of args) {
    if (n > first) {
      second = first;
      first = n;
    } else if (n > second && n < first) {
      second = n;
    }
  }
  if (second === -Infinity) {
    result = 0;
  } else {
    result = second;
  }
}
console.log(result);
