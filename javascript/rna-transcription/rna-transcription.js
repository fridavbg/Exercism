//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const DNAToRNA = {
    G: "C",
    C: "G",
    T: "A",
    A: "U",
};

export const toRna = (str) => {
    let result = "";
    if (str) {
        for (const letter of str) {
            result += DNAToRNA[letter];
        }
    }
    return result;
};
