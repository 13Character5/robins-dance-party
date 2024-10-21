controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    Player1.setPosition(160 / 5 * 2, 100)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    Player1.setPosition(160 / 5, 100)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    Player1.setPosition(160 / 5 * 4, 100)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprites.destroy(otherSprite, effects.confetti, 100)
    info.changeScoreBy(10)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    Player1.setPosition(160 / 5 * 3, 100)
})
info.onLifeZero(function on_life_zero() {
    game.gameOver(true)
})
scene.onHitWall(SpriteKind.Projectile, function on_hit_wall(sprite2: Sprite, location: tiles.Location) {
    sprites.destroy(sprite2, effects.ashes, 100)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.InBackground)
    info.changeLifeBy(-1)
})
let right : Sprite = null
let down : Sprite = null
let up : Sprite = null
let left : Sprite = null
let lane = 0
let Player1 : Sprite = null
game.splash("Dance Party")
info.setLife(5)
tiles.setCurrentTilemap(tilemap`
    level1
`)
effects.confetti.startScreenEffect()
Player1 = sprites.create(img`
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
    `, SpriteKind.Player)
Player1.setPosition(80, 100)
let Speed = 40
info.setScore(0)
game.onUpdateInterval(2000, function on_update_interval() {
    
    Speed += 1
})
game.onUpdateInterval(500, function on_update_interval2() {
    
    lane = randint(1, 4)
    if (lane == 1) {
        left = sprites.create(assets.image`
            left
        `, SpriteKind.Projectile)
        left.setPosition(160 / 5, -20)
        left.setVelocity(0, Speed)
    } else if (lane == 2) {
        up = sprites.create(assets.image`
            up
        `, SpriteKind.Projectile)
        up.setPosition(160 / 5 * 2, -20)
        up.setVelocity(0, Speed)
    } else if (lane == 3) {
        down = sprites.create(assets.image`
            down
        `, SpriteKind.Projectile)
        down.setPosition(160 / 5 * 3, -20)
        down.setVelocity(0, Speed)
    } else if (lane == 4) {
        right = sprites.create(assets.image`
            right
        `, SpriteKind.Projectile)
        right.setPosition(160 / 5 * 4, -20)
        right.setVelocity(0, Speed)
    }
    
})
