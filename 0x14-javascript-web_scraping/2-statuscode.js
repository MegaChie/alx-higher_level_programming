#!/usr/bin/node
fetch(process.argv[2]).then((response)=>{
  console.log(response.status);
};
