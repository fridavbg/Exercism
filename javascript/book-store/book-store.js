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

function calculateGroupDiscount(group) {
    const uniqueBooks = group.length;
    const discount = discounts[uniqueBooks] || 0;
    return uniqueBooks * bookPrice * (1 - discount);
}

export const cost = (books) => {
    const bookCopies = getBookCopies(books);
    let uniqueBookCounts = Object.values(bookCopies);
    let discountGroups = Object.keys(discounts);

    // Initialize min Cost to Infinity
    let prices = new Array(books.length + 1).fill(Infinity);
    // Base case : 0 books 0 cost
    prices[0] = 0;

    function findPricesForBooks(
        booksToBeGrouped,
        calculatedPrice,
        booksChecked
    ) {
        if (prices[booksChecked] > calculatedPrice) {
            prices[booksChecked] = calculatedPrice;
        }

        for (let groupSize of discountGroups) {
            groupSize = parseInt(groupSize);

            let discountBookGroup = [];
            let bookAmounts = [...booksToBeGrouped];

            for (
                let i = 0;
                i < bookAmounts.length && discountBookGroup.length < groupSize;
                i++
            ) {
                if (bookAmounts[i] > 0) {
                    bookAmounts[i]--;
                    discountBookGroup.push(i);
                }
            }

            if (discountBookGroup.length === groupSize) {
                findPricesForBooks(
                    bookAmounts.filter((count) => count > 0),
                    calculatedPrice + calculateGroupDiscount(discountBookGroup),
                    booksChecked + groupSize
                );
            }
        }
    }

    findPricesForBooks(uniqueBookCounts, 0, 0);

    return prices[books.length];
};
git;
