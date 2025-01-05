/** @format */

import React, { useState } from "react";
import QueryForm from "./components/QueryForm";
import OutputStream from "./components/OutputStream";

const App: React.FC = () => {
	const [outputs, setOutputs] = useState<string[]>([]);

	const handleNewOutput = (output: string) => {
		setOutputs((prev) => [...prev, output]);
	};

	return (
		<div>
			<h1>Multi-Agent RAG System</h1>
			<QueryForm onNewOutput={handleNewOutput} />
			<OutputStream outputs={outputs} />
		</div>
	);
};

export default App;
