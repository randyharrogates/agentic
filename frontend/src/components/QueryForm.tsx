/** @format */

import React, { useState } from "react";
import axios from "axios";

interface Props {
	onNewOutput: (output: string) => void;
}

const QueryForm: React.FC<Props> = ({ onNewOutput }) => {
	const [query, setQuery] = useState("");

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();
		const response = await axios.post("/query", { query });
		onNewOutput(response.data.queryResult || response.data.followUpResult);
	};

	return (
		<form onSubmit={handleSubmit}>
			<input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Enter your query" />
			<button type="submit">Submit</button>
		</form>
	);
};

export default QueryForm;
