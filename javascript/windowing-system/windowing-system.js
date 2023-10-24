// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export class Size {
    constructor(width = 80, height = 60) {
        this.width = width;
        this.height = height;
    }

    resize(newWidth, newHeight) {
        this.width = newWidth;
        this.height = newHeight;
    }
}

export class Position {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    move(newX, newY) {
        this.x = newX;
        this.y = newY;
    }
}

export class ProgramWindow {
    constructor() {
        this.screenSize = new Size(800, 600);
        this.size = new Size();
        this.position = new Position();
    }

    resize(newSize) {
        if (newSize.width < 1) {
            newSize.width = 1;
        }

        if (newSize.height < 1) {
            newSize.height = 1;
        }

        let newX = newSize.width;
        let newY = newSize.height;
        if (newX + this.position.x > this.screenSize.width) {
            newX = this.screenSize.width - this.position.x;
        }

        if (newY + this.position.y > this.screenSize.height) {
            newY = this.screenSize.height - this.position.y;
        }
        this.size.resize(newX, newY);
    }

    move(newPosition) {
        let newX = newPosition.x;
        let newY = newPosition.y;

        if (newX < 0) {
            newX = 0;
        }

        if (newY < 0) {
            newY = 0;
        }

        if (newX + this.size.width > this.screenSize.width) {
            newX = this.screenSize.width - this.size.width;
        }

        if (newY + this.size.height > this.screenSize.height) {
            newY = this.screenSize.height - this.size.height;
        }

        this.position.move(newX, newY);
    }
}

export function changeWindow(programWindow) {
    programWindow.resize(new Size(400, 300));
    programWindow.move(new Position(100, 150));
    return programWindow;
}
