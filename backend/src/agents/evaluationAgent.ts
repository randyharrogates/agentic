/** @format */

import { BaseAgent } from "./BaseAgent";

export class EvaluationAgent extends BaseAgent {
	constructor() {
		super({
			name: "EvaluationAgent",
			description: "Evaluates data and determines the next workflow step.",
		});
	}

	async evaluate(data: any): Promise<{ nextAgent: string | null; data: any }> {
		console.log(`[${this.name}] Evaluating data:`, data);

		// Perform evaluation logic
		const nextAgent = data.includes("follow up") ? "FollowUpAgent" : null;

		return { nextAgent, data };
	}
}
