//
// This is only a SKELETON file for the 'BookStore' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const discounts = {
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25,
    set: 0.1,
};

const bookPrice = 800;

const calculateDiscountPrice = (bookCopies) => {
    console.log("==== ", bookCopies);

    return;
};

const getBookCopies = (basket) => {
    const bookCounts = basket.reduce((acc, book) => {
        acc[book] = (acc[book] || 0) + 1;
        return acc;
    }, {});

    return bookCounts;
};

export const cost = (books) => {
    const bookCopies = getBookCopies(books);

    const discountPrice = calculateDiscountPrice(bookCopies);

    return discountPrice;
};

console.log(cost([]));
console.log(cost([2, 2]));
console.log(cost([1, 2]));
console.log(cost([1, 2, 3]));
console.log(cost([1, 2, 3, 4]));
console.log(cost([1, 2, 3, 4, 5]));
console.log(cost([1, 1, 2, 2, 3, 3, 4, 5]));
