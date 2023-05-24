import os
import openai

with open('key.txt', 'r') as file:
  first_line = file.readline()
os.environ["OPENAI_API_KEY"] = first_line

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
  model="gpt-4",
  temperature=0,
  messages=[
      {"role": "user", "content": """"
      1)Write a melody in the form of a list of (pitch, duration) pairs in Python syntax, where the pitch uses MIDI pitch standard, and the duration represents the number quarter notes. Use a pitch of None to represent a rest. Ensure the following:
The melody has a contour with several high and low points
-The melody has Chord-based melodies
The melody stays between MIDI pitch 50 and MIDI pitch 100
-The melody is at least 120 notes in length
-Video Game with some Stravinski and Mozart Influence style Soundtrack Scale-based melodies
2) Write a bassline to go with the melody . Make it slower and change to fast tempo, with rhythm and with harmony with the melody. Ensure the following:
-Add Variation to the bass line
-with some Stravinski and Mozart Influencekey
3) add a sub-bass to go with the melody, slow tempo, composed for drums must have:
-Add variation
-Change pitch
-with some Stravinski and Mozart Influence
-Monotone melodies patterns
-Wide range of notes and harmony

                                  """}

  ]
)

print(completion.choices[0].message.content)
print(completion.choices[0].message)


