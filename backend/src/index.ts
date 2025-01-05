/** @format */

import express, { Request, Response } from "express";
import mongoose from "mongoose";
import dotenv from "dotenv";
import { QueryAgent } from "./agents/QueryAgent";
import { EvaluationAgent } from "./agents/EvaluationAgent";
import { FollowUpAgent } from "./agents/FollowUpAgent";

dotenv.config();

const app = express();
app.use(express.json());

// MongoDB Connection
mongoose
	.connect(process.env.MONGO_URI as string, { useNewUrlParser: true, useUnifiedTopology: true })
	.then(() => console.log("MongoDB connected"))
	.catch((err) => console.error("MongoDB connection error:", err));

// Initialize agents
const queryAgent = new QueryAgent();
const evaluationAgent = new EvaluationAgent();
const followUpAgent = new FollowUpAgent();

// Route for querying the RAG system
app.post("/query", async (req: Request, res: Response) => {
	const { query } = req.body;

	try {
		const queryResult = await queryAgent.handleQuery(query);
		const evaluationResult = await evaluationAgent.evaluate(queryResult);

		if (evaluationResult.nextAgent === "FollowUpAgent") {
			const followUpResult = await followUpAgent.handleFollowUp(evaluationResult.data);
			return res.json({ followUpResult });
		}

		res.json({ queryResult });
	} catch (err) {
		console.error(err);
		res.status(500).send("An error occurred.");
	}
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
