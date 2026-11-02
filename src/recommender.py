import csv
from dataclasses import asdict, dataclass
from typing import Dict, List, Tuple

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the highest-scoring songs for one user profile."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(user_prefs, asdict(song))[0],
            reverse=True,
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain which preferences helped a song's score."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, asdict(song))
        return "; ".join(reasons) or "No strong preference match."

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file with numeric values converted."""
    songs = []
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            for field, converter in numeric_fields.items():
                row[field] = converter(row[field])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song and return the score with the reasons behind it."""
    score = 0.0
    reasons = []
    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    target_energy = user_prefs.get("target_energy", user_prefs.get("energy"))

    if song["genre"] == favorite_genre:
        score += 4.0
        reasons.append("genre match (+4.0)")

    if song["mood"] == favorite_mood:
        score += 3.0
        reasons.append("mood match (+3.0)")

    if target_energy is not None:
        energy_points = max(0.0, 3.0 * (1 - abs(song["energy"] - float(target_energy))))
        score += energy_points
        reasons.append(f"energy close to target (+{energy_points:.2f})")

    if "likes_acoustic" in user_prefs:
        likes_acoustic = user_prefs["likes_acoustic"]
        acoustic_match = (likes_acoustic and song["acousticness"] >= 0.6) or (
            not likes_acoustic and song["acousticness"] <= 0.4
        )
        if acoustic_match:
            score += 1.0
            reasons.append("acoustic preference match (+1.0)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score, explain, and rank the top k songs for one set of preferences."""
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) or "No strong preference match."
        ranked.append((song, score, explanation))

    return sorted(ranked, key=lambda recommendation: recommendation[1], reverse=True)[:k]
