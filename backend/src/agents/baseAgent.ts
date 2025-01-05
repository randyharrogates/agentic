/** @format */

import { Configuration, OpenAIApi } from "openai";

interface AgentConfig {
	name: string;
	description: string;
}

export class BaseAgent {
	private openai: OpenAIApi;
	public name: string;
	public description: string;

	constructor(config: AgentConfig) {
		this.name = config.name;
		this.description = config.description;

		// Initialize OpenAI API
		const configuration = new Configuration({
			apiKey: process.env.OPENAI_API_KEY,
		});
		this.openai = new OpenAIApi(configuration);
	}

	/**
	 * Method to handle queries for this agent
	 * @param input - The input string to process
	 * @returns - The output from OpenAI
	 */
	async handleQuery(input: string): Promise<string> {
		try {
			const response = await this.openai.createChatCompletion({
				model: "gpt-4",
				messages: [
					{ role: "system", content: `Agent: ${this.name}. ${this.description}` },
					{ role: "user", content: input },
				],
				max_tokens: 1000,
				temperature: 0.7,
			});

			return response.data.choices[0].message?.content || "No response generated.";
		} catch (error) {
			console.error(`[${this.name} Error]:`, error);
			throw new Error("Failed to process the query.");
		}
	}
}
