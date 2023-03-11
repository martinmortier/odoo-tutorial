/** @odoo-module **/
import {Component, useState, xml } from "@odoo/owl";
export class Counter extends Component {
    state = useState({value: 0})

    increment(){
        this.state.value++
    }

    static template = xml`
        <div>
            Counter: <span t-esc="state.value"/>
        </div>
        <button t-on-click="increment">Increment</button>
    `
}