import { useState } from 'react';
import { getAnswer } from '../api/assistantAPI';

export default function useAssistant() {
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchAnswer = async (question, context) => {
    setLoading(true);
    const result = await getAnswer(question, context);
    setAnswer(result);
    setLoading(false);
  };

  return { answer, loading, fetchAnswer };
}
