var crypto = require("crypto");
var hash = crypto.createHash("sha256");

var timestamp = Date.now();
var message = "Random Message";
var nonce = 0;
guess = 99999999999999999999;
payload = timestamp + message;
throttle = 1000000;
target = Math.pow(2, 64) / throttle;

var start = Date.now();
while (guess > target) {
    hash = crypto.createHash("sha256");
    nonce+=1;
    guess = parseInt(hash.update(payload + nonce).digest('hex').substring(0,16), 16);
}
var end = Date.now()
console.log("Run time: ", (end-start)/1000);