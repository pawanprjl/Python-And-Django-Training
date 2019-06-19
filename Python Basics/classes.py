class Enemy:

    id = 0

    def __init__(self, life):
        self.life = life
        self.enemyId = Enemy.id
        Enemy.id += 1

    def returnId(self):
        return self.enemyId

en = Enemy(5)
