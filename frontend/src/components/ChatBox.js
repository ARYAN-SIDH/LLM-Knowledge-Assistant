import React, { useState } from 'react';

export default function ChatBox({ onSubmit }) {
  const [question, setQuestion] = useState('');
  const [context, setContext] = useState('');

  const handleSubmit = () => {
    onSubmit(question, context);
  };

  return (
    <div>
      <textarea
        rows=\"5\"
        placeholder=\"Enter context\"
        value={context}
        onChange={e => setContext(e.target.value)}
      />
      <input
        placeholder=\"Ask a question\"
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={handleSubmit}>Ask</button>
    </div>
  );
}
