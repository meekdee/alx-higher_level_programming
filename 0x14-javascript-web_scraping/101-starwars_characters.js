#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      try {
        const characterResponse = await fetchCharacter(character);
        console.log(characterResponse.name);
      } catch (error) {
        console.log(error);
      }
    }
  }
});

function fetchCharacter (characterURL) {
  return new Promise((resolve, reject) => {
    request.get(characterURL, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character);
      }
    });
  });
}
