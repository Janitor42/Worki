import wrap
import random
class Shar():
    # magig metod
    def __init__(self,x,y,scale,friend):
        self.sh=wrap.sprite.add('pacman', x, y, 'player2')
        self.friends=friend
        wrap.sprite.set_size(self.sh,scale,scale)
        self.rd_x=random.randint(1,5)
        self.rd_y = random.randint(1, 5)
        self.b=scale
    def add_five(self):
        self.b+=5
    def go(self):
        wrap.sprite.move(self.sh,self.rd_x,self.rd_y)
        if wrap.sprite.get_x(self.sh)>=800-self.b/2:
            self.rd_x=-self.rd_x
        if wrap.sprite.get_x(self.sh) <= self.b/2:
            self.rd_x = abs(self.rd_x)
        if wrap.sprite.get_y(self.sh)>=500-self.b/2:
            self.rd_y=-self.rd_y
        if wrap.sprite.get_y(self.sh) <= self.b/2:
            self.rd_y = abs(self.rd_y)
        self.b=100
        wrap.sprite.set_size(self.sh,100,100)
        while  self._collise():
            self.b -=1
            wrap.sprite.set_size(self.sh, self.b, self.b)


    def _collise(self):
        for i in self.friends:
            if i is self:
                continue
            if wrap.sprite.is_collide_sprite(self.sh,i.sh):
                return True
        return False









