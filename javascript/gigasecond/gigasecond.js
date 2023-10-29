//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const gigaSec = Math.pow(10, 9) * 1000;

export const gigasecond = (date) => {
    return new Date(gigaSec + date.getTime());
};
