from beet import ResourcePack
from generator.libs.debugger import debug
from generator.libs.sound_config import *

def main(rp: ResourcePack):
    debug(__name__, f"running module", True)
    entries = [
        entry("entity.ghast.ambient", [
            "aagh",
            sound("aagh", 1.2),
            sound("aagh", 0.85, 1.5)
        ])
    ]
    
    create_sound_config(rp, entries)