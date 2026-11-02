# 🎧 Model Card: FocusFlow

## 1. Model Name

FocusFlow is a small music recommender simulation.

## 2. Goal / Task

The system suggests songs from a small catalog based on a user's favorite
genre, mood, target energy, and acoustic preference.

## 3. Data Used

The catalog has 17 songs. Each song includes genre, mood, energy, tempo,
valence, danceability, and acousticness. I added seven songs to make the
starter catalog more varied. The data does not include lyrics, listening
history, skips, saves, or feedback from real people.

## 4. Algorithm Summary

FocusFlow scores one song at a time. A genre match adds 4 points, a mood match
adds 3 points, energy closeness adds up to 3 points, and a matching acoustic
preference adds 1 point. It sorts all songs from highest to lowest score and
shows the top results with reasons.

## 5. Observed Behavior / Biases

The system works well when a profile has clear genre and mood preferences. For
a lofi, focused profile, `Focus Flow` ranked first. For a pop, happy profile,
`Sunrise City` ranked first. Genre has the largest weight, so the system can
over-favor familiar music and miss songs from other genres that fit the same
mood or energy.

## 6. Evaluation Process

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles. The top
results fit the main genre, mood, and energy preferences: `Sunrise City`,
`Library Rain`, and `Storm Runner` each ranked first for their matching
profiles. I also tested a weight shift by cutting the genre score from 4 to 2
and doubling the maximum energy score from 3 to 6. That made the results more
energy-focused, but not clearly more accurate, so I restored the original
weights. The two starter tests pass.

## 7. Intended Use and Non-Intended Use

This is for classroom exploration of basic recommendation logic. It can help
show how a few preferences become a ranked list. It should not be used to make
real music recommendations or assumptions about a person's taste because the
catalog and profile are too small.

## 8. Ideas for Improvement

- Add a diversity rule so the top results are not all from one genre.
- Let users mark songs as saved or skipped, then use that feedback later.
- Add more songs and more than one mood or genre preference per profile.

## 9. Personal Reflection

The biggest learning moment for me was seeing how a small weight change could
reorder the recommendations. When I made energy more important and genre less
important, songs with closer energy values moved ahead of some genre matches.
That made the system feel less like a neutral list and more like a set of
choices I had built into the rules.

AI tools helped me brainstorm features, compare profile results, and check the
scoring idea. I still needed to read the score reasons and test the output
myself because a suggested rule can be mathematically valid without matching
what I want the recommender to do. If I extended this project, I would add more
user feedback and a diversity rule before adding more complex features.
