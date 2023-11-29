//
// This is only a SKELETON file for the 'BookStore' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const discounts = {
    1: 0,
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25,
};

const bookPrice = 800;

const getBookCopies = (basket) => {
    return basket.reduce((acc, book) => {
        acc[book] = (acc[book] || 0) + 1;
        return acc;
    }, {});
};

export const cost = (books) => {
    const bookCopies = getBookCopies(books);
    let totalPrice = 0;
    let bookGroups = [];

    while (Object.keys(bookCopies).some((book) => bookCopies[book] > 0)) {
        let group = [];
        for (const book in bookCopies) {
            if (bookCopies[book] > 0 && group.length < 5) {
                group.push(book);
                bookCopies[book]--;
            }
        }
        bookGroups.push(group.length);
    }

    let indexOfFive = bookGroups.indexOf(5);
    let indexOfThree = bookGroups.indexOf(3);
    while (indexOfFive !== -1 && indexOfThree !== -1) {
        bookGroups[indexOfFive] = 4;
        bookGroups[indexOfThree] = 4;
        indexOfFive = bookGroups.indexOf(5);
        indexOfThree = bookGroups.indexOf(3);
    }

    totalPrice = bookGroups.reduce((acc, groupSize) => {
        groupSize = Number(groupSize);
        return acc + bookPrice * groupSize * (1 - discounts[groupSize]);
    }, 0);

    return totalPrice;
};

// Test cases
console.log(cost([])); // Should return 0
console.log(cost([2, 2])); // Should return 1600
console.log(cost([1, 2])); // Should return 1520
console.log(cost([1, 2, 3])); // Should return 2160
console.log(cost([1, 2, 3, 4])); // Should return 2560
console.log(cost([1, 2, 3, 4, 5])); // Should return 3000
console.log(cost([1, 1, 2, 2, 3, 3, 4, 5])); // Should return 5120
