from beet import Context, load_config, locate_config
from beet.contrib.vanilla import Vanilla

from generator.modules.custom_models import main as custom_models
from generator.modules.sounds import main as sounds
from generator.libs.debugger import debug

def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)
    rp = ctx.assets

    custom_models(rp, vanilla)
    sounds(rp)

    config = load_config(locate_config(ctx.directory))
    debug(__name__, f'built resource pack as {".zip file" if config.resource_pack.zipped else "folder"}', True)