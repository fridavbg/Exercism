/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timer) {
    let str = "Not done, please wait.";
    if (timer === 0) {
        str = "Lasagna is done.";
    } else if (!timer) {
        str = "You forgot to set the timer.";
    }
    return str;
}

export function preparationTime(layers, time = 2) {
    return layers.length * time;
}

export function quantities(layers) {
    let noodleSauce = {
        noodles: 0,
        sauce: 0,
    };
    let noodleCount = 0;
    let sauceCount = 0;
    for (let i = 0; i < layers.length; i++) {
        const ingredient = layers[i];
        if (ingredient === "noodles") {
            noodleCount++;
        } else if (ingredient === "sauce") {
            sauceCount++;
        }
    }

    if (noodleCount > 0) {
        noodleSauce.noodles = noodleCount * 50;
    }
    if (sauceCount > 0) {
        noodleSauce.sauce = sauceCount * 0.2;
    }

    return noodleSauce;
}

export function addSecretIngredient(friendsList, myList) {
    const secretIngredient = friendsList[friendsList.length - 1];
    myList.push(secretIngredient);
}

export function scaleRecipe(recipe, portions) {
    let modRecipe = {};
    for (const ingredient in recipe) {
        if (Object.hasOwnProperty.call(recipe, ingredient)) {
            const value = recipe[ingredient];
            modRecipe[ingredient] = (value / 2) * portions;
        }
    }
    return modRecipe;
}
