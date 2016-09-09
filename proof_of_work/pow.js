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
    hashA = crypto.createHash("sha256");
    hashB = crypto.createHash("sha256");
    nonce+=1;
    guess = parseInt(
              hashB.update(
                hashA.update(payload + nonce).digest('hex'))
              .digest('hex') 
            .substring(0,16), 16);
    // Turn on to debug
    //guess = hash.update(payload + nonce).digest('hex');

    // 16 Hex nibbles
    console.log(guess)
    //console.log(guess.substring(0,16));
    // 16 x 4 bits = 64 bits in decimal
    //console.log(parseInt(guess.substring(0,16), 16));
    //console.log(target)
}
var end = Date.now()
console.log("Run time: ", (end-start)/1000);