from dataclasses import dataclass


@dataclass
class SpotifyTrack:
    trackID: str
    artist: str
    name: str
    uri: str



@dataclass
class PixabayImage:
    imageID: int
    url: str