/** @odoo-module **/

import { registry } from "@web/core/registry";
import {Layout} from '@web/search/layout';
import { getDefaultConfig } from "@web/views/view";

const { Component, useSubEnv, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks";
import { Domain } from '@web/core/domain';


class AwesomeDashboard extends Component {

    setup(){
        useSubEnv({
            config: {
                ...getDefaultConfig(),
                ...this.env.config,
            },
        });
        this.display = {
            controlPanel: { "top-right": false, "bottom-right": false }
        }

        this.action = useService('action')

        this.rpc = useService("rpc")
        onWillStart(async () => {
            const result = await this.rpc('/awesome_tshirt/statistics')
            console.log('result')
        })
    }

    openCustomers(){
        this.action.doAction("base.action_partner_form")
    }

    newOrders(){
    }
    cancelOrders(){
        const domain =
            "[('create_date','>=', (context_today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')), ('state', '=', 'cancelled')]";
        this.action.doAction({
            type: 'ir.actions.act_window',
            name: 'Last 7 days orders',
            res_model: "awesome_tshirt.order",
            domain: new Domain(domain).toList(),
            views: [
                [false, 'list'],
                [false, 'form']
            ]
        })
    }
}

AwesomeDashboard.components = { Layout };
AwesomeDashboard.template = "awesome_tshirt.clientaction";


registry.category("actions").add("awesome_tshirt.dashboard", AwesomeDashboard);
