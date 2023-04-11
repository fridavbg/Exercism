// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
    return birdsPerDay.reduce(function (acc, val) {
        return acc + val;
    }, 0);
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
    const daysPerWeek = 7;
    const startIndex = (week - 1) * daysPerWeek;
    const endIndex = startIndex + daysPerWeek;
    let birdCount = 0;
    for (let i = startIndex; i < endIndex; i++) {
        birdCount += birdsPerDay[i];
    }
    return birdCount;
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {number[]} corrected bird count data
 */
export function fixBirdCountLog(birdsPerDay) {
    for (let i = 0; i < birdsPerDay.length; i += 2) {
        birdsPerDay[i] += 1;
    }
    return birdsPerDay;
}
