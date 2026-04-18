from beet import ResourcePack, SoundConfig as BeetSoundConfig, NamespaceFileScope
from generator.libs.debugger import debug

from typing import ClassVar

class SoundConfig(BeetSoundConfig):
    scope: ClassVar[NamespaceFileScope] = ("",)
    extension: ClassVar[str] = ".json"

def create_sound_config(rp: ResourcePack, entries: list[dict]):
    debug(__name__, f"creating sounds.json with {entries.__len__()} entrie(s)")
    contents: dict = dict()
    for entry in entries:
        contents.update(entry)

    rp["minecraft:sounds"] = SoundConfig(dict(contents))

def entry(id: str, sounds: list[dict | str]) -> dict:
    debug(__name__, f'creating sounds.json entry "{id}" with {sounds.__len__()} sound(s)')
    for sound in sounds:
        if isinstance(sound, list):
            raise ValueError("sounds list contains list(s)")
    return dict({
        id: {
            "replace": True,
            "sounds": sounds,
            "subtitle": f"subtitles.{id}"
        }
    })

def sound(name: str, pitch: float = 1.0, volume: float = 1.0) -> dict:
    return dict({
        "name": name,
        "pitch": pitch,
        "volume": volume
    })

def sounds(name:str, count: int, pitch_osc: float, volume: float):
    debug(__name__, f'creating {count * 2 + 1} "{name}" sounds')
    to_return: list[dict | str] = [name]
    for i in range(count):
        to_return.append(sound(name, 1.0 + pitch_osc * i, volume))
        to_return.append(sound(name, 1.0 - pitch_osc * i, volume))
    
    return to_return