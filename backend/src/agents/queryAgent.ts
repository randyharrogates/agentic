/** @format */

import { BaseAgent } from "./BaseAgent";

export class QueryAgent extends BaseAgent {
	constructor() {
		super({
			name: "QueryAgent",
			description: "Handles user queries and retrieves relevant responses.",
		});
	}

	/**
	 * Override or extend base behavior if necessary
	 * @param query - User query
	 * @returns - Query result
	 */
	async handleQuery(query: string): Promise<string> {
		console.log(`[${this.name}] Processing query:`, query);
		return super.handleQuery(query);
	}
}
