/** @odoo-module */

import { registry } from "@web/core/registry";

export const getPartners = {
    dependencies: ["rpc","orm"],
    async start(env, { rpc,orm }) {
        const data = await orm.searchRead(
            "res.partner", 
            [], 
            ["image_128","name", "website", "phone"]
        )
        return { data };
    },
};

registry.category("services").add("owl.getPartners", getPartners);