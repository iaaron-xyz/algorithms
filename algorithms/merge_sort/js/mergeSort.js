/**
 * Merge 2 ordered arrays into
 * one ordered array
 * 
 * @param {array} L - Left array
 * @param {array} R - Right array
 * @param {array} M - original array
 */
function merge(L, R, A) {
  const sizeL = L.length;
  const sizeR = R.length;
  let i = 0, j = 0, k = 0;
  // place from lower to higher
  while (i < sizeL && j < sizeR) {
    // place the left element if lower else the right element
    if (L[i] <= R[j]) {
      A[k] = L[i];
      i += 1;
    } else {
      A[k] = R[j];
      j += 1;
    }
    k += 1;
  }
  // append the remaining elements
  for (i; i <= sizeL-1; i++) {
    A[k] = L[i];
    k += 1;
  }
  for (j; j <= sizeR-1; j++) {
    A[k] = R[j];
    k += 1;
  }
}


/**
 * Merge Sort: Sort 1 array using the
 * merge sort algorithm
 * 
 * @param {array} A 
 * @returns {int} 0 - returns zero if succesful
 */
function mergeSort(A) {
  const size = A.length
  // Return nothing when the list is of 1 element
  if (size < 2) return
  // Set parameters
  const mid = Math.floor(size/2);
  const left = A.slice(0,mid);
  const right = A.slice(mid);
  // merge and sort
  mergeSort(left);
  mergeSort(right);
  merge(left, right, A);
  return 0;
}


// Test
const A = [4,6,7,2,100,1,5,3,22,47,15,2];
console.log(`Before: ${A}`);
mergeSort(A);
console.log(`After: ${A}`);
