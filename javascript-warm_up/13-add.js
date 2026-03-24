#!/usr/bin/node
function add (a, b) {
	if (isNaN(a) || isNaN(b)) {
		return 'Not a number';
	}  else {
		return a + b;
	}
}
module.exports = add;
