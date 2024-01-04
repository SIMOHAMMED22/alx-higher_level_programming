#!/usr/bin/node
const request = require('request');

// Function to check if a character URL ends with '/18/'
const isWedgeAntilles = (characterURL) => characterURL.endsWith('/18/');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;

    // Use reduce to count movies where Wedge Antilles is present
    const count = films.reduce((totalCount, movie) => {
      // Use some to check if any character URL matches Wedge Antilles
      if (movie.characters.some(isWedgeAntilles)) {
        return totalCount + 1;
      }
      return totalCount;
    }, 0);

    console.log(count);
  }
});
