/** @odoo-module **/

import { Component } from "@odoo/owl";
import {Counter} from './counter'
import {Todo} from './todo'

export class Playground extends Component {
    static template = "owl_playground.playground"
    static components = { Counter, Todo }

    setup(){
        this.todos = [{id: 1, description: "Milk", done: true}, {id: 2, description: "Strawberry", done: false}]
    }

}
