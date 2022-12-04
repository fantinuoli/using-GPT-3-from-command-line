import os
import openai
from rich import print
from rich.prompt import Prompt

openai.api_key = "your key" 
# or use env variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

def callOpenAI():
  while True:
    gpt_prompt = Prompt.ask("\n\n[bold magenta]User[/bold magenta] says")
    
    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=gpt_prompt,
      temperature=0.5,
      max_tokens=256,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    answer = response['choices'][0]['text']
    answer = answer.strip('\n') 

    print("\n[bold green]GPT-3[/bold green] says: " + answer)

callOpenAI()
