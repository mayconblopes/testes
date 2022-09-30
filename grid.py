import os
import flet
from flet import Container, Page, Row, Text, alignment, border, border_radius, colors, GridView

os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'

def main(page: Page):
    gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)


    for i in range(18):
        gv.controls.append(
            Container(
                Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_400),
                border_radius=border_radius.all(5),
            )
        )
    page.update()

flet.app(target=main, port=8000)