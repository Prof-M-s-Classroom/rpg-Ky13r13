import openai
import os

openai.api_key = key
def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """ Please generate me an RPG story, with 13 decisions involved, each with 2 choices. The genre of this story is going to be survival, 
    in a dystopian like future where the life you knew crumbled before you,
     and youre left with some old friends. Id like you to include topics such as adrenaline and pushing
     past your limits, with the human spirit as a significant part. I want users to feel sullen after. Thanks
     
     
     Each line must follow this format:
event_number|description|left_event|right_event

Descriptions should describe the scenario. 
left_event and right_event are the event_numbers of the next choices (or 'None' if it's an ending).

Only output the story in this format. Do not include extra text, titles, or commentary."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename: str, story_text):
    with open(filename, "w") as file:
        file.writelines(story_text)


if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)
