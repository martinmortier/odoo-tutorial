/** @odoo-module **/
import {Component, useState, xml } from "@odoo/owl";
export class Todo extends Component {
    // static defaultProps = {
    //         id: 1,
    //         description: 'Milk',
    //         done: true
    // }

    static props = {
        id: Number,
        description: String,
        done: Boolean
    }

    static template = xml`
    <div>
        <div t-att-class="{'text-muted text-decoration-line-through': props.done }">
            <span t-esc="props.id"/> . <span t-esc="props.description" />
        </div>
    </div>
    `
}