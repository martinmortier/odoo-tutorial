/** @odoo-module **/
import {Component, useState, xml } from "@odoo/owl";
export class Todo extends Component {
    static defaultProps = {
        milk: {
            id: 1,
            description: 'Milk',
            done: true
        }
    }

    static props = {
        milk: {
            id: Number,
            description: String,
            done: Boolean
        }
    }

    static template = xml`
    <div>
        <div t-att-class="{'text-muted text-decoration-line-through': props.milk.done }">
            <span t-esc="props.milk.id"/> . <span t-esc="props.milk.description" />
        </div>
    </div>
    `
}