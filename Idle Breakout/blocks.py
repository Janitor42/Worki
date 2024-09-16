from wrap import sprite as sp
import wrap
import finance
import frame_statistics

colors = [[20, 150, 255], [218, 71, 255], [250, 144, 77],
          [255, 255, 94], [92, 255, 173], [97, 92, 255],
          [247, 30, 197], [255, 59, 88], [125, 245, 86]]


def create_image_value(count):
    if count >= 10000:
        return '' + str(count) + ''
    if count >= 1000:
        return ' ' + str(count) + ' '
    if count >= 100:
        return '  ' + str(count) + '  '
    if count >= 10:
        return '   ' + str(count) + '   '
    if count < 10:
        return '    ' + str(count) + '    '




class Block:
    all_damage = 0
    protect_power = 1
    all_blocks = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.line_with_text = create_image_value(Block.protect_power)

        self.value = Block.protect_power

        self.name = sp.add_text(self.line_with_text, self.x, self.y, font_name='Times New Roman')
        color_now = (self.value % 10) - 1

        wrap.sprite_text.set_back_color(self.name, colors[color_now][0], colors[color_now][1], colors[color_now][2])

        self.state = True

        Block.all_blocks.append(self)


    def __del__(self):
        sp.remove(self.name)

    def change_block(self, pover_ball):

        Block.all_damage += pover_ball
        finance.count_money(pover_ball)

        frame_statistics.redraw_text(Block.all_damage)

        self.value -= pover_ball
        value = create_image_value(self.value)
        wrap.sprite_text.set_text(self.name, str(value))

        color_now = (self.value % 10) - 1

        wrap.sprite_text.set_back_color(self.name, colors[color_now][0], colors[color_now][1], colors[color_now][2])

        if self.value <= 0:
            self.state = False

    def remove_block(self):
        if not self.state:
            wrap.sprite.hide(self.name)
            Block.all_blocks.remove(self)
