from alexis import Command
from alexis.utils import img_embed


class Avatar(Command):
    def __init__(self, bot):
        super().__init__(bot)
        self.name = 'avatar'
        self.help = '$[avatar-help]'

    async def handle(self, cmd):
        user = cmd.author if cmd.argc == 0 else await cmd.get_user(cmd.text)
        if user is None:
            await cmd.answer('$[user-not-found]')
            return

        has_avatar = user.avatar_url != ''
        avatar_url = user.avatar_url if has_avatar else user.default_avatar_url

        text = '$[user-avatar]' if has_avatar else '$[user-avatar-no]'
        await cmd.answer(embed=img_embed(avatar_url, text), locales={'user': user.display_name})
