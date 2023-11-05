//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");

export const isPangram = (sentence) => {
    if (sentence) {
        return alphabet.every((letter) =>
            sentence.toLowerCase().includes(letter)
        );
    }
    return false;
};

console.log(isPangram("a"));
