/** @format */

import React from "react";

interface Props {
	outputs: string[];
}

const OutputStream: React.FC<Props> = ({ outputs }) => {
	return (
		<div>
			<h2>Agent Outputs</h2>
			<ul>
				{outputs.map((output, index) => (
					<li key={index}>{output}</li>
				))}
			</ul>
		</div>
	);
};

export default OutputStream;
