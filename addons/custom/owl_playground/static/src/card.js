/** @odoo-module **/
import {Component, xml} from '@odoo/owl'
export class Card extends Component {

    static template = xml`
    <div class="card" style="width: 18rem;">
        <img src="..." class="card-img-top" alt="..." />
        <div class="card-body">
            <h5 class="card-title">
                <t t-if="props.slots.title">
                    <t t-slot="title"/>
                </t>
            </h5>
            <p class="card-text">
                <t t-slot="default"/>
            </p>
        </div>
    </div>
    `
}