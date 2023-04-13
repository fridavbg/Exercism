// @ts-check

import { log } from "console";
import { isNumber } from "util";

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
    let string1 = array1.toString();
    let string2 = array2.toString();
    let sum1 = string1.replace(/,/g, "");
    let sum2 = string2.replace(/,/g, "");
    return Number(sum1) + Number(sum2);
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
    let str = String(value);
    return str === str.split("").reverse().join("");
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
    let errMsg = "";
    if (!input) {
        errMsg = "Required field";
    } else if (isNaN(Number(input)) || input === "0") {
        errMsg = "Must be a number besides 0";
    }
    return errMsg;
}

console.log(errorMessage("123"));
// => ''

console.log(errorMessage(""));
// => 'Required field'

console.log(errorMessage("abc"));

// => 'Must be a number besides 0'
