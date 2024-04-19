#!/usr/bin/node

const request = require('request');

const url = "https://swapi-api.hbtn.io/api/films/";
const movieId = process.argv[2];

request(url + movieId, function (err, res, body) {
    if (err) {
        console.error('Error:', err);
        return;
    }

    if (res.statusCode !== 200) {
        console.error('Status:', res.statusCode);
        return;
    }

    const actors = JSON.parse(body).characters;
    exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
    if (x === actors.length) return;

    request(actirs[x], function (err, res, body) {
        if (err) {
            console.error('Error:', err);
            return;
        }

        if (res.statusCode !== 200) {
            console.error('Status:', res.statusCode);
            return;
        }

        console.log(JSON.parse(body).name);
        exactOrder(actors, x + 1);
    });
};

