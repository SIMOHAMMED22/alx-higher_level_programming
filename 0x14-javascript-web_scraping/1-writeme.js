#!/usr/bin/node
import { writeFile } from 'fs';

const filePath = process.argv[2];
const content = process.argv[3];

writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
