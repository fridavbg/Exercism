//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
];

export const decodedValue = (colors) => {
    const color1 = COLORS.indexOf(colors[0]);
    const color2 = COLORS.indexOf(colors[1]);
    const result = String(color1) + String(color2);
    return parseInt(result);
};

console.log(decodedValue(["brown", "black"]));
