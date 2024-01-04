#!/usr/bin/node
const fs = require('fs'); // Import the 'fs' module for file operations
const request = require('request'); // Import the 'request' module for making HTTP requests

const url = process.argv[2]; // Get the URL from the command-line arguments
const filePath = process.argv[3]; // Get the file path from the command-line arguments

// Make an HTTP request to the specified URL and pipe the response to a file
request(url)
  .pipe(fs.createWriteStream(filePath)); // Create a writable stream to the file
