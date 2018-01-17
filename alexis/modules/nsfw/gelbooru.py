from urllib.parse import urlencode
from xml.etree.ElementTree import fromstring as parsexml
from random import choice

from alexis import Command
from alexis.base.utils import img_embed


class Gelbooru(Command):
    def __init__(self, bot):
        super().__init__(bot)
        self.name = 'gelbooru'
        self.nsfw_only = True

    async def handle(self, message, cmd):
        if cmd.argc < 1:
            await cmd.answer('formato: $PX$NM <texto de búsqueda>')
            return

        await cmd.typing()

        query = {
            'page': 'dapi',
            's': 'post',
            'q': 'index',
            'tags': cmd.text
        }

        q_url = 'https://gelbooru.com/index.php?' + urlencode(query)
        async with self.http.get(q_url) as r:
            posts = parsexml(await r.text()).findall('post')
            if len(posts) == 0:
                await cmd.answer('sin resultados :c')
                return

            post = choice(posts)
            await cmd.answer(img_embed(post.get('file_url')))
