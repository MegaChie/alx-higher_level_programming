#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log('X') * parseInt(process.argv[2]);    
  }
} else {
  console.log('Missing size');
}
