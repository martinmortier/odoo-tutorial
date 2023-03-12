/** @odoo-module **/
import {Component, useState, xml } from "@odoo/owl";
export class Todo extends Component {

    static props = {
        id: Number,
        description: String,
        done: Boolean,
        toggleState: Function
    }

    static template = xml`
    <div>
        <div t-att-class="{'text-muted text-decoration-line-through': props.done }">
            <span t-esc="props.id"/> . <span t-esc="props.description" />
            <input type="checkbox" t-model="props.done" t-on-click="(event) => props.toggleState(event,props.id)"/>
        </div>
    </div>
    `
}