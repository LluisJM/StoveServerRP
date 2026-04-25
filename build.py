from beet import Context, load_config, locate_config
from beet.contrib.vanilla import Vanilla

from generator.modules.custom_models import main as custom_models
from generator.modules.custom_formatting import main as custom_formatting
from generator.modules.sounds import main as sounds

from generator.libs.debugger import debug

def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)
    rp = ctx.assets
    dp = ctx.data
    config = load_config(locate_config(ctx.directory))

    plushes = custom_models(rp, vanilla)
    sounds(rp)

    rp.save("./build", "resources", True, overwrite=True)
    debug(__name__, f'built resource pack as zip file\n', True)
    debug(__name__, f'building resource pack as {".zip file" if config.resource_pack.zipped else "folder"}\n', True)

    custom_formatting(dp, plushes)

    rp.save("./build", "resource-utils", True, overwrite=True)
    debug(__name__, f'built resource pack as zip file\n', True)
    debug(__name__, f'building data pack as {".zip file" if config.data_pack.zipped else "folder"}\n', True)