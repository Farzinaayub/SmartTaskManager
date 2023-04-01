import openai
import transcribe
import api_key


openai.api_key = api_key.api
input_text=transcribe.from_mic()
def ner(input_text):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Extract the entities from the text with labels Action,Task,Time,Relative time,Date,Relative Date,Stakeholders,Location\ntext: Remind me to buy some chocolates for saya and diya from Lulu Mall.\n\nAction:Set Reminder\nTask: Buy Chocolates\nTime: Not specified\nRelative time: not specified\nDate: not specified\nRelative Date: Today\nStakeholders: me,saya,diya\nLocation: Lulu Mall\n##\ntext: assign the frontend module to rajesh's team. They can start working from tomorrow\n\nAction: Delegation\nTask: Assign Frontend Module\nTime: Not specified\nRelative time: Tomorrow\nDate: Not specified\nRelative Date: Tomorrow\nStakeholders: Rajesh's Team\nLocation: Office\n##\ntext:{input_text}\n",
    temperature=0.02,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
  return response['choices'][0]['text']
print(ner(input_text))
