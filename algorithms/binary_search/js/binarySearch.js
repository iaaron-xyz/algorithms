/**
 * 
 * @param {array} list 
 * @param {integer} item 
 */

function binary_search(list, item) {
  // initial values
  let low = 0;
  let high = list.length - 1;

  while (low <= high) {
    // set the guess
    mid = Math.floor((low + high)/2);
    const guess = list[mid];
    console.log(`Guess: ${mid}`);
    // found
    if (guess === item) {
      return mid;
    }
    // discard upper half
    if (guess > item) {
      high = mid - 1;
    }
    // discard lower half
    else {
      low = mid + 1;
    }
  }
}

console.log(binary_search([1,3,4,5,7,8,11,234], 234));
console.log(binary_search([1,3,4,5,7,8,11,234], 3));