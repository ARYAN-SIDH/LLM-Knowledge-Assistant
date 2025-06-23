import React from 'react';
import ChatBox from '../components/ChatBox';
import AnswerCard from '../components/AnswerCard';
import useAssistant from '../hooks/useAssistant';

export default function HomePage() {
  const { answer, loading, fetchAnswer } = useAssistant();

  return (
    <div>
      <h1>AI Knowledge Assistant</h1>
      <ChatBox onSubmit={fetchAnswer} />
      {loading ? <p>Loading...</p> : <AnswerCard answer={answer} />}
    </div>
  );
}
