# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version uses a content-based scoring rule to recommend songs that match a
user's favorite genre, mood, energy level, and acoustic preference. I expanded
the catalog from 10 to 17 songs so it includes more than the starter set of
genres and moods. The recommender scores every song, then ranks the
highest-scoring songs first.

---

## How The System Works

Each `Song` stores its title, artist, genre, mood, energy, tempo, valence,
danceability, and acousticness. I will use genre, mood, energy, and
acousticness for the first version of the score. A `UserProfile` stores a
favorite genre, a favorite mood, a target energy level, and whether the user
likes acoustic music.

My starting profile is:

```python
{
    "favorite_genre": "lofi",
    "favorite_mood": "focused",
    "target_energy": 0.45,
    "likes_acoustic": True,
}
```

The scoring rule evaluates one song at a time:

- Matching genre: +4 points
- Matching mood: +3 points
- Energy closeness: up to +3 points, with closer energy values earning more
- Matching acoustic preference: +1 point

Genre receives the most weight because it is the clearest starting signal for
this profile. Mood and energy then help separate a focused lofi song from an
intense rock song. The ranking rule sorts every scored song from highest to
lowest score and returns the top results.

```text
User preferences
      ↓
Score each song in songs.csv
      ↓
Sort scores from highest to lowest
      ↓
Return the top k recommendations with reasons
```

This is a small simulation, not a full Spotify-style system. A larger system
could also use behavior such as listens, skips, saves, and playlists. My rule
may over-prioritize the favorite genre and miss songs from other genres that
still fit the user's mood or energy.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 17

Top recommendations:

Focus Flow - Score: 10.85
Because: genre match (+4.0); mood match (+3.0); energy close to target (+2.85); acoustic preference match (+1.0)

Midnight Coding - Score: 7.91
Because: genre match (+4.0); energy close to target (+2.91); acoustic preference match (+1.0)

Library Rain - Score: 7.70
Because: genre match (+4.0); energy close to target (+2.70); acoustic preference match (+1.0)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- I tested the default lofi, focused profile. `Focus Flow` ranked first because
  it matched the genre and mood while staying close to the target energy.
- I also tested a pop, happy profile with target energy 0.8. `Sunrise City`
  ranked first, followed by `Gym Hero` and `Rooftop Lights`, which matched my
  expectation for that profile.

---

## Limitations and Risks

This recommender only works with 17 songs and a few hand-written labels. It
does not use lyrics, listening history, skips, or feedback from other users.
Genre has the largest weight, so the system can overlook a song from another
genre that fits the user's energy and mood.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this version helped me see that a recommender starts with choices about
what counts as a useful signal. I used genre, mood, energy, and acousticness,
then turned those choices into points. The ranking was easy to read because
each score came with reasons, but I can also see how changing one weight can
shift the whole list.

I also learned that a simple system can be biased by its own design. My
favorite-genre weight is strong, so it keeps the recommendations close to what
the profile already likes. A larger system would need more data and a way to
make room for discovery instead of only repeating the same type of music.



