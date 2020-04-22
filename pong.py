# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
direction = RIGHT
ball_pos = [WIDTH /2, HEIGHT /2]
ball_radius = 20
ball_vel = [0,1]
paddle1_pos = HEIGHT / 2.5
paddle2_pos = HEIGHT / 2.5
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH /2, HEIGHT /2]
    ball_vel[0] = -random.randrange(120, 240) / 100

    if direction:
        ball_vel[0] *= -1

    ball_vel[1] = -random.randrange(60, 180) / 100

# helper function for collision detection
def is_collision(ball_pos, paddle_pos):
    if paddle_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle_pos + HALF_PAD_HEIGHT:
        return True
    else:
        return False


# define event handlers
def restart():
    new_game()

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(True)
    paddle1_pos = HEIGHT / 2.5
    paddle2_pos = HEIGHT / 2.5

def draw(canvas):
    global score1, score2
    global paddle1_pos, paddle2_pos
    global ball_pos, ball_vel
    global paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # rebound off of ceiling or floor
    if (ball_pos[1] <= BALL_RADIUS or
        ball_pos[1] >= (HEIGHT - BALL_RADIUS)):
        ball_vel[1] *= -1

    # Ball at left gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if is_collision(ball_pos, paddle1_pos):
            ball_vel[0] *= -1
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)

    # Ball at right gutter
    if ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS:
        if is_collision(ball_pos, paddle2_pos):
            ball_vel[0] *= -1
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(
        ball_pos,
        BALL_RADIUS,
        2,
        "Green",
        "White"
    )

    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos + HALF_PAD_HEIGHT <= HEIGHT and
         paddle1_vel > 0) or
        (paddle1_pos - HALF_PAD_HEIGHT >= 0 and paddle1_vel < 0)) :
        paddle1_pos += paddle1_vel
    elif ((paddle2_pos + HALF_PAD_HEIGHT <= HEIGHT and
          paddle2_vel > 0) or
          (paddle2_pos - HALF_PAD_HEIGHT >= 0 and
           paddle2_vel < 0)) :
        paddle2_pos += paddle2_vel

    # draw paddles
    # Left paddle
    canvas.draw_polygon(
        [
            (0, paddle1_pos - HALF_PAD_HEIGHT),
            (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
            (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),
            (0, paddle1_pos + HALF_PAD_HEIGHT)
        ],
        1,
        "White",
        "White"
    )

    # Right paddle
    canvas.draw_polygon(
        [
            (WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
            (WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
            (WIDTH, paddle2_pos + HALF_PAD_HEIGHT),
            (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)
        ],
        1,
        "White",
        "White"
    )

    # determine whether paddle and ball collide

    # draw scores
    canvas.draw_text(str(score1), [225, 100], 60, "White")
    canvas.draw_text(str(score2), [350, 100], 60, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    paddle_vel = 10

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 200)


# start frame
new_game()
frame.start()

