/** @format */

import { BaseAgent } from "./BaseAgent";

export class FollowUpAgent extends BaseAgent {
	constructor() {
		super({
			name: "FollowUpAgent",
			description: "Handles follow-up logic for ongoing workflows.",
		});
	}

	async handleFollowUp(data: any): Promise<string> {
		console.log(`[${this.name}] Processing follow-up for data:`, data);
		return `Follow-up result for: ${data}`;
	}
}
