def on_up_pressed():
    Player1.set_position(160 / 5 * 2, 100)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    Player1.set_position(160 / 5, 100)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Player1.set_position(160 / 5 * 4, 100)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.confetti, 100)
    info.change_score_by(10)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_down_pressed():
    Player1.set_position(160 / 5 * 3, 100)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.game_over(True)
info.on_life_zero(on_life_zero)

def on_hit_wall(sprite2, location):
    sprites.destroy(sprite2, effects.ashes, 100)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)

right: Sprite = None
down: Sprite = None
up: Sprite = None
left: Sprite = None
lane = 0
Player1: Sprite = None
game.splash("Dance Party")
info.set_life(5)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
effects.confetti.start_screen_effect()
Player1 = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
Player1.set_position(80, 100)
Speed = 40
info.set_score(0)

def on_update_interval():
    global Speed
    Speed += 1
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    global lane, left, up, down, right
    lane = randint(1, 4)
    if lane == 1:
        left = sprites.create(assets.image("""
            left
        """), SpriteKind.projectile)
        left.set_position(160 / 5, -20)
        left.set_velocity(0, Speed)
    elif lane == 2:
        up = sprites.create(assets.image("""
            up
        """), SpriteKind.projectile)
        up.set_position(160 / 5 * 2, -20)
        up.set_velocity(0, Speed)
    elif lane == 3:
        down = sprites.create(assets.image("""
            down
        """), SpriteKind.projectile)
        down.set_position(160 / 5 * 3, -20)
        down.set_velocity(0, Speed)
    elif lane == 4:
        right = sprites.create(assets.image("""
            right
        """), SpriteKind.projectile)
        right.set_position(160 / 5 * 4, -20)
        right.set_velocity(0, Speed)
game.on_update_interval(500, on_update_interval2)
