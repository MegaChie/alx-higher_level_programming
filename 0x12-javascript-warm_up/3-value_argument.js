#!/usr/bin/node
// comment text
if (process.argv.length === 2) {
  console.log('No argument')
} else {
  for (let i = 2; i < process.argv.length; i++) {
    console.log(process.argv[i])
  }
}
