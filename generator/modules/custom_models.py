from beet import ResourcePack
from beet.contrib.vanilla import Vanilla
from generator.libs.debugger import debug
from generator.libs.custom_models import *

def create_plush_model(rp: ResourcePack, player: str, variant: str = "default") -> str:
    return create_child_model(rp, "stove:item/plush", f"stove:item/plush/{player}/{variant}")

def main(rp: ResourcePack, vanilla: Vanilla) -> dict[str, str]:
    debug(__name__, f"running module", True)

    plushes: dict[str, int] = {}

    plush_players: dict[str, int] = {}
    plush_variants: dict[str, int] = {
        "default": 0,
        "evil": 1,
        "roleplay": 2,
        "legacy": 3
    }
    for texture in rp.textures:
        if texture.startswith("stove:item/plush/"):
            split: list[str] = texture.split("/")
            player = split[-2]
            variant = split[-1]

            value = 0

            if not player in plush_players:
                plush_players[player] = (list(plush_players.values())[-1] if plush_players else 0) + 1
            value += plush_players[player] * 100

            if not variant in plush_variants:
                plush_variants[variant] = (list(plush_variants.values())[-1] if plush_players else 0) + 1
            value += plush_variants[variant]

            plushes[create_plush_model(rp, player, variant)] = value
    
    debug(__name__, f"registered plushes for {plush_players.__len__()} players and {plush_variants.__len__()} variants")
                
    give_custom_models(rp, "minecraft:item/paper", vanilla, plushes)

    return plushes
