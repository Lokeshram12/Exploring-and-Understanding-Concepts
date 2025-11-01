import { google } from '@ai-sdk/google';
import { generateText } from 'ai';
import 'dotenv/config';
const apiKey = process.env.GOOGLE_GENERATIVE_AI_API_KEY;
if (!apiKey) {
  throw new Error('Missing GOOGLE_GENERATIVE_AI_API_KEY. Set it in the environment before running.');
}

const model = google('gemini-2.5-flash', { apiKey });

const { text} = await generateText({
  model: model,
  prompt: 'What is the sum of the first 10 prime numbers?'
});


console.log(text);
