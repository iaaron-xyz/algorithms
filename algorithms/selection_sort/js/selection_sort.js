/**
 * Find the smallest number in an array
 * @param {array} arr 
 * @returns {integer}
 */

function findSmallest(arr) {
  // store the smallest element
  let smallest = arr[0];
  // store the index of the smallest element
  let smallestIndex = 0
  for (let i = 1; i < arr.length; i += 1) {
    if (arr[i] < smallest) {
      smallest = arr[i];
      smallestIndex = i;
    }
  }
  return smallestIndex;
}

/**
 * Sort an array using Selection Sort
 * @param {array} arr 
 * @returns {array}
 */

function selectionSort(arr) {
  let sortedArr = [];
  const arrLength = arr.length;
  for (let i = 0; i < arrLength; i += 1) {
    const smallestIndex = findSmallest(arr);
    sortedArr.push(arr[smallestIndex]);
    arr.splice(smallestIndex, 1);
  }
  return sortedArr;
}

// Usage example
console.log(selectionSort([6,2,7,11,4,2]));