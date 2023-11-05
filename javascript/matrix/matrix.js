//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
    constructor(str) {
        this._rows = str.split("\n").map((row) => row.split(" ").map(Number));
        this._columns = [];

        for (const row in this._rows) {
            for (let idx in this._rows[row]) {
                this._columns[idx] = this._columns[idx] || [];
                this._columns[idx][row] = this._rows[row][idx];
            }
        }
    }

    get rows() {
        return this._rows;
    }

    get columns() {
        return this._columns;
    }
}
