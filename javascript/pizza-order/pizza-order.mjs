/// <reference path="./global.d.ts" />
//
// @ts-nocheck

/**
 * Determine the prize of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
const pizzaMenu = {
    Margherita: 7,
    Caprese: 9,
    Formaggio: 10,
    ExtraSauce: 1,
    ExtraToppings: 2,
};

export function pizzaPrice(pizza, ...extras) {
    let totalPrice = 0;
    if (pizza in pizzaMenu) {
        totalPrice += pizzaMenu[pizza];
    }
    for (const topping of extras) {
        totalPrice += pizzaMenu[topping];
    }
    return totalPrice;
}

/**
 * Calculate the prize of the total order, given individual orders
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */

export function orderPrice(pizzaOrders) {
    let totalPrice = 0;
    for (const order in pizzaOrders) {
        console.log(order);
    }
    return totalPrice;
}

const margherita = ["Margherita"];
const caprese = ["Caprese", "ExtraToppings"];
orderPrice([margherita, caprese]);
